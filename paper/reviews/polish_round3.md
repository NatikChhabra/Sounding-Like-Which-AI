# Round 3 polish: copy-edit changelog for main.tex

Scope: writing only. No claim, number, `\R{}` macro, citation key, label or figure/table content changed. A script checked that all 415 `\R{}`/`\ref`/`\label`/`\cite*` occurrences are identical before and after. The compile has no errors and no undefined references. The Conclusion still ends on p. 8 and Limitations starts on p. 9.

## Abstract
- Dropped the "therefore" from the closing reference-set sentence, so it now reads "...will eventually show the shift receding".

## Introduction
- AC 6.2: replaced "The two questions read one number differently: ..." with two plain sentences: "The two questions treat one number differently. Prevalence estimators report a small 'LLM share' ...".
- AC 6.2: "that share describes the two text distributions, and its change over time is our object of study" became "we treat that share as a property of the two text distributions and study how it changes over time".
- Changed "training data" to "pretraining data" to match the term used everywhere else, and folded "and we hold the task fixed" into "by vintage on a fixed task".
- AC 2.9: "added after review" became "added after simulated review", so ARR readers do not take it to mean an earlier ARR round.

## Related Work
- AC 6.3: replaced the delayed-subject inversion ("whether 'human' text remains an independent anchor is the question our vintage comparison bears on") with "Our vintage comparison asks whether human text still provides an anchor independent of LLM style."

## Data
- Terminology: "Archive-months ... smaller archives" became "Field-months ... smaller fields", because "field" is defined as "archive" one sentence earlier.
- AC 2.4j: "the 14 generators available before review" became "14 generators, each capped at 450 training texts". The old qualifier contradicted App. D(3), where Phi-4 and Granite were first used after the first review.

## Method
- AC 6.4: removed the aphoristic closer ("...: an instrument that merely ages would produce one"). The sentence now reads "..., so any gap they show reflects instrument ageing."
- AC 6.4: dropped "as the identified comparison", which implied causal identification. Defined the term **pre-ChatGPT-data region** here, at its first use.
- "so that topic words of the prompt set cancel" became "so that most topic words ... cancel", to match the existing Limitations caveat that the mined lists contain some topic words.

## Results
- 5.1: "Held out from training, the other generators are mostly recognised" became "Generators held out of training are mostly recognised".
- 5.3: split the number-heavy yearly-MSO sentence in two. Added the missing subject in "...or the trend, the gap stays between". Split the placebo-grid and drift-placebo sentence at the semicolon.
- 5.3 (AC 2.4l): reordered the field list to "computer science (38.1) and quantitative biology (36.2)", since cs is the larger.
- 5.4: the region is now named by its defined term ("The pre-ChatGPT-data region (GPT-4, ...)"). "Pre-2023 LLMs" became "the pre-ChatGPT-data generators"; the old wording was inaccurate because they were released in 2023. Split the long annual-means sentence before "Each change has...".
- 5.4 aggregate paragraph: "whether or not writing has stopped moving" became "even if writing keeps moving". "The ... region is the only comparison free of that ambiguity" became "Of our comparisons, only the pre-ChatGPT-data region avoids that ambiguity". The meaning is unchanged; both edits remove aphoristic closers.
- 5.5 markers (AC 6.5): "so the fair comparison is with marker words of..." became "so we also compare with words mined from...". Removed the "rather than conspicuous markers" pivot. Rephrased "diverge ... for some recent generators but not for older ones: once..." into two plain sentences with the same claim.

## Discussion and Conclusion
- "models pretrained before ChatGPT" (Discussion) and "models trained before ChatGPT" (Conclusion) now both read "the pre-ChatGPT-data generators".
- AC 6.6: changed the heading "The reference decides the trajectory" to "Trajectories depend on the reference". "'sounding like AI' there partly means writing well" became "...partly reflects writing quality".
- AC 6.6: split the "precondition, though not evidence" inversion: "Under either reading, ... no longer independent anchors for each other. This is a precondition for ... model-collapse work, though not evidence of them."
- AC 6.6: "flags fluent student writing more than learner writing" became "flags non-learner essays more often than learner essays". This is the comparison that was actually measured.
- Conclusion: "Which models define 'LLM style' decides whether the shift looks finished" became "Whether the shift looks finished depends on which models define 'LLM style'". Removed a "therefore", and "should state, and refresh, the vintage" became "should report the vintage ... and refresh them".

## Limitations and appendix
- Limitations: "eight archives (two of them physics archives)" became "eight fields (two of them in physics)".
- App. B (AC 6.5): "(on the logit scale X against Y)" became "(X against Y on the logit scale)".

## Not applied: these change claims or content, so the author must decide
- "cannot have learned it / cannot be an artefact" changed to "whose pretraining data predate ChatGPT / unlikely" (Contribution 4 and §5.4; AC 2.2).
- "about a third of the gap under all 14 generators" changed to the like-for-like 20.2 pp P1 comparison (AC 2.2).
- "did not change" changed to "we detect no change" for dispersion (Contribution 5; AC 6.2/2.6).
- The marker claim "the decline of *delve* mostly reflects which models the markers come from" and the Discussion sentence on *delve*. The AC says the data contradict both (AC 2.5).
- "Detectors ... will understate" changed to "may understate" (AC 6.6).
- The placebo evaluation cap ("or in November 2022 if earlier"), the χ² dof/statistic, and the Vicuna release month in Table 1 (2023-08).
- App. D(3) "texts were merged" changed to "prompt batches were committed" (git record), and "Every reported result" changed to "statistic" (AI Use).
- The unused `\TODO` macro definition (L14) was left in place.
- The AC's terminology table recommends "Claude" over "the 2026 model". Per the brief, "the 2026 model" is kept as the term for Claude throughout.
