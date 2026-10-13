"""results/*.json|csv -> results/numbers.tex. The paper cites numbers only as \\R{file.row.column};
a missing key is a LaTeX error, so text and results cannot drift apart.
"""
import json, math, re
from pathlib import Path

import pandas as pd

RES = Path(__file__).resolve().parent.parent / "results"
PCT = ("mso", "recall", "share", "excess", "level_shift", "slope_change", "pre_slope", "lo", "hi", "difference")
# note: "corr_*" keys are correlations (2 dp), handled by the default branch
KEYCOLS = ("group", "held_out_model", "feature", "fake_break")


def fmt(key, v):
    leaf = key.rsplit(".", 1)[-1]
    if isinstance(v, str):
        return v.replace("_", r"\_").replace("&", r"\&")
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "--"
    if leaf == "p" or leaf.endswith("_p") or leaf == "p_value" or ".field_holm." in key:
        return r"{<}0.001" if v < 0.001 else f"{v:.3f}"
    if leaf == "relative_gap":  # "about 2.1 times the trend": one decimal is the honest precision
        return f"{v:.1f}"
    if "dispersion" in key or leaf == "logit_gap":  # distances, not shares
        return f"{v:.2f}"
    if leaf in ("n", "months", "dof", "ell_in_region", "median_words", "n_breaks") or leaf.startswith("n_") or "_n_" in leaf:
        return f"{int(v):,}"
    if re.fullmatch(r"[ym]\d{4}", leaf) or leaf in ("in_04", "in_06", "marker") or "alpha" in leaf or \
            leaf.startswith(("change", "gap", "marker_gap", "linear_", "quadratic_", "trend_at", "diff", "resid",
                             "median_abs", "max_abs", "tpr", "fpr", "median_retained")):
        return f"{100 * v:.1f}"
    if leaf.startswith(("or_", "odds", "coef", "ell_coef", "corr", "rho")):  # rho_lo/rho_hi are correlations too
        return f"{v:.2f}"
    if ".field_share." in key or leaf.startswith("summary_share"):
        return f"{100 * v:.1f}"
    if "auc" in leaf:
        return f"{v:.3f}"
    if leaf.startswith(PCT) or leaf.endswith(PCT):
        return f"{100 * v:.1f}"  # percentage points, no % sign (added in text)
    return f"{v:.2f}"


def flatten(prefix, obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            flatten(f"{prefix}.{k}", v, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            name = v.get("fake_break", i) if isinstance(v, dict) else i
            flatten(f"{prefix}.{name}", v, out)
    else:
        out[prefix] = fmt(prefix, obj)


def main():
    out = {}
    for f in sorted(RES.glob("*.json")):
        flatten(f.stem, json.loads(f.read_text()), out)
    for f in sorted(RES.glob("*.csv")):
        df = pd.read_csv(f)
        if "model" in df and "prompt" in df:
            df.index = df.model.astype(str) + "/" + df.prompt.astype(str)
        else:
            col = next((c for c in KEYCOLS if c in df), None)
            if col is None:
                continue  # time series: figures only
            df.index = df[col].astype(str)
        for row, r in df.iterrows():
            for c, v in r.items():
                flatten(f"{f.stem}.{row}.{c}", v, out)
    lines = [r"\newcommand{\R}[1]{\ifcsname r@#1\endcsname\csname r@#1\endcsname\else"
             r"\errmessage{Missing result #1}\fi}"]
    lines += [rf"\expandafter\def\csname r@{k}\endcsname{{{v}}}" for k, v in sorted(out.items())]
    (RES / "numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(len(out), "numbers")
    feature_table()


def missing(tex=RES.parent / "paper" / "main.tex"):
    """\\R keys used in the paper but absent from numbers.tex (LaTeX stops at the first one)."""
    have = set(re.findall(r"r@(.+?)\\endcsname", (RES / "numbers.tex").read_text(encoding="utf-8")))
    used = set(re.findall(r"\\R\{([^}]*)\}", Path(tex).read_text(encoding="utf-8")))
    return sorted(used - have)


def tex_feature(f):
    """'pos:DET_NOUN_VERB' -> readable LaTeX label."""
    kind, name = f.split(":", 1)
    name = {"mtld": "MTLD lexical diversity", "sent_mean": "sentence length (mean)",
            "sent_sd": "sentence length (SD)", "word_len": "word length"}.get(name, name)
    label = {"fw": "word", "pos": "POS trigram", "dep": "dependency", "pun": "punctuation", "s": ""}[kind]
    name = name.replace("_", r"\_").replace('"', "''")
    if kind in ("fw", "pun"):
        name = r"\textit{" + name + "}" if kind == "fw" else r"\texttt{" + name.replace("-", "-{}") + "}"
    return (label + " " + name).strip()


def feature_table(k=10):
    """Top-k LLM-typical and human-typical arXiv features (standardised logistic coefficients) as table rows."""
    up = pd.read_csv(RES / "arxiv_features_llm_typical.csv").head(k)
    down = pd.read_csv(RES / "arxiv_features_human_typical.csv").head(k)
    rows = [f"{tex_feature(a)} & ${b:.2f}$ & {tex_feature(c)} & ${d:.2f}$ \\\\"
            for a, b, c, d in zip(up.feature, up.coef, down.feature, down.coef)]
    # \bottomrule must follow the last row directly; after an \input it is a misplaced \noalign
    (RES / "feature_table.tex").write_text("\n".join(rows) + "\n\\bottomrule\n", encoding="utf-8")


if __name__ == "__main__":
    assert fmt("x.mso", 0.0351) == "3.5" and fmt("x.p_value", 0.0001) == r"{<}0.001"
    assert fmt("x.odds_ratio", 0.356) == "0.36" and fmt("x.n", 7424) == "7,424"
    assert fmt("x.or_lo", 0.1656) == "0.17" and fmt("x.cv_auc_all", 0.98763) == "0.988"
    assert fmt("x.level_shift_p", 0.894) == "0.894" and fmt("x.level_shift", 0.0465) == "4.7"
    assert fmt("x.arxiv_n_fields", 8.0) == "8" and fmt("x.n_generators", 8.0) == "8" and fmt("x.y2025", 0.3644) == "36.4" and fmt("x.excess_p", 0.2) == "0.200"
    assert fmt("robustness_v3.field_holm.cs", 0.0123) == "0.012" and fmt("x.m2016", 0.05) == "5.0"
    assert fmt("a_dispersion_trend.gap_2025.ci_lo", -0.36) == "-0.36" and fmt("x.logit_gap", 0.28) == "0.28"
    assert fmt("x.cs_2024_alpha_cv", 0.12) == "12.0" and fmt("x.relative_gap", 2.31) == "2.3"
    main()
