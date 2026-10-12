# 04 — Data sources and venues (checked 2026-10-12)

Rules: only what was found online, with URLs. **UNVERIFIED** = not confirmed from a primary/official page. No deadline below is invented; "not announced" means I searched and found nothing.

---

## PART A — DATA

### A1. arXiv abstracts (main human corpus)

| Source | Access | Licence | Size / coverage | Account? |
|---|---|---|---|---|
| **arXiv OAI-PMH** `https://oaipmh.arxiv.org/oai` | Formats `oai_dc`, `arXiv` (category + licence fields), `arXivRaw` (version history incl. v1 dates). Sets like `cs:cs:CL`. Resumption tokens expire daily. | Metadata "may be reused in non-commercial and commercial systems", see API Terms of Use. https://info.arxiv.org/help/oa/index.html | All papers, updated daily. arXiv passed 3M articles (blog, 9 Jul 2026) | No |
| **Kaggle "Cornell-University/arxiv"** (`arxiv-metadata-oai-snapshot.json`) | Kaggle download / `kaggle datasets download` | CC0 1.0 (stated on HF mirror card https://huggingface.co/datasets/arxiv-community/arxiv_dataset) | Weekly updates at launch (2020). A 2026 paper used it for 2,823,623 papers. Current file size: **UNVERIFIED** (Kaggle page did not render) | **Yes**, API needs a Kaggle account + `kaggle.json` token (third-party tutorials). Whether browser download needs login: **UNVERIFIED** |
| HF `arxiv-community/arxiv_dataset` | Loader only, 13 kB. Says to download the Kaggle archive manually | CC0 | Card says ~1.7M papers (old) | HF account not needed, but Kaggle is |
| Other HF mirrors | Found only small or stale ones (e.g. `gr8monk3ys/academic-papers-dataset`, 2,019 papers). **No full, current 2025/2026 HF mirror was confirmed** | varies | | |

arXiv bulk-access etiquette (https://info.arxiv.org/help/bulk_data.html): OAI-PMH is "the preferred way" to keep metadata; use `export.arxiv.org`; burst up to 4 req/s then sleep 1 s. Do not crawl full text programmatically (S3 is for full text).

**Recommendation:** use the Kaggle snapshot (one file, CC0) for the 2018–2026 abstracts, use OAI-PMH `arXivRaw` only if v1 submission dates are needed. Filter `cs.CL`, plus non-CS controls (e.g. math, physics).

### A2. UK Hansard (control corpus) and other timestamped spoken corpora

| Source | Notes | Licence | Account? |
|---|---|---|---|
| **TheyWorkForYou / ParlParse XML** | `rsync data.theyworkforyou.com::parldata`, folder `scrapedxml/debates/` (per-day files `debatesYYYY-MM-DDx.xml`). Browse at http://www.theyworkforyou.com/pwdata/scrapedxml/. Git mirror "currently unavailable". https://parser.theyworkforyou.com/hansard.html. Coverage: main chambers from 1918; Westminster Hall from 1999/2001 (https://data.mysociety.org/datasets/uk-hansard/). Whether **2025–2026 files are present: UNVERIFIED** (directory listing too large to read; the TWFY site returned 503). Check with `rsync data.theyworkforyou.com::parldata/scrapedxml/debates/ \| grep debates2025` | Parliamentary material reusable under the **Open Parliament Licence** per the TWFY API page (archived 2016 copy, **UNVERIFIED current**). Request credit "Data service provided by TheyWorkForYou" | No (rsync is anonymous) |
| TheyWorkForYou API | Free for low-volume non-profit use (≤50k calls/yr, archived page) | as above | API key |
| **UK Parliament Hansard API** https://hansard-api.parliament.uk/ | Developer hub with an OpenAPI spec. Endpoints and terms not read (**UNVERIFIED**) | © UK Parliament. Open Parliament Licence assumed, **UNVERIFIED** (parliament.uk returned 403) | **UNVERIFIED** |
| HF Hansard datasets | **None found** with clear 2024–2025 UK coverage | | |
| **Australian Hansard corpus (Katz & Alexander), Zenodo v8, 14 Oct 2025** https://zenodo.org/records/7799467/latest | House of Representatives, **2 Mar 1998 – 31 Jul 2025**, single 580 MB parquet. Ready to use, a strong second control | **CC BY 4.0** | No |
| US Congressional Record (govinfo bulk) | GPO's listed bulk XML sets do not include the Congressional Record. A `CONGREC` folder is mentioned only by a third party (**UNVERIFIED**). https://www.govinfo.gov/developers | US gov work (generally public domain, not confirmed for this) | No |

**Recommendation:** use UK Hansard via rsync as the main control. Use the Australian Hansard parquet as a second, zero-effort control (it runs to Jul 2025, so it covers 2.5 years after ChatGPT).

### A3. Human-vs-AI datasets with commercial-model outputs

| Dataset | Commercial generators | Abstracts domain? | Licence | HF |
|---|---|---|---|---|
| **RAID** (Dugan et al. 2024) https://huggingface.co/datasets/liamdugan/raid | ChatGPT, **GPT-4**, GPT-3, Cohere (+ open: GPT-2, Llama-chat, Mistral, MPT). **No Claude/Gemini** | **Yes, `abstracts`** (+ books, news, poetry, recipes, reddit, reviews, wiki, code, czech, german) | **MIT** | Yes, ungated, `load_dataset("liamdugan/raid")`. 16.7 GB total; train 11.8 GB with adversarial, ~800 MB without |
| **DetectRL** (NeurIPS 2024) https://github.com/NLP2CT/DetectRL, paper https://arxiv.org/html/2410.23746 | GPT-3.5-turbo, PaLM-2-bison, **Claude-instant**, Llama-2-70b | **Yes, arXiv abstracts** (+ XSum, WritingPrompts, Yelp) | Dataset licence not stated (**UNVERIFIED**; paper is CC BY 4.0) | Not on HF yet ("soon"), GitHub only |
| **M4GT-Bench** https://github.com/mbzuai-nlp/M4GT-Bench (paper arXiv:2402.11175, CC BY 4.0) | Generator list not readable from page (**UNVERIFIED**, likely includes GPT-4) | **UNVERIFIED** | Repo licence not stated | Google Drive, not HF |
| **MAGE** https://github.com/yafuly/MAGE | 27 LLMs (OpenAI/LLaMA/EleutherAI families); GPT-4 for the "wilder" test set | Scientific writing included; PubMedQA in the wild set | Conflicting: Apache-2.0 (sidebar) vs CC BY 4.0 (badge) | Yes, `yaful/MAGE` |
| **HC3** https://huggingface.co/datasets/Hello-SimpleAI/HC3 | ChatGPT (version unspecified, early 2023) | No (ELI5, finance, medicine, open_qa, wiki_csai) | CC BY-SA 4.0 | Yes, 48.6k rows |
| **MIRAGE** (DetectAnyLLM, Sep 2025) https://arxiv.org/abs/2509.14268 | 17 LLMs incl. proprietary (GPT-4o, Claude named as motivation). Also includes "polish" and "rewrite" settings | 10 corpora / 5 domains (abstracts **UNVERIFIED**) | **UNVERIFIED** | Not found on HF. Project page https://fjc2005.github.io/detectanyllm |

**Gap:** no dataset was confirmed that has **Claude 3+/Gemini/GPT-4o outputs on arXiv abstracts** with a clear licence. Options: (a) RAID abstracts (GPT-4/ChatGPT, MIT) plus DetectRL abstracts (Claude-instant); (b) generate a small set locally with open models (A5). Note for the paper: open-model text is a proxy for commercial style, not a substitute.

### A4. Non-native learner English corpora

| Corpus | Access | Licence | Size |
|---|---|---|---|
| **ELLIPSE** https://github.com/scrosseye/ELLIPSE-Corpus | CSV on GitHub; test ZIP password `ellipse_test`; raw ZIP `ellipse_raw_data` | **CC BY-NC-SA 4.0** (GitHub). The Zenodo record (preprint PDF only) says CC BY 4.0 | ~6,500 ELL essays (grades 8–12, US) |
| **PERSUADE 2.0** https://github.com/scrosseye/persuade_corpus_2.0 | Google Drive CSVs; test ZIP password `persuade_test` | **CC BY-NC-SA 4.0** | 25,000+ argumentative essays, grades 6–12 (includes ELL status) |
| **Liang et al. 2023 TOEFL** https://huggingface.co/datasets/WxWx/ChatGPT-Detector-Bias | HF, ungated | **MIT** | `TOEFL_real_91`, `TOEFL_gpt4polished_91`, `CollegeEssay_real_70`, `CS224N_real_145` + GPT-3 sets. No official GitHub found |
| **ICNALE** | Official download page/terms **not found** (old sakura.ne.jp URL from 2012). Registration likely required (**UNVERIFIED**) | **UNVERIFIED** | ~1.3M words, 10 Asian regions (incl. learners from Asia; India not confirmed) |

All of these are non-commercial-OK for an academic paper. NC-SA means any derived release must also be NC-SA.

### A5. Local inference: Ollama on RX 7800 XT (Windows 11)

- Ollama docs (https://docs.ollama.com/gpu): **RX 7800 XT is listed for Windows**. Requires "an AMD ROCm v7 / HIP7-capable driver stack" (i.e., current Adrenalin driver with HIP 7). **Vulkan** backend is also available on Windows and enabled by default as a fallback. Check `ollama ps` shows 100% GPU; silent CPU fallback is the common failure.
- Card = gfx1101, 16 GB.
- Default (q4) model sizes from ollama.com (weights only; KV cache needs extra):
  - Fit comfortably: `qwen3:8b` 5.2 GB, `qwen3:14b` 9.3 GB, `gemma3:12b` 8.2 GB, `llama3.1:8b`, `mistral:7b`.
  - Tight but feasible: `gpt-oss:20b` **14 GB** (Apache 2.0), `mistral-small:22b/24b` (size not fetched, **UNVERIFIED** ~13–15 GB).
  - Will spill to RAM (slow): `gemma3:27b` 17 GB, `qwen3:30b` 19 GB, `qwen3:32b` 20 GB.
- Also listed: gemma4 (12b/26b/31b), qwen3.5 (9b/27b). Sizes not checked.

---

## PART B — VENUES

### B1. Agents4Science
- 2025 edition: deadline 15 Sep 2025, decisions 5 Oct 2025, virtual conference 22 Oct 2025. 315 submissions, 48 accepted. https://agents4science.stanford.edu/ , analysis https://arxiv.org/abs/2511.15534 (also Nature Biotechnology https://www.nature.com/articles/s41587-025-02963-8).
- Rules (2025): AI must be **sole first author**; humans may be secondary authors; max 3 submissions per human; 8 pages; OpenReview; AI contribution disclosure checklist; parallel submission elsewhere allowed; free.
- **2026 edition: NOT FOUND.** The site, call and FAQ mention only 2025 (checked 2026-10-12). Contact: agents4science at gmail dot com.
- Spin-off: **AI Agents4Qual 2026** (qualitative research), deadline 31 Jan 2026, past. https://www.aiagents4qual.org/

### B2. Other venues that accept AI-authored papers
- **aiXiv** (preprint server for AI- and human-authored work, AI reviewers) https://arxiv.org/abs/2508.15126. Small: "a few dozen papers" after a Nov 2025 update (Science coverage). Low prestige; useful only as a transparency deposit.
- Most mainstream venues do **not** accept AI as an author. See per-venue policies below.

### B3. ACL-family 2027 (all deadlines AoE)
Dates from the Joint Call for Workshops 2027 (https://www.aclweb.org/portal/content/joint-call-workshops-proposals-2027) and ARR (https://aclrollingreview.org/dates):

| Venue | Dates / location | Relevant deadlines |
|---|---|---|
| EACL 2027 | 9–14 Mar 2027, Athens (hybrid). Theme "The Human in Language" | **SRW:** pre-submission mentorship **6 Nov 2026**; direct submission **15 Dec 2026**; notification 5 Jan 2027 (https://2027.eacl.org/calls/srw/). Workshops: direct submission 15 Dec 2026 |
| COLING 2027 | 9–14 May 2027, Macau | Main ARR deadline was 12 Oct 2026 (today). Workshops: direct submission 5 Jan 2027 |
| NAACL 2027 | 1–5 Jun 2027, San Francisco | Main ARR 12 Oct 2026 (today). Workshops: direct submission 5 Feb 2027. SRW call exists by title only; **dates not found** |
| **ACL 2027** | 17–22 Aug 2027, Kyoto (main 20–22 Aug) | **Main ARR: 4 Jan 2027.** Workshops: direct submission 25 Apr 2027. **Theme track "Homogenization and Knowledge Collapse in LLMs"**, a direct fit (human vs model diversity, homogenization metrics) (https://2027.aclweb.org/calls/main/). ACL 2027 SRW: "coming soon" |
| EMNLP 2027 | ~early Nov 2027, Mexico/Central America (TBA) | none yet |

- **SRW eligibility:** ACL 2026 SRW explicitly welcomed students "including highschool"; the first author must be a current student (https://2026.aclweb.org/calls/student_research_workshop/). EACL 2027 SRW says the first author "MUST be a student (undergraduate or graduate)", with high school not mentioned (**ask the chairs**). Unaffiliated status is not addressed by either.
- **Topic workshops:** GenAI Content Detection (COLING 2025) had no 2026/2027 edition found. In2Writing: last found 2025 (NAACL), none for 2026/27 found. Workshop lists for 2027 appear after 13 Oct 2026, so recheck.
- **ACL AI-writing policy** (ACL 2023 policy, still linked from the ACL 2027 call; https://2023.aclweb.org/blog/ACL-2023-policy/): models cannot be authors. Disclosure in the Responsible NLP checklist is not grounds for desk rejection. But "new ideas + new text" generated by AI is **discouraged**. **This is the main risk for a fully AI-written paper at ACL venues.** Disclose fully; argue the case; or have the student substantially write and edit.

### B4. Preprint servers
- **arXiv endorsement:** from **21 Jan 2026**, an institutional email alone no longer gives automatic endorsement for new authors, in all sections (Math from 10 Dec 2025). https://blog.arxiv.org/arxiv/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics , https://info.arxiv.org/help/endorsement.html . A first-time unaffiliated cs.CL submitter needs a **personal endorser** (an active cs author with papers 3 months – 5 years old). Do not mass-email endorsers.
- **arXiv CS review/position rule** (31 Oct 2025, https://blog.arxiv.org/?p=1740): surveys and position papers need prior peer review. **Research papers are not affected**, so this paper is fine if framed as empirical research.
- **arXiv AI policy:** AI cannot be an author; significant use of text-to-text generative AI must be reported; all authors take full responsibility (https://blog.arxiv.org/2023/01/31/arxiv-announces-new-policy-on-chatgpt-and-similar-tools). **May 2026:** a one-year ban for "incontrovertible evidence" of unchecked AI output (hallucinated references, leftover chatbot text), after which papers must be peer-reviewed first (press: https://www.techspot.com/news/112442-arxiv-moves-combat-ai-slop-submissions-one-year.html ; https://flowingdata.com/2026/05/20/arxiv-will-ban-researchers-for-a-year-if-generative-ai-not-kept-in-check/ ; primary text **UNVERIFIED**).
- **arXiv rate limit (1 Oct 2026):** max **2 submissions per calendar month** per submitter, max 3 active; AI use OK if disclosed. https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
- **OSF Preprints:** "Content completely or mostly generated by large language model (LLM) tools" is **not appropriate**. https://help.osf.io/article/691-preprint-moderation-policies → **EXCLUDED** for a fully AI-written paper.
- **SSRN:** AI policy (updated 3 Aug 2026) requires disclosure; authors fully responsible; Research Integrity screening. Rejections are final with no reasons given. In 2026 SSRN stopped posting *published* CS papers. Course projects and "non-scholarly" items are not accepted. https://www.elsevier.support/ssrn/answer/AI , https://www.elsevier.support/ssrn/answer/get-started . Unaffiliated: affiliation field required. Allowed but screened (**UNVERIFIED** for independent authors).
- **Zenodo:** open upload, gives a DOI immediately, anyone can use it. ML spam classifier plus human moderation. Excludes "raw AI outputs as primary research artefacts" and fabricated findings; has a Generative-AI policy for depositors. https://support.zenodo.org/help/en-gb/2/141 . Zenodo says Google Scholar does **not** index it (https://support.zenodo.org/help/en-gb/29-indexing/61-is-zenodo-indexed-by-google-scholar). → Use it for **data/code DOI**, not as the main paper venue.

### B5. Journals

| Journal | AI policy | APC / waiver (India) | Unaffiliated OK? | Fit |
|---|---|---|---|---|
| **PLOS ONE** | AI cannot be an author. Disclose tools, use and validation in Methods/Acknowledgements. Authors must ensure "hypotheses, interpretations, and conclusions are their own" (https://journals.plos.org/plosone/s/ethical-publishing-practice) | APC amount **UNVERIFIED** (page 403). Research4Life waivers do not apply because countries with GNI > US$1T are ineligible (https://research4life.org/access/criteria; India's GNI > $1T is my inference). **PLOS Publication Fee Assistance**: case-by-case, apply at submission, show other funding sought (https://theplosblog.plos.org/?p=22703) | Generally yes (**UNVERIFIED**) | Soundness-only review, the best fit for "no novelty bar" |
| **Royal Society Open Science** | Disclose; no AI authorship; AI must not replace insight/analysis/conclusions (third-party summary, **UNVERIFIED**) | APC **£1,400 / $1,960** (https://royalsociety.org/journals/open-access/). **India NOT on the Open Access Equity waiver list** (https://royalsociety.org/journals/open-access/open-access-equity/); discretionary waiver possible | **UNVERIFIED** | Soundness-based, good fit |
| **Humanities & Social Sciences Communications** (Springer Nature) | LLMs not authors; document in Methods (https://www.springer.com/us/editorial-policies/artificial-intelligence--ai-/25428500) | APC: DOAJ says up to $1,990, aggregator $1,490 (**UNVERIFIED**). Waiver policy exists; India eligibility **UNVERIFIED** (likely discretionary only) | **UNVERIFIED** | Good topical fit (language and society) |
| **PeerJ Computer Science** | **UNVERIFIED** | Conflicting: $1,395 (DOAJ) / $1,888 / $2,155 (PeerJ pages). Waiver policy exists per DOAJ (https://www.doaj.org/toc/2376-5992) | **UNVERIFIED** | OK fit, costly |
| **Journal of Quantitative Linguistics** (T&F) | Disclose tool, version, how and why, in Methods/Acknowledgements; AI not an author | Hybrid: **free** on the subscription route (APC only if you choose OA). https://www.tandfonline.com/journals/njql20/about-this-journal | **UNVERIFIED** | Strong topical fit, $0 |
| **Corpus Linguistics and Linguistic Theory** (De Gruyter) | De Gruyter Brill **does not accept papers "generated by" AI** (https://degruyterbrill.com/en/ai-for-authors) | Gold OA from 2025 with no author charges | — | **EXCLUDED** for an AI-written paper |
| **Digital Scholarship in the Humanities** (OUP) | OUP policy not fetched (**UNVERIFIED**) | Hybrid: free on the subscription route; OA fee **UNVERIFIED** | **UNVERIFIED** | Fit for stylometry |

**Student journals**

| Journal | Fees | AI policy | Notes / reputation |
|---|---|---|---|
| **Journal of Emerging Investigators (JEI)** | $49 submission fee per JEI pay page (older pages say $35); **waiver available** (https://emerginginvestigators.org/submissions/pay-and-submit/pay) | **UNVERIFIED** (author PDF unreadable) | Grades 6–12, before university enrolment. **A senior mentor must be last author and must submit for the student.** Real scientist peer review, the most reputable. Rolling, up to ~12 months |
| **NHSJS** | Free (https://nhsjs.com/about/) | **"AI may not draft, paraphrase, expand, or rewrite your prose"** (https://nhsjs.com/ai-usage-policy/) | **EXCLUDED** for an AI-written paper |
| **Curieux** | Conflicting: free vs $200 (third-party only) | **UNVERIFIED** | Student-run; **UNVERIFIED** |
| **Columbia Junior Science Journal** | No publication fee (third-party) | **UNVERIFIED** | Grades 9–12; window ~Jul–30 Sep (third-party), so the **2026 cycle is likely closed**. Short 2–3 page format |
| **Journal of Student Research (JSR)** | Pay-to-publish: $50 pre-review plus a post-review fee ($99–$299, conflicting reports) | **UNVERIFIED** | Mixed reputation (admissions-consultancy commentary). Site down (522) when checked |

### B6. Profile boosters
- **IRIS National Fair 2026** (route to Team India at **Regeneron ISEF 2027**, 8–14 May 2027, Los Angeles): registration ran **1 Aug – 3 Oct 2026, now closed**. Classes 5–12. https://register.irisnationalfair.org/ , https://irisnationalfair.org/ . The next cycle (for ISEF 2028) likely opens around Aug 2027 (**UNVERIFIED**).
- **John Locke Institute Essay Competition:** 2026 had a **Law** category; under-19 for Senior; 2,000 words. The 2027 dates are **not announced** (third-party: likely Feb registration, late-spring deadline, **UNVERIFIED**). It is an essay, not this paper, but it is the most relevant credential for law school.
- **Immerse Education:** a paid commercial programme; not a credential. Skip.
- **ORCID:** free, no affiliation needed. Register now and use it on every submission.
- **Google Scholar profile:** anyone can create one, but a profile appears in search **only with a verified institutional email** (gmail is not accepted) (https://scholar.google.co.in/intl/en/scholar/citations.html). An unaffiliated student profile likely won't be publicly searchable.
- **Hugging Face dataset release:** free; derived data must respect source licences (NC-SA for ELLIPSE/PERSUADE; Open Parliament Licence attribution for Hansard).
- **Zenodo DOI** for code and data: free, immediate.

---

## Recommended plan

**Data:** Kaggle arXiv snapshot (CC0) → cs.CL + non-CS abstracts 2018–2026; UK Hansard via TWFY rsync (verify 2025 files) + Australian Hansard parquet (CC BY, to Jul 2025); RAID abstracts (MIT, GPT-4/ChatGPT) + DetectRL abstracts (Claude-instant) as the LLM reference, plus locally generated text from qwen3:14b / gemma3:12b / gpt-oss:20b; ELLIPSE + Liang TOEFL for the non-native check.

**Venue ladder (best realistic first):**
1. **ACL 2027 SRW** (call pending; 2026 edition welcomed high-schoolers), or **EACL 2027 SRW** (mentorship 6 Nov 2026, submit 15 Dec 2026; confirm high-school eligibility with the chairs). Fully disclose AI authorship; ACL "discourages" AI-generated ideas and text.
2. **ACL 2027 main, theme track "Homogenization"** (ARR 4 Jan 2027): a stretch goal.
3. **arXiv cs.CL preprint**: needs a personal endorser; research paper, not position paper; meticulous reference checking (one-year ban risk).
4. **Journal of Quantitative Linguistics** ($0 subscription route) or **PLOS ONE** (with Fee Assistance) / **RSOS** (discretionary waiver).
5. **JEI** (needs a mentor; AI policy unverified).
6. **Agents4Science**: only if a 2026/27 edition is announced (none found).

**Excluded:** OSF Preprints, NHSJS, CLLT/De Gruyter (all bar mostly AI-generated text); JSR (pay-to-publish).
