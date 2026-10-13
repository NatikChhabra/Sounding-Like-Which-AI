# Pre-release audit, round 2: ethics, policy and licences

Audited 2026-10-13 against commit `5f285c4` (origin/main, public). Files read: `paper/main.tex` (Data, Limitations,
Ethics Statement, AI Use and Authorship, Appendix A), `paper/AI_DISCLOSURE.md`, `README.md`, `data/README.md`,
`CITATION.cff`, `LICENSE`, `requirements.txt`, `PLAN.md`, every file in `data/` (decompressed and inspected), the
`results/` listing, and the git history. Policies were checked on the web on the same day (URLs inline). No file
other than this report was edited.

Severity: **Blocking** = would cause desk rejection, a policy violation, or a false statement in a permanent (DOI)
record. **Important** = should be fixed before the Zenodo release or the submission. **Minor** = polish.

---

## Blocking

### B1. The sole human author does not yet meet ACL's authorship criteria, and the paper says so
- The ACL Policy on Publication Ethics (last edited 17 Aug 2026) requires every author to meet four criteria,
  including "Drafting the work or revising it critically for important intellectual content" and "Final approval
  of the version to be published", and says "Authors are responsible for all content submitted". For AI-generated
  text about existing ideas it requires authors to show the text "was checked to be accurate".
  https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics
- The ARR CFP repeats that "all authors remain fully responsible for correctness". https://aclrollingreview.org/cfp
- The paper states: "drafted all text; no human has edited the text" and that the author "will read the final
  paper before release". `git log` confirms **zero `HUMAN-EDIT:` commits** (47 commits; 46 with
  `Co-Authored-By: Claude Opus 5.5`, plus `6675865` "Strip BOM", which is disclosed). A chair reading this section
  can conclude that the only listed author has not drafted, revised or approved the paper. The work also falls under
  ACL category (f) "new ideas + new text" (the AI proposed the research question, hypotheses and term). That is not
  banned, but the policy's point is that the model cannot be an author, so a human must meet the criteria.
- **Fix (before any ACL/SRW submission, including the 6 Nov mentorship draft):**
  1. The author reads the whole paper and revises it critically. Substantive changes go in as `HUMAN-EDIT:` commits,
     for example rewording claims, cutting or adding caveats, or checking numbers against `results/`.
  2. Replace "no human has edited the text" with an accurate statement, e.g. *"The human author read the full paper,
     revised it (commits labelled HUMAN-EDIT), checked every reference (see B2) and approved this version."* Write
     this only once it is true.
  3. Make the same change in `paper/AI_DISCLOSURE.md` ("What the human author did"), then rebuild with
     `paper/build.ps1`.

### B2. "Citations were not checked by a human" will get the paper desk-rejected at ACL and invites an arXiv ban
- ACL 2026 desk-rejected more than 100 accepted papers that cited non-existent work. Its statement says LLM use
  "does not remove the author's obligation to manually confirm the existence and relevance of every cited source",
  and says LLMs "do not replace the necessity for rigorous human oversight". https://2026.aclweb.org/acl_statement/
- The ARR CFP lists "hallucitations" among the grounds for desk rejection. https://aclrollingreview.org/cfp
- arXiv (May 2026, CS section): authors take "full responsibility for all its contents, irrespective of how the
  contents were generated". Incontrovertible evidence of unchecked LLM output (hallucinated references are the main
  example) brings a one-year ban, after which the author's next submission must first pass peer review.
  https://info.arxiv.org/help/moderation/index.html ;
  https://www.timeshighereducation.com/news/ban-authors-submitting-ai-content-welcome-unenforceable
- The paper and `AI_DISCLOSURE.md` state outright that no human checked the citations. At a venue that requires
  manual confirmation, that sentence admits non-compliance, even if every reference is in fact correct (the
  two-pass AI verification in `lit/verification/v5_*.md` is good evidence that they are).
- **Fix:** before any submission or arXiv post, the author personally opens every one of the roughly 70 references
  (DOI or arXiv page) and confirms that it exists and supports the citing sentence. Record this as a `HUMAN-EDIT:`
  commit adding `lit/HUMAN_CITATION_CHECK.md` (key, date, "exists / supports: yes/no"). Then change the sentence to
  *"Citations were verified by separate AI sessions and then checked by the human author against each source."* If
  the author will not do this, do not submit to ACL venues or post to arXiv.

### B3. Release status contradicts the human-read statement, and a Zenodo DOI would make it permanent
- The paper says the author "will read the final paper before release". But the repository is already public,
  `README.md` says "**Status:** release v1.0", and `CITATION.cff` has `date-released: 2026-10-13`. There is no git
  tag or GitHub release yet, and `PLAN.md` correctly lists the read-through and v1.0 as still to do. Read today, the
  README makes the paper's statement look false.
- Zenodo versions cannot simply be deleted or edited once minted. Under the Terms of Use, the uploader is
  "exclusively responsible for the content that they upload". https://about.zenodo.org/terms/
- **Fix now:**
  - In `README.md`, change the status to *"Status: pre-release draft (not yet read or approved by the author; not
    peer reviewed). v1.0 will be tagged after the author's read-through."*
  - Remove `date-released` from `CITATION.cff`, or set it on the day of the tag.
- **At release:** finish B1 and B2 first. Then put the sentence in the past tense (*"The human author read and
  approved this version on <date>"*) in `main.tex` and `AI_DISCLOSURE.md` (HUMAN-EDIT commit), rebuild, and only
  then create the GitHub release that triggers Zenodo.

### B4. EACL 2027 SRW eligibility of a pre-university first author is not confirmed
- The 2027 SRW CFP says that for research papers "the first author MUST be a student (undergraduate or graduate)".
  It does not mention high-school students, and there is no 2027 FAQ (it returns 404).
  https://2027.eacl.org/calls/srw/
- The 2026 FAQ explicitly allowed high-school students and required first authors to be "current students at the
  time of submission". https://2026.eacl.org/calls/srw/faq/
- The preprint gives the affiliation as "Independent researcher, Bilaspur, India", which does not show student
  status.
- **Fix:** before the 6 Nov 2026 mentorship deadline, email the EACL 2027 SRW chairs. Ask whether a full-time
  pre-university (school) student may be first author, and mention the disclosed AI-conducted nature of the work so
  that any objection comes up now. Keep the written answer. If eligible, list a student affiliation in OpenReview
  and on the camera-ready (e.g. the school, or "Independent researcher; secondary-school student").

---

## Important

### I1. The Hansard licence is misstated; the upstream text is CC BY-NC-ND, not CC BY
- The Katz and Alexander Zenodo record 17351233 (v8) is CC BY 4.0. https://zenodo.org/records/17351233
- The text it parses comes from aph.gov.au, whose site-wide licence is CC BY-NC-ND 4.0 ("with the exception of the
  Commonwealth Coat of Arms and where otherwise noted"). https://www.aph.gov.au/Help/Disclaimer_Privacy_Copyright
  (fetch returned 403 here; the wording was confirmed through search snippets of the same page). Older documents
  carry CC BY-NC-ND 3.0 AU.
- The release contains **1,202 LLM revisions (P2) of real Hansard speeches** in `llm_hansard.jsonl.gz`, which are
  arguably adaptations (NoDerivatives). It also contains verbatim opening sentences in `hansard_split.csv.gz`. Both
  are labelled CC BY 4.0 (commercial reuse allowed) or carry no licence at all.
- **Fix (before Zenodo):**
  - In `README.md`, `data/README.md` and the Ethics Statement, write "Australian Hansard (Parliament of Australia,
    CC BY-NC-ND 4.0), via the database of Katz and Alexander (CC BY 4.0)".
  - Relicense `llm_hansard.jsonl.gz` as CC BY-NC 4.0, and either (a) drop the P2 rows from the released file (keep
    their `src_id`s so they can be regenerated), or (b) keep them and state that they are revisions of
    Parliament-licensed text and are released for non-commercial research only. Option (a) is safer under ND.
  - Mark `hansard_split.csv.gz` as "opening sentences © Parliament of Australia, CC BY-NC-ND 4.0, reproduced
    unmodified except truncated", plus attribution. CC BY also requires indicating changes (sampling, truncation),
    so add that line for the Katz database.

### I2. Licence metadata says MIT for everything, and `samples/` has no licence
- `CITATION.cff` has `license: MIT`, and `LICENSE` is MIT. GitHub's sidebar and the Zenodo record built from the
  release will show MIT for the whole archive, including the CC BY-NC-SA essay generations. When a `.zenodo.json`
  exists, Zenodo uses it and ignores `CITATION.cff`. https://help.zenodo.org/docs/github/describe-software/citation-file/ ;
  https://help.zenodo.org/docs/github/describe-software/zenodo-json
- `data/README.md` gives licences for `generated/` only. The `samples/` files mix CC0 (arXiv ids and titles),
  PERSUADE-derived labels (`essay_split.csv.gz`: essay id plus ELL status, derived from a CC BY-NC-SA 4.0 corpus,
  https://github.com/scrosseye/persuade_corpus_2.0) and Hansard text (I1).
- **Fix:**
  - In `CITATION.cff`, set `license: [MIT, CC-BY-4.0, CC-BY-NC-SA-4.0]` (CFF 1.2.0 accepts a list of SPDX ids).
  - Add `.zenodo.json` with a description that lists the per-part licences. As the record licence, use
    `cc-by-4.0` with the exceptions spelled out in the description and notes, or `other-open` if Zenodo's vocabulary
    accepts it. Check this on a draft before publishing.
  - Add a licence column to the `samples/` table in `data/README.md`:
    - arXiv files: CC0
    - `essay_split`: CC BY-NC-SA 4.0
    - `hansard_split`: see I1
  - Add a catch-all line to the README Licences section: "Paper text, figures, results, review reports, literature
    notes and the analysis plan: CC BY 4.0".

### I3. The disclosure overstates human approvals
- `AI_DISCLOSURE.md` says the author "Approved the analysis plan, its deviations, every download and every public
  action". The paper says the author "approved the analysis plan and its deviations in the working conversation".
  The project memory records otherwise:
  - The author told the AI on 2026-10-12 to "stop asking permission for setup/downloads". That is a standing
    permission, not approval of each download.
  - Several deviations were made while the author was asleep (the 03:00–04:00 vintage reframing, the cleaning fix
    and the full re-run). They were accepted afterwards at best.
- None of this can be checked from the repository, since the approvals are not in git.
- **Fix:**
  - In `AI_DISCLOSURE.md`, write: *"Approved the analysis plan; gave standing permission for downloads and setup;
    was informed of deviations, several of which the AI system made while working unattended under an instruction
    to continue; approved making the repository public."* Keep only the clauses the author confirms.
  - In the paper, write: *"approved the analysis plan in the working conversation; deviations (Appendix A) were
    made by the AI system and reported to the author."*

### I4. ACL 2027 through ARR: the October 2026 reviewing policy can desk-reject this paper without review
- From the October 2026 cycle, a submission is guaranteed reviewers only if it names a qualified "service
  contributor". This is usually an author who is a qualified reviewer, or a non-author who vouches for the work.
  Papers without one go into a lottery, and those not drawn are desk-rejected.
  https://aclrollingreview.org/cfp ;
  https://www.aclweb.org/portal/sites/default/files/ACL%20sustainable%20reviewing%20policy_2026.pdf
- From October 2026, every author also needs a complete OpenReview profile (ORCID, accurate affiliation history,
  email, conflicts) within one week of the deadline, or the paper is desk-rejected.
- A pre-university author with no publications is not a qualified reviewer.
- **Fix:** before the 4 Jan 2027 deadline, find a non-author qualified contributor willing to vouch for the paper
  (the SRW mentor is the natural candidate), or accept the lottery risk. Also complete the OpenReview profile now,
  with the school in the affiliation history (see B4).

### I5. Responsible NLP checklist gaps
An "incorrect or misleading" checklist, or one that systematically lacks justifications, is grounds for desk
rejection (https://aclrollingreview.org/responsibleNLPresearch/ , https://aclrollingreview.org/cfp). The paper
currently has nothing to cite for:
- **B4 (personal information).** Hansard data name members of parliament: speaker ids such as `Owens1958`, party
  labels and opening sentences. PERSUADE essays are masked (`Generic_Name`, `Generic_School`, …). That masking
  survives in the released LLM revisions: 227 masking tokens and no e-mail addresses were found in
  `llm_essay.jsonl.gz`. Add to the Ethics Statement: *"Hansard speakers are members of parliament speaking in
  public office; we release only speech ids, speaker ids, party and opening sentences, which are already public.
  PERSUADE essays are de-identified by their creators, and released LLM revisions keep that masking; we release no
  essay texts."*
- **B2 and B3 (licences and intended use of models).** No model licences are stated. Add an appendix table
  (licences in M1) and one sentence saying that research use is consistent with each licence and acceptable-use
  policy.
- **C1 (compute).** No hardware or compute budget is reported (one desktop with an AMD RX 7800 XT through Ollama;
  give GPU-hours or an estimate). Add one sentence to Section 4 or an appendix.
- **A2 (risks).** The Ethics Statement already warns against judging individual writers. Add misuse of \mso{} as a
  detector and the energy cost of local generation (small).
- **E1.** Answer "Yes" and point to the AI disclosure section (see I6).

### I6. ARR wants the AI-use details in the Acknowledgements section
- The ACL policy says use "should be fully disclosed in the Acknowledgements section". The ARR CFP says use must be
  disclosed in the checklist "with details in the Acknowledgements section".
- The paper uses its own unnumbered section, "AI Use and Authorship". Its content is good; only the heading
  differs, but a literal-minded chair could object.
- **Fix:** rename the heading to `\section*{Acknowledgements: AI Use and Authorship}` and keep it in the anonymous
  review version, which is allowed because it contains no identifying information.

---

## Minor

- **M1. Model licences do not restrict publishing outputs, but downstream users should be told about the
  "no training" clauses.**
  - **Llama 2 and Vicuna v1.5** (Llama 2 Community License): §1.b.v forbids using the materials "or any output or
    results" to improve any other LLM. https://ai.meta.com/llama/license/
  - **Llama 3.1**: "Built with Llama" is required only when you "distribute or make available the Llama Materials",
    which means the weights and documentation, not outputs. Outputs used to train a *distributed* AI model require
    "Llama" at the start of that model's name. No model is distributed here, since the style classifier is not
    released. https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/blob/main/LICENSE
  - **Gemma 3** (Gemma Terms of Use): Google claims no rights in outputs, but models distilled from outputs count as
    "Model Derivatives".
  - **Gemma 4**: Apache 2.0. Initial release 31 Mar 2026; 12B released 3 Jun 2026.
    https://ai.google.dev/gemma/docs/releases
  - **Apache 2.0 or MIT**: Qwen3 and Qwen3.5, Mistral 7B, Granite 3.3 and 4.2, gpt-oss (plus its usage policy) and
    Phi-4 (MIT). No output restrictions.
  - **Claude**: Anthropic assigns its rights in outputs to the user
    (https://www.anthropic.com/legal/consumer-terms, §4). The Consumer Terms also require users to be at least 18;
    make sure the account used for the 2026-model generations meets the terms that apply to it.
  - **Fix:** add to `data/README.md`: *"Rows are outputs of models under their own licences (Llama 2 and Vicuna:
    Llama 2 Community License; Llama 3.1: Llama 3.1 Community License; Gemma 3: Gemma Terms of Use; others: Apache
    2.0 or MIT; Claude: Anthropic terms). Some of these restrict using outputs to train other models; check them
    before doing so."*
- **M2. Column documentation in `data/README.md` is wrong.**
  - `hansard_split.csv.gz` columns are `id,date,group,grp,pool,title`, where `group` is the party (402 rows empty)
    and `grp` is the speaker id. The party column is not documented.
  - `arxiv_split.csv.gz` columns are `id,date,group,grp,pool,title`, where `group` is the field.
  - Document the actual column names.
- **M3. The Ethics Statement says "we release only scores, not texts" for the Liang essays.** Only aggregate group
  rates are released (`results/essay_liang*.csv`). Say "only aggregate results".
- **M4. "The git history is the complete record" (README, AI_DISCLOSURE).** It records every file change, but not the
  author's instructions or approvals, which stayed in the conversation. Say "the complete record of changes to the
  files".
- **M5. arXiv wording.** arXiv's licence page says CC0 "will apply to all metadata" without naming abstracts or
  titles (https://info.arxiv.org/help/license/index.html). Write "arXiv metadata, including titles and abstracts, as
  distributed under CC0". The P2 abstract revisions in `llm_arxiv*.jsonl.gz` are then fine.
- **M6. arXiv logistics.** A first-time, unaffiliated cs.CL submitter needs a personal endorser
  (https://info.arxiv.org/help/endorsement.html). The AI disclosure satisfies arXiv's tool-reporting rule only after
  B1 and B2 are done.
- **M7. Author personal data.**
  - The preprint gives name, ORCID and city, with no e-mail. Commits use the GitHub noreply address.
  - The anonymous `main.pdf` contains no name, ORCID, GitHub URL or PDF author metadata (checked with pdftotext and
    a byte search).
  - The Windows username "<user>" remains in history (`cde9132`, `code/queues/run_v4.ps1`) and in the tracked
    `paper/reviews/prerelease_repo.md:211`. This is harmless but can be removed from the review file if unwanted.
  - Listing a school affiliation (B4) is the author's choice.
- **M8. Gemma 4 date.** The paper says "Gemma 4 … released in June 2026". The family was released on 31 Mar 2026
  and the 12B on 3 Jun 2026. Write "Gemma 4 12B (released June 2026)" in the text, as the table already does.

---

## Verified as accurate
- Zero `HUMAN-EDIT:` commits. 46 of 47 commits carry "(AI-written)" and the Claude trailer. The disclosed exception,
  `6675865`, did only what the disclosure says: it removed BOMs from `code/analysis.py` and one JSON file and
  regenerated `numbers.tex`.
- `preregistration.md` was first committed in `ef4fa21` (2026-10-12 07:53), before the first results commit (`cff4c35`
  09:08, `f7b53b9` 10:48).
- No AI system is listed as an author in the paper, the preprint or `CITATION.cff`, which complies with ACL and
  arXiv rules.
- The anonymous review version hides the commit hash and repository link, as ARR requires for linked material.
  Public preprints are allowed at any time unless the "no preprint" option is chosen.
- No third-party human texts are redistributed in full: the release contains ids, titles and Hansard opening
  sentences only. Liang et al. TOEFL and 8th-grade texts are not redistributed. The PERSUADE licence (CC BY-NC-SA
  4.0) is stated correctly, and the share-alike label on `llm_essay.jsonl.gz` is correct.
- The disclosure correctly states that the 2026 model is the drafting system and that simulated reviews come from
  the same model family.
