"""Topic-robust style features. Content words are never used as features.

Each document -> dict of {feature_name: value}:
  fw:<word>   closed-class (function) word rate per token
  pos:<A_B_C> coarse POS trigram rate per token
  dep:<label> dependency label rate per token
  pun:<char>  punctuation rate per token
  s:<name>    scalars (sentence length mean/sd, word length, MTLD)
"""
import re
from collections import Counter
from statistics import mean, pstdev

import spacy

CLOSED = {"ADP", "AUX", "CCONJ", "DET", "PART", "PRON", "SCONJ"}
PUNCT = list(",;:()\"'!?") + ["—", "–", "-"]  # em dash, en dash, hyphen
MAX_WORDS = 250  # every text is cut to its first 250 words so length can't drive results

_MD = [(re.compile(r"\*\*|__|`|^#+\s*", re.M), ""),
       (re.compile(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])"), r"\1"),  # *italic*
       (re.compile(r"^\s*(abstract|title|speech|essay)\s*:\s*", re.I | re.M), ""),
       (re.compile(r"^\s*([-*•]|\d+[.)])\s+", re.M), "")]


# typographic variants that are rendering artefacts, not style: curly quotes, non-breaking/figure
# hyphens, non-breaking and narrow spaces. Em/en dashes are kept: they are a real stylistic choice.
_QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                         "‐": "-", "‑": "-", "‒": "-", " ": " ", " ": " "})
_WRAPPER = re.compile(r"^\W*(here'?s|here is|below is|sure|okay|certainly|of course)\b"
                      r"(.*:\s*$|.*\b(essay|abstract|speech|version|revis\w*|rewrit\w*|response)\b)", re.I | re.S)
_NOTE = re.compile(r"^\s*(\*?\(?note|word count|i hope|let me know)", re.I)


_MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|\\\(.*?\\\)|\\\[.*?\\\]", re.S)
_KEEP = re.compile(r"\\(emph|textit|textbf|textsc|texttt|textrm|mathrm|text|it|bf)\s*\{([^{}]*)\}")


def delatex(text):
    """Map LaTeX conventions (common in human arXiv abstracts, rare in LLM output) to plain typography so
    the instrument cannot separate human from LLM text by encoding: math -> 'X', '---'/'--' -> em/en dash,
    formatting commands -> their content, other commands removed."""
    text = _MATH.sub(" X ", text)
    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = _KEEP.sub(r"\2", text)
    text = re.sub(r"\\(cite[tp]?|ref|url|label)\{[^}]*\}", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text).replace("~", " ").replace("``", '"').replace("''", '"')
    text = re.sub(r"\\([%&_#$])", r"\1", text)  # escaped symbols: \% -> %
    return text.replace("{", "").replace("}", "")


def unwrap(text):
    """Drop chat wrappers: 'Here's the essay:' intro, '---' rules, markdown headings,
    all-bold title lines, trailing notes. Applied to human text too (rarely matches)."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text.translate(_QUOTES)) if p.strip()]
    if paras and len(paras[0].split()) < 40 and _WRAPPER.search(paras[0]):
        paras = paras[1:]
    keep = []
    for p in paras:
        lines = [ln for ln in p.splitlines()
                 if not re.fullmatch(r"\s*(-{3,}|\*{3,}|#.*|\*\*[^*]+\*\*)\s*", ln)]
        if lines:
            keep.append("\n".join(lines))
    while keep and _NOTE.match(keep[-1]):
        keep.pop()
    return "\n\n".join(keep)


def clean(text):
    """Strip wrappers, markdown and labels so formatting artefacts can't give LLM text away."""
    text = delatex(unwrap(text))  # unwrap first: a markdown '---' rule is not a dash
    for pat, rep in _MD:
        text = pat.sub(rep, text)
    words = text.split()
    return " ".join(words[:MAX_WORDS])


def mtld(tokens, threshold=0.72):
    """Measure of Textual Lexical Diversity (McCarthy & Jarvis 2010), forward+backward mean."""
    def one_pass(seq):
        factors, types, count = 0.0, set(), 0
        for t in seq:
            types.add(t)
            count += 1
            if len(types) / count <= threshold:
                factors += 1
                types, count = set(), 0
        if count:
            factors += (1 - len(types) / count) / (1 - threshold)
        return len(seq) / factors if factors else float(len(seq))
    if len(tokens) < 10:
        return float("nan")
    return (one_pass(tokens) + one_pass(tokens[::-1])) / 2


def doc_features(doc):
    toks = [t for t in doc if not t.is_space]
    n = max(len(toks), 1)
    words = [t for t in toks if t.is_alpha]
    f = Counter()
    for t in toks:
        if t.pos_ in CLOSED:
            f["fw:" + t.lower_] += 1
        f["dep:" + t.dep_] += 1
        if t.text in PUNCT:
            f["pun:" + t.text] += 1
    pos = [t.pos_ for t in toks]
    for i in range(len(pos) - 2):
        f["pos:" + "_".join(pos[i:i + 3])] += 1
    out = {k: v / n for k, v in f.items()}
    sents = [sum(1 for t in s if not t.is_punct and not t.is_space) for s in doc.sents]
    sents = [s for s in sents if s > 0] or [0]
    out["s:sent_mean"] = mean(sents)
    out["s:sent_sd"] = pstdev(sents)
    out["s:word_len"] = mean(len(w) for w in words) if words else 0.0
    out["s:mtld"] = mtld([w.lower_ for w in words])
    return out


def extract(texts, n_process=5):
    nlp = spacy.load("en_core_web_sm", disable=["ner", "lemmatizer"])
    docs = nlp.pipe((clean(t) for t in texts), batch_size=200, n_process=n_process)
    return [doc_features(d) for d in docs]


if __name__ == "__main__":
    a = "**Abstract:** We propose a novel framework that delves into robust learning — and it works."
    assert clean(a).startswith("We propose") and "**" not in clean(a)
    g = "Okay, here’s an essay responding to the prompt:\n\n---\n\n## Ditch the Drive?\n\nCars are bad.\n\nNote: 250 words."
    assert clean(g) == "Cars are bad.", clean(g)
    g2 = "Okay, here's an essay responding to the prompt, aiming for a student voice.\n\nCars are bad."
    assert clean(g2) == "Cars are bad.", clean(g2)
    assert clean("Here we present a method.\n\nIt works.").startswith("Here we")  # human abstracts kept
    h = r"We prove that $f(x)\le 1$ --- a \emph{sharp} bound~\cite{a} --- holds for $n$--$m$ pairs."
    assert clean(h) == "We prove that X — a sharp bound — holds for X – X pairs.", clean(h)
    g3 = "**Abstract**  \nLong‑document work. We introduce *Sparse Attention* (SA), 2 * 3 = 6."
    assert clean(g3) == "Long-document work. We introduce Sparse Attention (SA), 2 * 3 = 6.", clean(g3)
    feats = extract([a, "The cat sat on the mat. It was happy, and so was I."], n_process=1)
    assert feats[0]["pun:—"] > 0 and feats[1]["fw:the"] > 0
    assert not any(k.startswith("fw:novel") for k in feats[0])  # content words excluded
    print("features ok", len(feats[0]), "features in doc 1")
