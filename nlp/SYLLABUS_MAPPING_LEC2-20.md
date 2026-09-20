# DSE4150 NLP — Syllabus Mapping for Lectures 2–20

Scope: everything up to and including **Lecture 20 (Text Processing — Words and sentence tokenization)**, per the lecture plan in `Course_Handout_DSE4150.pdf` (pages 5–6).

Note: the handout's lecture plan table starts at Lecture 2 — there is no Lecture 1 row.

---

## 1. Topics in the course handout up to Lecture 20

### Module A — Introduction (Lec 2–5) · CO: DSE4150.1

| Lec | Topic | Delivery |
| --- | --- | --- |
| 2 | Phases of NLP | Lecture |
| 3 | Knowledge in Speech and Language Processing, and Ambiguity | Problem solving |
| 4 | Knowledge in Speech and Language Processing, and Ambiguity (contd.) | Lecture |
| 5 | Overview of different models and algorithms in NLP | Lecture |

### Module B — Finite State Machine (Lec 6–10) · CO: DSE4150.2

| Lec | Topic | Delivery |
| --- | --- | --- |
| 6 | Basics of Finite State Automata — Acceptor and Transducer, and its Categorization | Problem solving |
| 7 | Formal language and its acceptance; DFA and NFA | Lecture |
| 8 | DFA | Lecture |
| 9 | NFA | Lecture |
| 10 | Relation and difference between DFA and NFA; Basic Regular Expression Patterns | Problem solving |

### Module C — Morphological Analysis (Lec 11–19) · CO: DSE4150.2 / .3

| Lec | Topic | Delivery |
| --- | --- | --- |
| 11 | Survey of English Morphology | Lecture |
| 12 | Inflectional Morphology | Lecture |
| 13 | Derivational Morphology | Lecture |
| 14 | Finite-State Morphological Parsing | Lecture |
| 15 | Building a Finite State Lexicon | — |
| 16 | FSTs for Morphological Parsing | Self study |
| 17 | Orthographic Rules | Lecture |
| 18 | Lexicon-Free FSTs | Lecture |
| 19 | Inflectional & Derivational Morphology | Lecture |

### Module D — Text Processing (Lec 20 only) · CO: DSE4150.4

| Lec | Topic | Delivery |
| --- | --- | --- |
| 20 | Words and sentence tokenization | Lecture |

**Out of scope** (Lec 21+): spelling error detection/correction, normalizing text, segmentation, N-grams, smoothing, POS tagging, constituency/dependency parsing, CKY.

---

## 2. PDF → syllabus mapping

| # | File | Pages | Lectures covered | In-scope? |
| --- | --- | --- | --- | --- |
| 1 | `Course_Handout_DSE4150.pdf` | 9 | — (defines scope) | Reference |
| 2 | `PPT-2 morphology and FSM.pdf` | 40 | 6–19 | **Fully in scope** |
| 3 | `PPT1 morphology and FSM.pdf` | 29 | 11–19 (+6, 9) | **Fully in scope** |
| 4 | `Introduction to Theory of Computation.pdf` | 41 | 6–10 | **Fully in scope** |
| 5 | `Regular_Expressions_in_NLP (1).pdf` | 15 | 10 (+20) | **Fully in scope** |
| 6 | `NFA_Formal_Architecture.pdf` | 13 | 9–10 | **Fully in scope** |
| 7 | `Beyond_Determinism.pdf` | 9 | 8–10 | **Fully in scope** |
| 8 | `NLP-UNIT-1-notes.pdf` | 48 | 2–20 (+21–27) | Partly beyond |
| 9 | `Lecture notes 20 ...spelling-correction-notes.pdf` | 14 | 20 (+21, 24) | Partly beyond |
| 10 | `PPT -3 tokenization-multilinguality.pdf` | 76 | 20 only | ~Half out of syllabus |

### Detail per file

**`NLP-UNIT-1-notes.pdf`** — the only source for Lec 2–5.
- Intro to NLP, 5 levels (lexical → pragmatic), applications → **Lec 2**
- Origins & challenges; phrasing ambiguity, polysemy/homonymy → **Lec 3–4**
- Language & Grammar: 7 linguistic levels (phonological → discourse) → **Lec 3–4**
- 9 grammar types (Transformational, LFG, GB, GPSG, DG, Paninian, TAG, CFG, PCFG) → **Lec 5** (partly Lec 32–34)
- Regex + FSA 5-tuple, DFA, NFA with examples → **Lec 6–10**
- Tokenization: word / sentence / character / subword / N-gram, each with importance, challenges, applications → **Lec 20**
- Morphological parsing, stemming, lemmatization, stemming-vs-lemmatization table → **Lec 11–14** (linguistic only, no FSTs)
- *Beyond:* text segmentation levels, sentence splitting (Lec 23), spelling errors + MED (Lec 21/24), unigram/bigram/trigram (Lec 25–27), Indian language processing

**`PPT-2 morphology and FSM.pdf`** (Illinois CS447, Hockenmaier) — best single source for Module B + C.
- Word types vs tokens, lemma vs surface form, Turkish agglutination → **Lec 11**
- Inflection (verb/noun/pronoun paradigms) → **Lec 12**; derivation (nominalization, negation, adjectivization) → **Lec 13**
- Morphemes, stems, affixes, free/bound, morphs, allomorphs, surface vs underlying → **Lec 11, 17**
- Formal languages: Σ, string ω, ε, Kleene closure Σ*, L ⊆ Σ* → **Lec 7**
- Automata → language classes (FSA=regular, PDA=CF, TM=RE); aⁿbⁿ not regular → **Lec 7**
- FSA 5-tuple ⟨Q,Σ,q₀,F,δ⟩; DFA δ:Q×Σ→Q vs NFA δ:Q×Σ→2^Q; accept/reject traces → **Lec 8–10**
- Regular expressions → **Lec 10**
- FSAs for derivational morphology; union/merging automata with ε → **Lec 15**
- Recognition vs analysis (cats → cat+N+pl); morphological parsing of *disgracefully*; generation + overgeneration → **Lec 14, 16**
- **FST 7-tuple ⟨Q,Σ,Δ,q₀,F,δ,σ⟩** with output function σ → **Lec 6 (transducer), 16**
- FST as relation Lin×Lout; inversion T⁻¹; composition/cascade T∘T′ → **Lec 16**
- E-insertion (fox+s→foxes), E-deletion (make+ing→making); intermediate representation `cat^s#`; `T_lex` and `T_e-insert` cascade with full state diagram → **Lec 17**
- Ambiguity in analysis (book +N+sg vs +V), need for nondeterministic FST → **Lec 18 (partial)**

**`PPT1 morphology and FSM.pdf`** (Cambridge, Copestake/Buttery) — sharpest on orthographic rules.
- Morpheme, affix, stem, compound, free/bound; suffix/prefix/infix/circumfix → **Lec 11**
- Inflectional morphemes + paradigm → **Lec 12**; derivational morphemes → **Lec 13**
- Language typology: isolating, synthetic, agglutinative, inflected; English as analytic → **Lec 11**
- Morpheme vs structural ambiguity; bracketing of *un-ion-ise-ed* → **Lec 11, 3–4**
- Morphology in NLP: full-form lexicon, stemming, lemmatization, morphosyntax, bidirectional processing → **Lec 11, 14**
- **e-insertion rule in formal notation** ε → e / [s,x,z] ^ __ s → **Lec 17**
- Affix lexicon entries (`ed PAST_VERB`, `s PLURAL_NOUN`), irregular forms (began/begun) → **Lec 15**
- FSA for recognition (day/month), recursive FSA, overgeneration → **Lec 6, 9**
- FST with surface:underlying pairs; `cakes↔cake^s`, `boxes↔box^s`; step-by-step trace of *boxes* → **Lec 14, 16**
- Using FSTs: one char pair per transition, one FST per spelling rule, limitations (no internal structure) → **Lec 16, 18**

**`Introduction to Theory of Computation.pdf`** — the numerical/problem-solving source for Module B.
- Symbol, alphabet Σ, string, |w|, ε, 2ⁿ strings of length n; Kleene closure L*/L⁺ → **Lec 7**
- Language; regular / context-free / context-sensitive / recursively enumerable → **Lec 7**
- FA definition {Q,Σ,q,F,δ}, features, applications → **Lec 6** (acceptor only)
- DFA + transition table/diagram; minimization, unreachable states, trap/dead state → **Lec 8**
- NFA + transition table; ε-moves → **Lec 9**
- DFA vs NFA comparison table → **Lec 10**
- **NFA→DFA subset construction** (worked examples), equivalence of two FA, 1 ≤ n ≤ 2^m → **Lec 10**
- Regex elements: repeaters, `* + { } . ? ^ $`, `\d \w \s \b`, negated classes → **Lec 10**
- **Designing FA from regex:** even # of a's, `ab` as substring, count of a divisible by 3, binary divisible by 3, odd # of a's → **Lec 10**

**`Regular_Expressions_in_NLP (1).pdf`** — pure Lec 10.
- Regex definition, `c.t`; why regex matters in NLP; basic syntax `. * + ? [ ] |`
- Character classes `\d \w \s`; quantifiers `{n}`, `{n,m}`; anchors `^ $ \b`; groups/capturing
- Worked examples: email extraction, **tokenizing a sentence with `\w+|[^\w\s]`** (→ also **Lec 20**), cleaning HTML with `re.sub`
- NLP regex cheat sheet; Python `re` module (`match`, `search`, `findall`, `sub`, `split`)

**`NFA_Formal_Architecture.pdf`** — Lec 9–10 only. Image-only PDF (OCR'd; no selectable text).
- NFA accepting strings ending in `0`; DFA vs NFA functional shift (next-state logic, incomplete transitions, design complexity)
- NFA 5-tuple (Q, Σ, q₀, F, δ) component by component
- **Transition function anomaly:** DFA Q×Σ→Q vs NFA Q×Σ→2^Q
- Power set: 2 states → 4 subsets, 3 states → 8 subsets (2^n)

**`Beyond_Determinism.pdf`** — Lec 8–10 only, conceptual. Image-only PDF (OCR'd).
- Determinism = absolute assurance of next state; anatomy of a 1-to-1 deterministic transition → **Lec 8**
- Non-determinism = 1-to-many mapping → **Lec 9**
- NFA execution models: random selection vs parallel execution → **Lec 9**
- **ε (epsilon) jump** — transition without consuming input, NFA only → **Lec 9**
- DFA vs NFA comparison matrix → **Lec 10**

**`Lecture notes 20 nlp-tokenization-spelling-correction-notes.pdf`** (Studocu)
- Tokenization: word / sentence / character / subword with worked examples → **Lec 20**
- *Beyond:* non-word vs real-word errors, dictionary / MED / context correction, MED operations, `kitten→sitting` = 3 (Lec 21, 24)
- **Pages 8–14 contain no content** (footer only).

**`PPT -3 tokenization-multilinguality.pdf`** (Stanford CS224N guest lecture)
- In scope (~slides 5–57) → **Lec 20**: what is a word/morpheme; segmenting into characters/morphemes/words/phrases; tokens, tokenizer, vocabulary, token IDs, embedding lookup; word tokenization pros/cons, Zipf's law, OOV/UNK; character/byte tokenization; subword tokenization — BPE, WordPiece, Unigram LM; **full BPE training walkthrough** ("Peter Piper"); BPE inference by applying merges in order; SentencePiece, SuperBPE
- **Out of syllabus (~slides 58–76):** glitch tokens, multilinguality, cross-lingual transfer, curse of multilinguality, tokenizer fairness/subword fertility, CANINE, MrT5, byte-level architectures
- **Does not cover sentence tokenization at all** — only words/subwords.

---

## 3. Gaps — handout topics ≤ Lec 20 with weak or no coverage

| Lec | Topic | Status | Closest available |
| --- | --- | --- | --- |
| 18 | **Lexicon-Free FSTs** | **Not covered** | No PDF uses the term. In Jurafsky & Martin this is the **Porter stemmer** as a lexicon-free cascade of rules; `NLP-UNIT-1-notes` mentions Porter/Snowball/Lancaster only as stemmer names, not as FSTs. Use T1 Ch. 3.8. |
| 6 | Acceptor/Transducer **"Categorization"** | **Weak** | Acceptor and transducer are both defined (ToC + `PPT-2`), but no PDF covers **Moore vs Mealy** machines or the acceptor/classifier/transducer/sequencer taxonomy. |
| 5 | Overview of models and algorithms in NLP | **Weak** | `NLP-UNIT-1-notes` grammar types + statistical models. J&M's framing (state machines, formal rule systems, logic, probabilistic models) is not laid out anywhere. |
| 3–4 | Knowledge in Speech & Language Processing | **Partial** | `NLP-UNIT-1-notes`' 7 linguistic levels substitutes for it, but J&M's explicit "six kinds of knowledge" list is absent. Ambiguity itself is well covered. |
| 20 | **Sentence** tokenization | **Thin** | Only `NLP-UNIT-1-notes` treats it properly (boundary detection + abbreviations, decimals, ellipsis, quotes). `PPT -3` skips it entirely. Word tokenization is covered heavily by contrast. |

**Strongest coverage:** Lec 8–10 (five overlapping sources) and Lec 11–17 (two dedicated decks).
