### bao2024fastdetectgpt
- Title: {Fast-DetectGPT}: {E}fficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature
- Link: https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf
- Paper sentence: "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt}, need more text as machine and human distributions converge \citep{chakraborty2024}, and have flagged non-native writing \citep{liang2023detectors}, although detectors trained on a large writing assessment showed no such bias \citep{jiang2024} and false-positive rates on non-native manuscripts vary widely \citep{park2026}."
- Paper sentence: "An off-the-shelf zero-shot statistic behaves differently: the analytic Fast-DetectGPT criterion \citep{bao2024fastdetectgpt} computed with GPT-2 small separates our human and LLM abstracts only moderately (AUC \R{arxiv_fastdetect_auc.heldin_auc}), and its calibrated flag rate on 600 abstracts per year does not rise (\R{arxiv_fastdetect.2015.share_flagged}\% in 2015, \R{arxiv_fastdetect.2022.share_flagged}\% in 2022, \R{arxiv_fastdetect.2026.share_flagged}\% in 2026)."

### gemma3card
- Title: Gemma 3 Model Card
- Link: https://ai.google.dev/gemma/docs/core/model_card_3
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### gemma4card
- Title: Gemma 4 12{B} Model Card
- Link: https://huggingface.co/google/gemma-4-12B-it
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### gemmareleases
- Title: ?
- Link: ?
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### granitecards
- Title: {Granite} 3.3 8{B} Instruct and {Granite} 4.2 8{B} Model Cards
- Link: https://huggingface.co/ibm-granite/granite-4.2-8b
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### jiang2023mistral
- Title: Mistral 7B
- Link: https://arxiv.org/abs/2310.06825
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### liang2023detectors
- Title: {GPT} detectors are biased against non-native {English} writers
- Link: http://dx.doi.org/10.1016/j.patter.2023.100779
- Paper sentence: "Individual documents are harder: readers are poor at telling human from machine text \citep{clark2021, jakesch2023, casal2023}, detectors can be evaded \citep{sadasivan2025, krishna2023, dugan2024raid}, and some detectors have flagged non-native writers' human text as AI-generated at high rates \citep{liang2023detectors}."
- Paper sentence: "Zero-shot detectors use token-likelihood statistics \citep{hans2024binoculars, bao2024fastdetectgpt}, need more text as machine and human distributions converge \citep{chakraborty2024}, and have flagged non-native writing \citep{liang2023detectors}, although detectors trained on a large writing assessment showed no such bias \citep{jiang2024} and false-positive rates on non-native manuscripts vary widely \citep{park2026}."
- Paper sentence: "A GPT-2 perplexity instrument flags \R{essay_liang_perplexity_gpt2.Real TOEFL.mso}\% of TOEFL essays but \R{essay_liang_perplexity_gpt2.Real US 8th grade.mso}\% of US 8th-grade essays, reproducing the bias reported by \citet{liang2023detectors}, while flagging these school learners less than their peers: which learners such a detector penalises depends on how predictable their writing is (Appendix~\ref{app:learners})."
- Paper sentence: "RAID and the Hugging Face release of \citet{liang2023detectors}, MIT; their US 8th-grade essays come from the authors' GitHub repository, which states no licence, and derive from the Hewlett Foundation ASAP data, so we release only scores, not texts)."

### liang2024mapping
- Title: Mapping the Increasing Use of {LLM}s in Scientific Papers
- Link: https://openreview.net/forum?id=YX7QnhxESU
- Paper sentence: "\end{abstract} \section{Introduction} Corpus studies find traces of LLM-assisted writing in abstracts, peer reviews, press releases and encyclopedias \citep{kobak2025, liang2024mapping, liang2024monitoring, liang2025widespread, brooks2024}, and LLM-associated words have become more frequent in unscripted speech \citep{yakura2024, anderson2025spoken}."
- Paper sentence: "Prevalence estimators report a small ``LLM share'' for text written before ChatGPT, which studies treat as consistent with false positives \citep{liang2024mapping}, subtract as baseline misclassification \citep{lin2025}, or use to calibrate thresholds \citep{brooks2024}."
- Paper sentence: "\section{Related Work} \paragraph{Prevalence of LLM-assisted writing.} Excess-vocabulary methods compare word frequencies with a counterfactual extrapolated from pre-LLM years \citep{kobak2025, holzwarth2026, lee2026}; distributional methods fit a mixture of human and LLM word distributions \citep{liang2024mapping, liang2024monitoring, liang2025widespread, geng2024}; classifier- and detector-based studies label documents \citep{lin2025, brooks2024, sun2025, khan2026}."
- Paper sentence: "This is the high-CS, low-mathematics ordering that prevalence studies report \citep{liang2024mapping}."
- Paper sentence: "Through the mixture identity (\S\ref{sec:mso}), the 2024 values imply that \R{robustness_v4.implied.cs_2024_alpha_cv}\% of computer-science and \R{robustness_v4.implied.math_2024_alpha_cv}\% of mathematics abstracts were LLM output if nothing else had changed (\R{robustness_v4.implied.cs_2024_alpha_lomo}\% and \R{robustness_v4.implied.math_2024_alpha_lomo}\% using held-out-generator recall), against prevalence estimates of 17.5\% and 4.9\% of sentences by February 2024 \citep{liang2024mapping}."

### llama31card
- Title: Llama 3.1 Model Card
- Link: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### mccarthy2010
- Title: {MTLD
- Link: http://dx.doi.org/10.3758/BRM.42.2.381
- Paper sentence: "\paragraph{Features and instruments.} Features exclude content words to limit topic sensitivity: per-token rates of closed-class words, coarse part-of-speech trigrams, dependency labels and punctuation marks, plus mean and standard deviation of sentence length, mean word length and MTLD lexical diversity \citep{mccarthy2010}, computed with spaCy~3.8 (\texttt{en\_core\_web\_sm}); features present in fewer than 1\% of training documents are dropped (top features in Appendix~\ref{app:features})."

### openai2023gpt4
- Title: {GPT-4} Technical Report
- Link: https://arxiv.org/abs/2303.08774
- Paper sentence: "Qwen3 8B & 2025-04 & \\ gpt-oss 20B & 2025-08 & Jun 2024 \\ Claude Opus 5.5 (2026 model) & 2026 & \\ \midrule \multicolumn{3}{@{}l}{\emph{Local; vintage analysis only (abstracts, P1--P3)}} \\ Llama-2-Chat 7B & 2023-07 & Sep 2022$^b$ \\ Vicuna 7B v1.5$^d$ & 2023-08 & Sep 2022$^b$ \\ Qwen3.5 9B & 2026-02/03 & \\ Gemma 4 12B & 2026-06 & Jan 2025 \\ Granite 4.2 8B & 2026-08 & \\ \bottomrule \end{tabular} \caption{Reference generators, with release month and pretraining-data cutoff where the developer states one. $^a$\citet{openai2023gpt4}; $^b$\citet{touvron2023llama2}; $^c$reported only in second"

### openai2025gptoss
- Title: gpt-oss-120b \& gpt-oss-20b Model Card
- Link: https://arxiv.org/abs/2508.10925
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### phi4card
- Title: Phi-4 Model Card
- Link: https://huggingface.co/microsoft/phi-4
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### qwen35card
- Title: Qwen3.5-9{B} Model Card
- Link: https://huggingface.co/Qwen/Qwen3.5-9B
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### qwen3card
- Title: ?
- Link: ?
- Paper sentence: "Other dates: \citet{jiang2023mistral, llama31card, phi4card, gemma3card, qwen3card, granitecards, openai2025gptoss, qwen35card, gemmareleases, gemma4card}.} \label{tab:gens} \end{table} \section{Method} \label{sec:method} \paragraph{Cleaning.} All texts pass through the same normalisation: chat wrappers (``Here's the abstract:''), lines echoing the prompt's title, markdown and trailing notes are removed; typographic variants and mis-decoded characters are mapped to plain equivalents;"

### touvron2023llama2
- Title: Llama 2: Open Foundation and Fine-Tuned Chat Models
- Link: https://arxiv.org/abs/2307.09288
- Paper sentence: "Qwen3 8B & 2025-04 & \\ gpt-oss 20B & 2025-08 & Jun 2024 \\ Claude Opus 5.5 (2026 model) & 2026 & \\ \midrule \multicolumn{3}{@{}l}{\emph{Local; vintage analysis only (abstracts, P1--P3)}} \\ Llama-2-Chat 7B & 2023-07 & Sep 2022$^b$ \\ Vicuna 7B v1.5$^d$ & 2023-08 & Sep 2022$^b$ \\ Qwen3.5 9B & 2026-02/03 & \\ Gemma 4 12B & 2026-06 & Jan 2025 \\ Granite 4.2 8B & 2026-08 & \\ \bottomrule \end{tabular} \caption{Reference generators, with release month and pretraining-data cutoff where the developer states one. $^a$\citet{openai2023gpt4}; $^b$\citet{touvron2023llama2}; $^c$reported only in second"

### vicuna15card
- Title: ?
- Link: ?
- Paper sentence: "Qwen3 8B & 2025-04 & \\ gpt-oss 20B & 2025-08 & Jun 2024 \\ Claude Opus 5.5 (2026 model) & 2026 & \\ \midrule \multicolumn{3}{@{}l}{\emph{Local; vintage analysis only (abstracts, P1--P3)}} \\ Llama-2-Chat 7B & 2023-07 & Sep 2022$^b$ \\ Vicuna 7B v1.5$^d$ & 2023-08 & Sep 2022$^b$ \\ Qwen3.5 9B & 2026-02/03 & \\ Gemma 4 12B & 2026-06 & Jan 2025 \\ Granite 4.2 8B & 2026-08 & \\ \bottomrule \end{tabular} \caption{Reference generators, with release month and pretraining-data cutoff where the developer states one. $^a$\citet{openai2023gpt4}; $^b$\citet{touvron2023llama2}; $^c$reported only in second"

### zheng2023judging
- Title: Judging {LLM}-as-a-Judge with {MT}-Bench and Chatbot Arena
- Link: https://arxiv.org/abs/2306.05685
- Paper sentence: "Qwen3 8B & 2025-04 & \\ gpt-oss 20B & 2025-08 & Jun 2024 \\ Claude Opus 5.5 (2026 model) & 2026 & \\ \midrule \multicolumn{3}{@{}l}{\emph{Local; vintage analysis only (abstracts, P1--P3)}} \\ Llama-2-Chat 7B & 2023-07 & Sep 2022$^b$ \\ Vicuna 7B v1.5$^d$ & 2023-08 & Sep 2022$^b$ \\ Qwen3.5 9B & 2026-02/03 & \\ Gemma 4 12B & 2026-06 & Jan 2025 \\ Granite 4.2 8B & 2026-08 & \\ \bottomrule \end{tabular} \caption{Reference generators, with release month and pretraining-data cutoff where the developer states one. $^a$\citet{openai2023gpt4}; $^b$\citet{touvron2023llama2}; $^c$reported only in second"
