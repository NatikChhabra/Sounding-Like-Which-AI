# Literature survey 01: LLM influence on human writing, homogenization, stylometry, overlap

Compiled 2026-10-12 through web search (arXiv, ACL Anthology, PMLR, ICLR proceedings, journal pages). Each entry lists title, authors, year, venue and URL as found in the source. Numbers come only from the abstract or full text I read, or from search-result summaries of the abstract. Anything I could not confirm against a primary source is marked **UNVERIFIED**.

Research question being tested: *How much does human-written text occupy the same measurable style region as LLM text, including before ChatGPT (a pre-2022 baseline), and did human writing move further into that region after Nov 2022 than its pre-2022 trend predicts?*

---

## 1. Population-level studies of LLM influence on human writing (prevalence)

**1.1 Kobak, González-Márquez, Horvát, Lause (2025). "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." *Science Advances* 11(27): eadt3813.** DOI: https://doi.org/10.1126/sciadv.adt3813 ; arXiv: https://arxiv.org/abs/2406.07016
- Method: tracked word frequencies in more than 15M PubMed abstracts (2010–2024). The expected 2024 frequency is a counterfactual extrapolated from 2021–2022 (q = p₋₂ + 2·max{p₋₂ − p₋₃, 0}), with 2023 excluded. Excess = observed − expected.
- Findings: at least 13.5% of 2024 abstracts were LLM-processed, up to about 40% in some subcorpora. There were 454 excess words in 2024 (343 lemmas), almost all of them *style* words. Earlier excess events (Ebola, Zika, COVID: up to 190 words in 2021) involved content words.
- Relation to our claim: this is the canonical "post-2022 vs pre-trend" design, so the trend-break half of our question is **already done for word frequencies**. Kobak et al. treat the pre-period only as a counterfactual. They never ask how LLM-like the pre-2022 text already was. Because the baseline is extrapolated from 2021–2022, any earlier drift toward LLM style is absorbed into it rather than measured.

**1.2 Holzwarth, González-Márquez, Kobak (2026). "Most biomedical publications show signs of LLM-assisted writing." arXiv preprint.** https://arxiv.org/abs/2608.10715
- Method: a new word-frequency prevalence method applied to *full texts* in PubMed Central. According to a search summary, the method extrapolates a linear 2018–2022 trend (**UNVERIFIED** detail).
- Findings: 89% of 2025 papers show excess LLM-associated vocabulary. The rate is 68% in Discussion paragraphs versus 32% in Methods, and Methods sections overall exceed 50%.
- Relation: the most recent and largest prevalence estimate. Its framing is still prevalence. If "LLM-like" vocabulary is near-saturating, how much of the "excess" is attributable to authorship and how much to imitation becomes a sharper question, which supports our motivation.

**1.3 Liang, Zhang, Wu, Lepp, …, Manning, Zou (2024). "Mapping the Increasing Use of LLMs in Scientific Papers." COLM 2024.** https://arxiv.org/abs/2404.01268 . Journal version: Liang et al. (2025) "Quantifying large language model usage in scientific papers," *Nature Human Behaviour* (PDF: https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf).
- Method: the "distributional GPT quantification" framework fits a mixture of a human word distribution (pre-ChatGPT papers, fit on 2020) and an LLM word distribution (GPT-3.5 expansions of outlines) to estimate the corpus fraction α. COLM version: 950,965 papers, Jan 2020–Feb 2024. NHB version: 1,121,912 papers through Sep 2024.
- Findings: CS reaches up to 17.5% (COLM) and 22% (NHB); Math and Nature portfolio reach up to 6.3% (COLM) and 9% (NHB). **Key for us:** pre-ChatGPT α (Nov 2022) was **not zero**: 2.3% for CS, 2.9% for EESS, 2.4% for Math, and 3.1% for Nature. The authors call these a "pre-ChatGPT reference point" consistent with the method's false-positive rate.
- Relation: this is the closest existing number to a "pre-2022 overlap." Liang et al. treat it as **estimator noise to be ignored**, not as a substantive quantity. Our paper can reinterpret and decompose that baseline (genre, field, author, trend), which is a concrete hook for the novelty claim.

**1.4 Liang, Izzo, Zhang, Lepp, Cao, Zhao, Chen, Ye, Liu, Huang, McFarland, Zou (2024). "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews." ICML 2024 (oral), PMLR 235: 29575–29620.** https://proceedings.mlr.press/v235/liang24b.html ; https://arxiv.org/abs/2403.07183
- Method: the same corpus-level mixture estimator, using expert-written and AI-generated reference texts. Applied to reviews from ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023.
- Findings: 6.5–16.9% of review text may have been substantially LLM-modified. Usage was higher for low-confidence reviews, reviews submitted near the deadline, and reviewers less likely to respond to rebuttals.
- Relation: pure prevalence. It introduces the estimator that our overlap metric must be distinguished from. Its validation on pre-ChatGPT reviews gives another implicit "baseline overlap."

**1.5 Liang, Zhang, Codreanu, Wang, Cao, Zou (2025). "The Widespread Adoption of Large Language Model-Assisted Writing Across Society." *Patterns* (Oct 2025).** https://arxiv.org/abs/2502.09747 ; PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12745980/
- Data: Jan 2022–Sep 2024. 687,241 CFPB consumer complaints, 537,413 corporate press releases, 304.3M job postings, and 15,919 UN press releases.
- Findings (late 2024): about 18% of financial-complaint text, up to 24% of corporate press releases, just under 10% of job postings at small firms, and about 14% of UN press releases. Use surged after ChatGPT and plateaued in 2024. The supplement validates the estimator on pre-ChatGPT blends, with about 2–3 percentage points of error (from a search summary; **UNVERIFIED** exact figure).
- Relation: shows the prevalence framing generalizes across society. Its corpora start in 2022, so it offers **no long pre-2022 trend** and no pre-ChatGPT overlap analysis.

**1.6 Geng & Trotta (2024). "Is ChatGPT Transforming Academics' Writing Style?" arXiv:2404.08627** (an ICML 2024 listing exists at https://icml.cc/virtual/2024/37569; the venue type, probably a workshop, is **UNVERIFIED**). https://arxiv.org/abs/2404.08627
- Method: word-frequency mixture over about 1M arXiv abstracts (May 2018–Jan 2024), calibrated on real abstracts mixed with ChatGPT-revised abstracts.
- Findings: about 35% of CS abstracts look ChatGPT-revised, using the "revise the following sentences" prompt as the reference. The baseline is a **flat pre-ChatGPT average**: the authors "assume that the frequencies of these words should remain stable without LLM," so pre-2022 trends are not extrapolated.
- Relation: the closest prevalence study on our exact corpus (arXiv abstracts). The flat-baseline assumption is a weakness that our trend-adjusted design directly addresses. The authors note that LLM-like wording does not prove direct LLM use, a caveat our paper builds on.

**1.7 Geng & Trotta (2025). "Human-LLM Coevolution: Evidence from Academic Writing." Findings of ACL 2025, pp. 12689–12696.** https://arxiv.org/abs/2502.09606 ; https://aclanthology.org/2025.findings-acl.657/
- Findings: in arXiv abstracts, "delve" and other publicized ChatGPT-overused words dropped sharply after early 2024, while "significant" kept rising.
- Relation: the "LLM style region" is a moving target, because humans and editors react to known markers. A style region defined by marker words is unstable over time, which argues for multi-feature (stylometric or register) definitions. This both threatens and motivates our design.

**1.8 Gray (2024). "ChatGPT 'contamination': estimating the prevalence of LLMs in the scholarly literature." arXiv:2403.16887.** https://arxiv.org/abs/2403.16887
- Method: disproportionate jumps in marker words ("meticulously", "intricate", "commendable") in the Dimensions database.
- Findings: at least about 60,000 papers (slightly over 1%) in 2023 were LLM-assisted. A follow-up (arXiv:2512.01560, Dec 2025) estimates more than 10% of 2024 papers.
- Relation: prevalence via marker words. No overlap framing.

**1.9 Lin & Zhu (2025). "Divergent LLM Adoption and Heterogeneous Convergence Paths in Research Writing." arXiv:2504.13629** (working paper, not peer reviewed as far as I found). https://arxiv.org/abs/2504.13629
- Method: 627,384 arXiv papers (Jan 2021–Dec 2023). Fine-tuned classifiers detect ChatGPT-revised style, and a difference-in-differences analysis measures convergence.
- Findings: LLMs drive convergence in writing. Early adopters, male, non-native and junior researchers shift most toward the style of established researchers. **Key for us:** the classifier's nonzero pre-Nov-2022 "adoption" rate is called misclassification and **subtracted as a baseline**. The test confusion matrix implies about 7.75% of unrevised human abstracts are labeled as revised.
- Relation: a second paper that sees pre-ChatGPT human text landing in the "AI" region and **discards it as noise**. That is exactly the quantity our paper treats as the object of study.

**1.10 Bentley, Vidiella, Ruck, Dutta, Li, Valverde (2026). "Human–LLM Collaboration Is Transforming Complexity Metrics in Scientific Texts." arXiv:2606.27052.** https://arxiv.org/abs/2606.27052
- Method: millions of arXiv abstracts from 2010–2025. A composite "LLM-associated style index" is built from z-scored dash markers plus the words "significant", "crucial" and "showcase". A regression includes year × post-2023 interaction terms, alongside Zipf and Heaps exponents and top-word turnover.
- Findings: the style index rises sharply after early 2023. The authors note it "was increasing through time" before that. Zipf and Heaps changes are subtle, while top-rank turnover jumps from 2023.
- Relation: **the closest prior work on our exact corpus and design** (an arXiv style index with a pre-trend, plus a post-2023 break). It is still a 4-marker index, does not quantify how much pre-2023 human text already sits in an LLM style region, and does not check whether its markers were already common in human writing. That gap remains ours, but this paper must be cited and differentiated.

**1.11 Lee (2026). "An LLM-Associated Register Shift in Korean Journal Abstracts: A Morphology-Aware Excess-Vocabulary Study, 2018–2026." arXiv:2609.07447** (single-author working paper). https://arxiv.org/abs/2609.07447
- Method: Kobak-style excess against the pre-2023 trend, applied to 398,296 Korean KCI abstracts, with placebo floors computed on pre-LLM years.
- Findings: no excess in 2023, onset in late 2024. Estimated LLM-processed share in 2026 is at least 16.1% (single-word statistic) or 33.0% (set statistic). Placebo floors are 0.1–2.2 points. *Sisahada* ("suggest") appears in 21.4% of abstracts versus 5.3% expected.
- Relation: methodological template for **placebo tests on pre-LLM years**, which our trend-break test should copy. It frames the change as a "register shift," close to our "style region" language.

**1.12 Alani & Jansen (2026). "Are Scientists Starting to Sound like ChatGPT? Stylistic Diffusion in Biomedical Abstracts in the LLM Era." MDPI *Machine Learning and Knowledge Extraction* 8(8): 223** (journal, volume and article number inferred from the PDF filename "make-08-00223"; **UNVERIFIED**). PDF: https://www.bernardjjansen.com/uploads/2/4/1/8/24188166/make-08-00223.pdf ; https://www.mdpi.com/2504-4990/8/8/223
- Method: 28,415 PubMed abstracts (2018–2025), a strict LLM-marker dictionary plus a control vocabulary, and interrupted time-series models.
- Findings: marker use rose from 4.995 to 11.658 per 1,000 words (+133.4%), while control vocabulary declined slightly. The change was strongest in 2024–2025.
- Relation: the title asks almost our question ("sound like ChatGPT"), but the paper measures marker *diffusion*, not distributional overlap or the pre-2022 overlap level. It is a direct competitor on framing and must be cited.

**1.13 Brooks, Eggert, Peskoff (2024). "The Rise of AI-Generated Content in Wikipedia." Proc. 1st Workshop on Advancing NLP for Wikipedia (WikiNLP 2024), pp. 67–79.** https://aclanthology.org/2024.wikinlp-1.12/ ; https://arxiv.org/abs/2410.08044
- Method: GPTZero and Binoculars, with thresholds **calibrated to a 1% false-positive rate on pre-GPT-3.5 articles**.
- Findings: more than 5% of new English Wikipedia articles were flagged. Flagged articles tended to be lower quality, self-promotional or partisan.
- Relation: once again, pre-ChatGPT human text that scores as AI is used only to set the threshold.

**1.14 Russell, …, Iyyer (2026). "AI use in American newspapers is widespread, uneven, and rarely disclosed." ACL 2026 (long), 2026.acl-long.663.** https://aclanthology.org/2026.acl-long.663/ ; https://arxiv.org/abs/2510.18774
- Findings: 186K articles from 1.5K US newspapers (summer 2025). The Pangram detector flags about 9% as partly or fully AI-written. Op-eds in WaPo, NYT and WSJ are 6.4× more likely than news to contain AI text, and only 5 of 100 flagged articles disclosed it.
- Relation: news prevalence via a per-document detector. No overlap or baseline analysis.

**1.15 Sun, Zhang, Shen, Zhang, Liu, Backes, Zhang, He (2025). "Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media." ACL 2025 (long), 2025.acl-long.1120.** https://aclanthology.org/2025.acl-long.1120 ; https://arxiv.org/abs/2412.18148
- Findings: 2.4M posts from Medium, Quora and Reddit (Jan 2022–Oct 2024). The AI Attribution Rate rose from 1.77% to 37.03% on Medium and from 2.06% to 38.95% on Quora. The rate is nonzero at the start, which is again a baseline that goes unanalysed.

**1.16 La Cava, Aiello, Tagarelli (2025). "Machines in the Crowd? Measuring the Footprint of Machine-Generated Text on Reddit." arXiv:2510.07226.** https://arxiv.org/abs/2510.07226
- Findings: 51 subreddits (2022–2024). Machine-generated text is marginal overall but peaks at up to 9% in some communities and months, concentrated in technical and support subreddits and among a few users.

**1.17 Yakura, Lopez-Lopez, Brinkmann, de la Serna, Kirfel, Gupta, Soraperra, Eisenmann, Wulff, Rahwan (2024–2026). "Empirical evidence of Large Language Model's influence on human spoken communication." arXiv:2409.01754 (v4, Jul 2026; no journal reference listed).** https://arxiv.org/abs/2409.01754
- v1 used about 280K academic YouTube talks. v4 uses a synthetic-control analysis of 737,083 hours from 824,634 podcast episodes plus a preregistered experiment (N = 496).
- Findings: "delve", "showcase", "boast", "intricacies" and "meticulous" rose abruptly in spontaneous speech after ChatGPT. A short chatbot exchange led participants to adopt the bot's words, and the effect persisted past a distractor task.
- Relation: **strong evidence that humans move into the LLM style region without LLM authorship**, which directly supports our "sounds like AI regardless of authorship" framing. It is lexical only and has no pre-2022 overlap level.

**1.18 Anderson, Galpin, Juzek (2025). "Model Misalignment and Language Change: Traces of AI-Associated Language in Unscripted Spoken English." AIES 2025, 8(1): 179–191.** https://ojs.aaai.org/index.php/AIES/article/view/36540 ; https://arxiv.org/abs/2508.00238
- Findings: 22.1M words from unscripted science and tech podcasts. AI-associated words showed a moderate but significant post-2022 rise, while baseline synonyms showed no directional shift. A press summary says about three-quarters of the words increased (**UNVERIFIED**).
- Relation: same as 1.17. Its synonym-control design is useful to us.

**1.19 Matsui (2024). "Delving into PubMed Records: Some Terms in Medical Writing Have Drastically Changed after the Arrival of ChatGPT." medRxiv preprint.** DOI: https://doi.org/10.1101/2024.05.14.24307373 — the existence of the record is verified. Findings are **UNVERIFIED** because I could not read the abstract.

**Patents:** I found **no peer-reviewed prevalence study**. An IAM Media trade article ("'ChatGPTisms' popping up in patent applications," https://www.iam-media.com/article/chatgptisms-popping-in-patent-applications) reports a word-frequency spike about 18 months after launch. It is paywalled and **UNVERIFIED**.

---

## 2. Homogenization and diversity loss

**2.1 Padmakumar & He (2024). "Does Writing with Language Models Reduce Content Diversity?" ICLR 2024.** https://proceedings.iclr.cc/paper_files/paper/2024/hash/02dec8877fb7c6aa9a79f81661baca7c-Abstract-Conference.html ; https://arxiv.org/abs/2309.05196
- Controlled argumentative-essay study with three conditions: no model, GPT-3, and InstructGPT. Only InstructGPT co-writing significantly reduced diversity (essays became more similar, with lower lexical and content diversity). The effect came mainly from the model-contributed text.
- Relation: points to feedback tuning as the cause of a narrow "LLM region," which supports defining the region from instruction-tuned output. It measures homogenization, not overlap with pre-existing human text.

**2.2 Doshi & Hauser (2024). "Generative AI enhances individual creativity but reduces the collective diversity of novel content." *Science Advances* 10(28): eadn5290.** DOI: https://doi.org/10.1126/sciadv.adn5290 ; PMC11244532
- Online experiment (293 writers; 3,519 evaluations from 600 evaluators). Seeing AI ideas made stories more creative, better written and more enjoyable, especially for less creative writers, but AI-assisted stories were more similar to one another.
- Relation: homogenization background. Experimental and not population-level.

**2.3 Anderson, Shah, Kreminski (2024). "Homogenization Effects of Large Language Models on Human Creative Ideation." Creativity & Cognition '24.** DOI: https://doi.org/10.1145/3635636.3656204 ; https://arxiv.org/abs/2402.01536
- With 36 participants, ChatGPT users produced less semantically distinct ideas across users than users of an alternative tool, and reported less ownership.
- Relation: background.

**2.4 Sourati, Karimi-Malekabadi, Ozcan, McDaniel, Ziabari, Trager, Tak, Chen, Morstatter, Dehghani (2025/2026). "The Shrinking Landscape of Linguistic Diversity in the Age of Large Language Models." *Nature Human Behaviour* (2026), DOI 10.1038/s41562-026-02550-0** (per the arXiv journal reference). https://arxiv.org/abs/2502.11266
- Three studies, seven datasets, more than 880K texts. LLM rewriting preserves content but homogenizes style. Writing-complexity variance falls 21–50% (p ≤ .05), and output shifts toward dominant-group characteristics. A secondary summary says the datasets include papers, news and Reddit from before and after ChatGPT (**UNVERIFIED** detail).
- Relation: **important neighbour**. It shows style *variance shrinking*, which is the companion of our "moving into the region" claim. It is still framed around LLM-rewritten text, not human text that already sat in the region.

**2.5 Sourati, Ziabari, Dehghani (2026). "The Homogenizing Effect of Large Language Models on Human Expression and Thought." *Trends in Cognitive Sciences* (opinion; online Mar 2026 per a listing; **UNVERIFIED** date).** https://arxiv.org/abs/2508.01491
- A review and argument that LLMs reinforce dominant styles and that this convergence can amplify across users. Theory and framing support only.

**2.6 Kirk, Mediratta, Nalmpantis, Luketina, Hambro, Grefenstette, Raileanu (2024). "Understanding the Effects of RLHF on LLM Generalisation and Diversity." ICLR 2024.** https://proceedings.iclr.cc/paper_files/paper/2024/hash/5a68d05006d5b05dd9463dd9c0219db0-Abstract-Conference.html ; https://arxiv.org/abs/2310.06452
- RLHF generalizes better out of distribution than SFT but significantly reduces output diversity across measures.
- Relation: mechanism for why the LLM style region is compact, which makes "fraction of human text inside it" a meaningful quantity.

**2.7 Wu, Black, Chandrasekaran (2025). "Generative Monoculture in Large Language Models." ICLR 2025.** https://arxiv.org/abs/2407.02209
- Output diversity narrows relative to the training data (e.g., uniformly positive reviews for books with mixed reception). Changing sampling or prompts does not fix it, and the authors blame alignment.
- Relation: mechanism and background.

**2.8 Juzek & Ward (2025). "Why Does ChatGPT 'Delve' So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models." COLING 2025, pp. 6397–6411.** https://aclanthology.org/2025.coling-main.426/ ; https://arxiv.org/abs/2412.11385
- Identifies 21 focal words whose rise in abstracts is likely LLM-driven. Finds no evidence the cause is architecture, algorithm choice or training data, and finds evidence consistent with RLHF contributing.
- Relation: if the region's markers come from RLHF preferences that humans *already* had (raters preferred them), then some pre-2022 human text should already sit in the region. This is theoretical support for a nonzero pre-2022 overlap.

**2.9 Gude, Santos-Rios, Bond, Flickinger, Gómez-Rodríguez, Zamaraeva (2026). "More Aligned, Less Diverse? Analyzing the Grammar and Lexicon of Two Generations of LLMs." ACL 2026 (long), pp. 38900–38911.** https://aclanthology.org/2026.acl-long.1803/
- HPSG-based syntactic and lexical diversity, compared with NYT text from 2023 and 2025. Human news changed little between the two periods. Newer instruction-tuned models have lower syntactic and especially lower lexical diversity.
- Relation: a counter-signal, since human NYT text shows little drift (but with no pre-2022 data). The region definition must be model-generation-specific.

---

## 3. Stylometric and linguistic differences between human and LLM text

**3.1 Reinhart, Markey, Laudenbach, Pantusen, Yurko, Weinberg, Brown (2025). "Do LLMs write like humans? Variation in grammatical and rhetorical styles." *PNAS* 122(8): e2422455122.** DOI: https://doi.org/10.1073/pnas.2422455122 ; https://arxiv.org/abs/2410.16107
- Parallel human and LLM corpora from shared prompts (Llama 3 variants, GPT-4o), compared on Biber lexico-grammatical features. Systematic human–LLM and inter-LLM differences persist with scale and are larger for instruction-tuned models than for base models (e.g., denser, noun-heavy, more "academic" register).
- Relation: **supplies the feature space** for defining a "style region." It measures *differences*, not the fraction of human texts falling in the LLM region, and has no temporal or pre-2022 analysis.

**3.2 Rallapalli, Gallagher, Yurko, Brooks, Loughin, Sezgin, Turri (2026). "Interpretable Stylistic Variation in Human and LLM Writing Across Genres, Models, and Decoding Strategies." arXiv:2604.14111.** https://arxiv.org/abs/2604.14111
- Biber features for 11 LLMs × 8 genres × 4 decoding strategies. **Genre has a stronger effect on style than source (human vs LLM)**. Chat-tuned models cluster together, and model matters more than decoding.
- Relation: **the most important confound paper for us**. If genre dominates, then human academic abstracts may naturally sit near the LLM region, so pre-2022 overlap is expected and must be stratified by genre. It supports the premise but also warns that "overlap" may reduce to "genre."

**3.3 Muñoz-Ortiz, Gómez-Rodríguez, Vilares (2024). "Contrasting Linguistic Patterns in Human and LLM-Generated News Text." *Artificial Intelligence Review*.** DOI: 10.1007/s10462-024-10903-2 ; https://arxiv.org/abs/2308.09067
- Compared with LLM news text, human news has more scattered sentence lengths, richer vocabulary, different dependency and constituent distributions, and more negative emotion. LLM text has more numbers, symbols, auxiliaries and pronouns.
- Relation: feature candidates. No overlap or temporal analysis.

**3.4 Cao, Go, Hu, Sushmita (2026). "Temporal Flattening in LLM-Generated Text: Comparing Human and LLM Writing Trajectories." Findings of ACL 2026 (per arXiv).** https://arxiv.org/abs/2604.12097
- 412 authors and 6,086 documents (2012–2024). LLMs show *higher* lexical diversity but much less semantic and affective drift over time. Temporal-variability features alone separate human from LLM trajectories (94% accuracy, 98% ROC-AUC).
- Relation: a caveat that LLM output is not uniformly "less diverse" on every axis (e.g., lexical diversity), so the region definition matters.

**3.5 Wang, Tripto, Park, Li, Zhou (2025). "Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors." Findings of EMNLP 2025.** https://arxiv.org/abs/2509.14543
- LLMs imitate structured styles (news, email) well and informal styles (blogs, forums) poorly. A secondary review reports figures of about 95% versus about 17–21% (**UNVERIFIED** numbers).
- Relation: overlap depends on genre. Formal genres are more imitable, so expect higher overlap there.

**3.6 Dawkins, Fraser, Kiritchenko (2025). "When Detection Fails: The Power of Fine-Tuned Models to Generate Human-Like Social Media Text." arXiv:2506.09975 ("to appear in ACL Findings").** https://arxiv.org/abs/2506.09975
- 505,159 generated posts. Detection collapses when the fine-tuned model is private. A secondary source says Biber-feature differences shrink sharply after fine-tuning (**UNVERIFIED**).
- Relation: the region is model- and tuning-dependent.

**3.7 Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui (2021). "MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers." NeurIPS 2021 (Outstanding Paper).** https://papers.nips.cc/paper/2021/hash/260c2432a0eecc28ce03c10dadc078a4-Abstract.html
- A distribution-level divergence between human and model text in a quantized embedding space.
- Relation: **methodological precedent for distributional overlap**, used for evaluating models rather than measuring human drift. It could serve as one of our overlap metrics.

**3.8 Yang, Wenger, So (2026). "Where Models Converge and Humans Diverge: A Coverage Framework for Distributional Pluralism in Open-Ended Generation." arXiv:2608.05576.** https://arxiv.org/abs/2608.05576
- Introduces LLM-Coverage and In-Boundary Rate (whether LLM outputs fall inside the human response boundary). LLM output is plausible but narrow, concentrated near the centre of human space.
- Relation: **the inverse of our metric** (LLM-in-human-region rather than human-in-LLM-region). It is a useful formal analogue to cite, with no temporal component.

---

## 4. Model collapse and feedback loops

**4.1 Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal (2024). "AI models collapse when trained on recursively generated data." *Nature* 631: 755–759.** DOI: https://doi.org/10.1038/s41586-024-07566-y
- Recursive training on generated data loses distribution tails (LLMs, VAEs, GMMs).
- Relation: motivation. If human text drifts into the LLM region, "human" training data is no longer an independent anchor.

**4.2 Gerstgrasser et al. (2024). "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data." arXiv:2404.01413 (also listed at ICML 2024 workshop pages: https://icml.cc/virtual/2024/36382).** https://arxiv.org/abs/2404.01413
- Replacing real data with synthetic data leads to collapse, while accumulating both keeps test error bounded (shown in theory and experiments).
- Relation: the accumulate-versus-replace assumption hinges on real data staying "real." Human style drift is an underexplored third path.

**4.3 Dohmatob, Feng, Yang, Charton, Kempe (2024). "A Tale of Tails: Model Collapse as a Change of Scaling Laws." ICML 2024, PMLR 235: 11165–11197.** https://proceedings.mlr.press/v235/dohmatob24b.html
- Synthetic data truncates tails and changes scaling laws, shown in theory plus Llama-2 experiments.
- Relation: background.

**4.4 Human adoption of LLM style:** Yakura et al. (1.17), Anderson/Galpin/Juzek (1.18), Geng & Trotta 2025 (1.7) and Lin & Zhu (1.9) are the empirical evidence that the human side of the loop moves.

---

## 5. Prior work on "pre-ChatGPT human text that already looked like AI" and genre as a confound

**5.1 Liang, Yuksekgonul, Mao, Wu, Zou (2023). "GPT detectors are biased against non-native English writers." *Patterns* 4(7): 100779.** DOI: https://doi.org/10.1016/j.patter.2023.100779 ; https://arxiv.org/abs/2304.02819
- Seven detectors were tested on 91 human-written TOEFL essays (pre-ChatGPT human text). The average false-positive rate was 61.22%. All seven detectors flagged 18 of 91 essays (19.78%), and at least one flagged 89 of 91 (97.80%). The cause is low perplexity from constrained vocabulary.
- Relation: **the clearest prior demonstration that some human text sounds like AI regardless of authorship**. It is framed as detector bias, at small scale, for one population, and not as a population-level style region or a trend.

**5.2 Park, Jeong, Kim (2026). "Style as a Confound: False Positives in AI Detection of Non-Native Academic Writing." arXiv:2608.26710 (listed as EMNLP 2026).** https://arxiv.org/abs/2608.26710
- 135,389 pairs of original and professionally edited manuscripts (2018–2025), scored by 13 detectors. False-positive rates on human text range from 0% to 100% across detectors. Edits move scores in opposite directions depending on the detector, and the shift scales with editing intensity. A search summary says the paper splits baselines into pre-ChatGPT (2018–2022) and post-ChatGPT periods (**UNVERIFIED**; the abstract does not report a breakdown).
- Relation: **the closest framing to "style, not authorship"**, including pre-2022 human documents. Its scope is detector fairness on edited non-native writing, not the share of a whole genre in an LLM style region or a trend break. It must be cited prominently.

**5.3 Rallapalli et al. 2026 (3.2): genre outweighs source.** This is the strongest evidence that genre convention is a confound for any overlap measure.

**5.4 Pre-period as noise in prevalence estimators:** Liang et al. 2024 (pre-ChatGPT α of 2.3–3.1%, 1.3), Lin & Zhu 2025 (pre-period subtracted as misclassification, 1.9), Brooks et al. 2024 (1% FPR calibration on pre-GPT-3.5 Wikipedia, 1.13), Sun et al. 2025 (nonzero AAR in Jan 2022, 1.15). All four *observe* nonzero pre-ChatGPT "AI-likeness" and **treat it as estimator error**.

**5.5 Juzek & Ward 2025 (2.8):** RLHF and rater preference as the source of LLM-favoured words implies the style existed in human preference before ChatGPT. This is indirect support.

---

## Novelty assessment

**Is "overlap with a pre-2022 baseline" already done?** **Partially, but not as framed.** No paper I found treats *the fraction of human-written text that falls inside an LLM-defined multi-feature style region* as the primary object of study, measures its pre-2022 level, and then tests whether the post-Nov-2022 trajectory exceeds the extrapolated pre-trend. The pieces exist separately, however, and reviewers will know them.

**Closest prior works, and what each already covers:**
1. **Liang et al. 2024 (COLM/NHB) and Lin & Zhu 2025.** Both observe a nonzero pre-ChatGPT "AI" share in arXiv (α ≈ 2.3–3.1% in Nov 2022, and about 7.75% of unrevised abstracts misclassified, respectively). Both dismiss it as false positives. *Gap: nobody decomposes or interprets the baseline (by field, genre, author type, or pre-2022 trend).*
2. **Kobak et al. 2025, Holzwarth et al. 2026, Lee 2026 and Bentley et al. 2026.** All four run post-2022 versus pre-trend designs. Kobak, Holzwarth and Lee use word frequencies with trend extrapolation and placebo floors. Bentley uses an arXiv style index from 2010 with a pre-trend. *Gap: these are lexical marker counts, not a distributional style region, and none asks how much pre-2022 human text already sat in the region. Bentley notes the index was rising pre-2023 but does not analyse it.*
3. **Liang et al. 2023 (Patterns) and Park et al. 2026 (EMNLP).** These show that human text, including pre-2022 text, scores as AI because of style (low perplexity, non-native or edited writing). *Gap: framed as detector bias, not tracked over time, and not population-level across a genre.*
4. **Yakura et al., Anderson/Galpin/Juzek, Lin & Zhu, Alani & Jansen, Sourati et al.** These show humans moving toward LLM style (speech, abstracts) and style variance shrinking. *Gap: lexical markers or rewriting experiments, with no baseline overlap level and no trend-break test on a multi-feature region.*
5. **Reinhart et al. 2025 and Rallapalli et al. 2026.** These provide the Biber feature space and show genre > source. *Gap: cross-sectional, with no temporal or pre-2022 trajectory. Rallapalli is also the main threat, since "overlap" may simply equal "academic register."*

**Remaining defensible gap:** (a) define the LLM style region in a multi-feature space (Biber, stylometric or embedding) that does not depend on marker words, which Geng & Trotta 2025 show are unstable. (b) Report the **pre-2022 human-in-region fraction** as a substantive quantity, stratified by genre and field. (c) Test the **post-2022 deviation from the pre-2022 trend** with placebo years, following Lee 2026 and Kobak 2025. (d) Explicitly separate "sounds like AI" from "written by AI," citing Liang 2023, Park 2026 and Yakura 2026.

**Risks:**
- Reviewers may argue that the overlap metric is 1 − specificity of a detector, which Liang 2024 and Lin & Zhu already report. The paper must argue why the baseline is signal and not noise, for example by showing structure in it by field, author or trend.
- Reviewers may argue that overlap is just a genre effect (Rallapalli 2026). Genre and field stratification is needed.
- Bentley et al. (Jun 2026) and Alani & Jansen (2026) are recent and close in wording ("sound like ChatGPT"; arXiv style index since 2010). They must be cited and differentiated.
