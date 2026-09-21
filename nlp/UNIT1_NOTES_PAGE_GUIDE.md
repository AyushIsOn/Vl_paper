# `NLP-UNIT-1-notes.pdf` — Page-by-Page Guide (for DSE4150, syllabus ≤ Lec 20)

48 pages total: **17 must-read · 11 optional · 20 skip**.

---

## Tier 1 — Must read (17 pages)

| Page | Content | Lec |
| --- | --- | --- |
| 2 | NLP definition, why it matters, "Levels in NLP" diagram | L2 |
| **3** | **The 5 phases** (Lexical → Syntactic → Semantic → Discourse → Pragmatic) + Applications of NLP + Georgetown-IBM 1954 | L2 |
| 5 | **§4 Navigating Phrasing Ambiguities** — 5 resolution approaches. §5 Misspellings | L4 |
| 7 (2nd half) | "Language and Grammar in NLP" begins; Phonological Level | L3 |
| **8** | Morphological / Lexical (`bank`) / Syntactic / Semantic (*"I saw a man with a telescope"*) levels | L3, L4 |
| **9** | Pragmatic + Discourse levels; **Grammar in NLP** + list of 9 grammar types | L3, L5 |
| 15 | Regular Expression defn; **FSA defn + Components (Q, Σ, δ, q₀, F)** + Types | L6, L7 |
| **16** | **DFA in full** — 5-tuple, δ: Q×Σ→Q, 4 characteristics, working, example | L8 |
| **17** | **NFA in full** — 5-tuple, δ: Q×(Σ∪{ε})→P(Q), 4 characteristics | L9 |
| 18 | NFA example; **Tokenization** defn + the 5 types | L9, L20 |
| **19** | **Word Tokenization** — `isn't` split, importance, **5 challenges** | L20 |
| **20** | **Sentence Tokenization** — boundary detection, example, importance | L20 |
| **31** | **Sentence Splitting / SBD** — challenges: Dr., 3.14, A.P.J., URLs, quotes | L20 |
| 32 | NLTK `sent_tokenize`; **Morphological Parsing** defn, `unhappiness` | L20, L11 |
| 33 | **Stemming** — heuristics, `studies → studi` (non-word) | L11, L18 |
| 34 | **Lemmatization** — lemma, `better → good`, POS-aware | L11 |
| **35** | **Stemming vs Lemmatization comparison table**; Porter / Snowball / Lancaster | L11, L18 |

**The 9 highest-value pages: 3, 8, 9, 16, 17, 19, 20, 31, 35.**

---

## Tier 2 — Read if time (11 pages)

| Page | Content | Lec |
| --- | --- | --- |
| 4 | Statistical era (n-grams, HMM, NER); deep learning era; Challenges §1–3 | L3/L4 |
| 6 | **§7 Words with Multiple Meanings — polysemy / homonymy**; biases; multilinguality | L4 |
| 10 | Transformational Grammar (deep/surface); LFG (C-/F-structure) | L5 |
| 11 | GB (Government, Binding); GPSG; Dependency Grammar | L5 |
| 12 | **Paninian Grammar — Karaka system** (Karta, Karma, Karana, Adhikarana). Ties to textbook **T2** | L5 |
| 13 | TAG (initial/auxiliary trees, substitution/adjunction); CFG begins | L5 |
| 14 | CFG rules; PCFG (probabilities sum to 1 per LHS) | L5 |
| 21 | Character Tokenization | L20 |
| 22 | **Sub-Word Tokenization** — `unhappiness → un\|happi\|ness`, OOV, BERT/GPT/T5 | L20 |
| 23 | N-gram Tokenization — unigram/bigram/trigram | L20 |
| 27 | Sentence-segmentation challenges (reinforces p31) | L20 |

---

## Tier 3 — Skip (20 pages, 42% of the document)

| Pages | Content | Belongs to |
| --- | --- | --- |
| 1 | The notes' own Unit-1 syllabus | — |
| 24–26, 28–30 | Text Segmentation (paragraph/word/subword/character) | Lec 23 |
| 36–39 | Spelling error detection & correction (7 methods) | Lec 21, 24 |
| 40 | Minimum Edit Distance / Levenshtein + DP matrix | Lec 21, 24 |
| 41–46 | Statistical models: unigram / bigram / trigram + Python | Lec 25–27 |
| 46–48 | Indian Language Processing, ILP levels, IndicBERT | Not in handout |

---

## Exam-bait specifics worth memorising

- **p3** — Georgetown-IBM experiment, 1954, 60 Russian sentences
- **p8** — *"I saw a man with a telescope"* (syntactic/semantic ambiguity); `bank` → financial/river (polysemy)
- **p9** — *"Can you open the window?"* (pragmatics); *Ravi went home. He was tired.* (discourse/anaphora)
- **p12** — Karaka roles: Karta (doer), Karma (object), Karana (instrument), Adhikarana (location)
- **p16** — DFA: **exactly one** transition per (state, symbol); **no ε-transitions**
- **p17** — NFA: δ maps to **P(Q), the power set**; accepts if **at least one** path ends in a final state
- **p19** — `NLP is fun, isn't it?` → `NLP | is | fun | , | is | n't | it | ?`
- **p19** — 5 word-tokenization challenges: punctuation, contractions, hyphenation, MWEs, language dependency
- **p20/27/31** — sentence-boundary hard cases: `Dr.`, `etc.`, `U.S.A.`, `3.14`, `A.P.J.`, ellipsis, quotes, URLs
- **p22** — `unhappiness → un | happi | ness`
- **p33** — `studies → studi` (stemmer produces a non-word)
- **p35** — Porter / Snowball / Lancaster are **stemmers**, not lemmatizers

---

## Three defects in this PDF

1. **p15's regex section is broken.** It opens with 10 bullets describing grammar/parsing benefits ("Identifies subject, verb, object and modifiers", "Supports syntactic parsing") — a copy-paste error. These are **not** properties of regular expressions.
2. **No regex syntax anywhere in 48 pages.** No `.` `*` `+` `?` `[ ]` `^` `$` `\d` `\w` `\s` `{n,m}` `\b`. **L10 cannot be studied from this file** — use `Regular_Expressions_in_NLP (1).pdf` pp. 4–7.
3. **p15 lists only DFA and NFA as FSA types — no transducer.** L6 requires "Acceptor *and* Transducer"; that half is only in `PPT-2` slides 27, 30, 31.
