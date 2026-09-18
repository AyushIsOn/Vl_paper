# BPM Mid-Term Study Guide

Built from the three uploaded files. All arithmetic below was recomputed independently and matches the slides unless a **⚠ DISCREPANCY** note says otherwise.

## Source inventory

| File | Contents | Coverage |
|---|---|---|
| `BPM half material -compressed.pdf` | 41 photos of a **49-slide** deck (Manipal University — Dr. Sukhwinder Sharma, Dr. Aprna Tripathi, Dr. Neeraj Kumar Verma) | slides ~6–46 |
| `BPM apriori confusion-compressed.pdf` | 48 photos of a **130-slide** deck | slides 44–89 |
| `BPM Addon.pptx` | 31 slides, machine-readable text | Process Models / Petri Nets / Workflow Nets / BPMN |

Both PDFs are photographs of a laptop screen — no text layer, so they were read visually page by page.

---

# NUMERICAL 1 — Decision Tree / ID3

## Formulas (as written in your deck)

$$Info(D) = -\sum_{i=1}^{m} p_i \log_2(p_i)$$

Slides 43–44 make a point of the leading minus sign, and it's a likely short-answer question:
probabilities lie between 0 and 1 → $\log_2$ of a value < 1 is negative → the minus sign flips it, because **information must be positive**.

$$Info_A(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times Info(D_j) \qquad Gain(A) = Info(D) - Info_A(D)$$

Pick the attribute with the **highest Gain** as the split. `Info_A(D)` is the *weighted* entropy — the weights $|D_j|/|D|$ are what students most often drop.

## Worked example A — AllElectronics `buys_computer` (14 tuples, 9 Yes / 5 No)

$Info(D) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} = \mathbf{0.940}$

| Attribute | Partitions (Yes/No) | $Info_A(D)$ | **Gain** |
|---|---|---|---|
| **age** | youth 2/3, middle_aged 4/0, senior 3/2 | 0.694 | **0.246** ← winner |
| income | low 3/1, medium 4/2, high 2/2 | 0.911 | 0.029 |
| student | yes 6/1, no 3/4 | 0.788 | 0.152 |
| credit_rating | fair 6/2, excellent 3/3 | 0.892 | 0.048 |

`age` becomes the root. Note `middle_aged` is 4 Yes / 0 No → entropy 0 → **pure leaf, stop splitting that branch**. Examiners love that detail.

Worked long-hand for age:
$Info_{age}(D)=\frac{5}{14}(0.971)+\frac{4}{14}(0)+\frac{5}{14}(0.971)=0.694$

## Worked example B — Play Tennis (slide 45, 14 days, 9 Yes / 5 No)

Same $Info(D) = 0.940$.

| Attribute | Partitions | $Info_A(D)$ | **Gain** |
|---|---|---|---|
| **Outlook** | Sunny 2/3 (H=0.971), Overcast 4/0 (H=0), Rain 3/2 (H=0.971) | 0.694 | **0.247** ← root |
| Temp | Hot 2/2 (1.0), Mild 4/2 (0.918), Cool 3/1 (0.811) | 0.911 | 0.029 |
| Humidity | High 3/4 (0.985), Normal 6/1 (0.592) | 0.788 | 0.152 |
| Windy | Weak 6/2 (0.811), Strong 3/3 (1.0) | 0.892 | 0.048 |

**Root = Outlook.** Overcast is pure → leaf = Yes.

Notice this dataset is numerically *identical* to AllElectronics (same 9/5 split, same four gain values). Learn one, you have both.

## Slide 42 — the "business conclusion" framing

The deck ties ID3 back to a business narration, and it's likely a viva/short question. Amazon warehouse case: ~15% of orders delivered late; attributes = Order, Stock Available, Payment Verified, Courier Available, Delivery.

Tree: `Payment? → No: Delayed / Yes → Stock? → No: Delayed / Yes → Courier? → Yes: On Time / No: Delayed`

Narration form: **If** Payment Verified **AND** Stock Available **Then** Delivery On Time, **Otherwise** Delivery Delayed.

## Exam template

1. Count the class split → compute $Info(D)$.
2. For each attribute: partition, entropy per partition, weight by $|D_j|/|D|$, sum → $Info_A(D)$.
3. $Gain = Info(D) - Info_A(D)$ for all attributes; pick the max.
4. Any partition with entropy 0 is a leaf; recurse on the rest **using only that subset's rows**.

Handy values: $\log_2$ splits — 2/2→1.000, 3/1→0.811, 4/1→0.722, 4/2→0.918, 5/1→0.650, 6/1→0.592, 2/3→0.971, 3/4→0.985, 9/5→0.940.

---

# NUMERICAL 2 — Apriori / Association Rule Mining

## Your professor's non-standard vocabulary — match it

| Deck's term | Meaning |
|---|---|
| Support = $P(X \cup Y)$, the **"lower bound"** | fraction of transactions containing the itemset; filters **frequent** itemsets |
| Confidence = $P(Y/X)$, the **"upper bound"** | $\dfrac{support(X \cup Y)}{support(X)}$; filters **interesting/strong** rules |

$$Support(X \Rightarrow Y)=\frac{\text{txns containing both}}{\text{total txns}} \qquad Confidence(X \Rightarrow Y)=\frac{support(X \cup Y)}{support(X)} \qquad Lift=\frac{Confidence}{support(Y)}$$

**Apriori property:** every non-empty subset of a frequent itemset must itself be frequent. Contrapositive is the pruning rule — if any $(k-1)$-subset is infrequent, discard the $k$-candidate *without counting it*.

## Worked example — StationeryShop, 10 transactions, min_sup 20% (count ≥ 2), min_conf 30%

| TID | Items | | TID | Items |
|---|---|---|---|---|
| T1 | Bag, Uni, Cry | | T6 | Bag, Pen, Book |
| T2 | Book, Bag, Uni | | T7 | Cry, Uni, Bag |
| T3 | Bag, Uni, Pen | | T8 | Book, Cry, Bag |
| T4 | Bag, Pen, Book | | T9 | Uni, Cry, Pen |
| T5 | Uni, Cry, Bag | | T10 | Pen, Uni, Book |

### Pass 1 — L1
Bag 8, Uni 7, Book 5, Cry 5, Pen 5. All ≥ 2 → all survive.
*(Sanity check: 8+7+5+5+5 = 30 = 10 txns × 3 items. Always do this.)*

### Pass 2 — C2 → L2

| Itemset | Count | Transactions | Verdict |
|---|---|---|---|
| {Bag, Uni} | 5 | T1,T2,T3,T5,T7 | keep |
| {Bag, Cry} | 4 | T1,T5,T7,T8 | keep |
| {Bag, Book} | 4 | T2,T4,T6,T8 | keep |
| {Uni, Cry} | 4 | T1,T5,T7,T9 | keep |
| {Bag, Pen} | 3 | T3,T4,T6 | keep |
| {Book, Pen} | 3 | T4,T6,T10 | keep |
| {Uni, Pen} | 3 | T3,T9,T10 | keep |
| {Uni, Book} | 2 | T2,T10 | keep (exactly at threshold) |
| {Cry, Book} | 1 | T8 | **prune** |
| {Cry, Pen} | 1 | T9 | **prune** |

### Pass 3 — C3 → L3

Pruned by the Apriori property *before counting* (each contains {Cry,Book} or {Cry,Pen}):
{Bag,Cry,Book}, {Bag,Cry,Pen}, {Cry,Book,Pen}, {Cry,Uni,Book}, {Cry,Uni,Pen}

Survived pruning, then counted:

| Candidate | Count | Verdict |
|---|---|---|
| {Bag, Book, Pen} | 2 (T4,T6) | **frequent** |
| {Bag, Cry, Uni} | 3 (T1,T5,T7) | **frequent** |
| {Bag, Uni, Book} | 1 (T2) | below min_sup |
| {Bag, Uni, Pen} | 1 (T3) | below min_sup |
| {Uni, Book, Pen} | 1 (T10) | below min_sup |

**L3 = { {Bag,Book,Pen}, {Bag,Cry,Uni} }**

### Pass 4
Joining the two members of L3 requires the first $k-2 = 2$ items to agree ({Bag,Book} vs {Bag,Cry}) — they don't, so **C4 = ∅ and the algorithm terminates.**

### The True/False question

> *"If a person buys a Uniform then he also buys a School Bag."*

- $support\{Uni, Bag\} = 5/10 = \mathbf{50\%} \ge 20\%$ ✔ (T1, T2, T3, T5, T7)
- $confidence(Uni \Rightarrow Bag) = 5/7 = \mathbf{71.43\%} \ge 30\%$ ✔
- Reverse: $confidence(Bag \Rightarrow Uni) = 5/8 = 62.50\%$ ✔

**Verdict: TRUE** — the rule clears both thresholds.

> **⚠ DISCREPANCY.** The slide justifies this with *"Support for {Book, Uniform} = 20%"*. That is the wrong item pair — {Book, Uni} is a different itemset (count 2 = 20%, T2 and T10). The question asks about **Uniform → School Bag**, whose support is **50%**. The verdict TRUE is unaffected, but quote 50% and list the TIDs. If the intended reading were {Book,Uni} at exactly 20%, it still only *just* meets min_sup and its confidence would be 2/7 = 28.6% — which **fails** min_conf 30%, giving the opposite answer. Worth knowing both readings.

> **Bonus mark — Lift.** $Lift(Uni \Rightarrow Bag) = \frac{0.50}{0.7 \times 0.8} = \mathbf{0.893}$. Below 1, so Uniform and Bag are **slightly negatively correlated** despite the healthy 71% confidence — Bag is simply so common (80%) that buying a Uniform makes it marginally *less* likely than chance. This is the textbook illustration of why confidence alone misleads.

## Exam template

1. Count 1-itemsets → prune below min_sup.
2. **Join** $L_{k-1}$ with itself (first $k-2$ items equal), **prune** any candidate with an infrequent subset, *then* count.
3. Stop when $L_k$ or $C_{k+1}$ is empty.
4. For rules: generate from the largest frequent itemsets, compute confidence, keep those ≥ min_conf. Add lift if asked for "interesting".

Convert percentage min_sup to a **count** immediately (20% of 10 = 2) — mixing the two is the classic error.

---

# NUMERICAL 3 — Confusion Matrix

## ⚠ Your deck's layout is TRANSPOSED vs. sklearn

The slides put **Predicted on the rows, Actual on the columns**:

|  | Actual Positive | Actual Negative |
|---|---|---|
| **Predicted Positive** | **TP** | **FP** |
| **Predicted Negative** | **FN** | **TN** |

Read the axis labels on the exam paper before assigning cells. The mnemonic that survives either layout: the **second letter is what you predicted**, the **first letter says whether you were right**. FP = you *said* positive and were *wrong*.

## Formulas

$$Accuracy=\frac{TP+TN}{TP+TN+FP+FN} \quad Precision=\frac{TP}{TP+FP} \quad Recall=\frac{TP}{TP+FN} \quad F1=\frac{2 \times P \times R}{P+R}$$

- **Precision** — of everything I flagged positive, how much really was? Use when **FP is costly** (spam filter binning a real email).
- **Recall / Sensitivity** — of all real positives, how many did I catch? Use when **FN is costly** (missing a disease). The deck flags the medical case explicitly.
- **F1** — harmonic mean, the go-to for **imbalanced datasets**. Harmonic (not arithmetic) so that one bad component drags the score down.

## Worked example A — slide 86

TP = 560, FP = 60, FN = 50, TN = 330 (N = 1000)

- Accuracy = 890/1000 = **89.00%**
- Precision = 560/620 = **90.32%**
- Recall = 560/610 = **91.80%**
- F1 = 2(0.9032)(0.9180)/(0.9032+0.9180) = **91.06%**

## Worked example B — the imbalanced "sick" case

TP = 30, FP = 30, FN = 10, TN = 930 (N = 1000)

- Accuracy = 960/1000 = **96.00%**
- Precision = 30/60 = **50.00%**
- Recall = 30/40 = **75.00%**
- F1 = **60.00%**

**This is the whole point of the example.** 96% accuracy looks excellent, yet precision is a coin flip: only 40 of 1000 patients are actually sick, so predicting "healthy" for everyone would still score 96%. The **accuracy paradox** — quote it if asked why accuracy is a poor metric on imbalanced data, and reach for F1 instead.

---

# Theory revision — the rest of the syllabus

## DIKW hierarchy
**Data → Information → Knowledge → Wisdom.** Data = raw facts; Information = processed/contextual; Knowledge = patterns and experience applied; Wisdom = judgement about what *should* be done.

## Business process fundamentals
A **business process** is a sequence of activities an organisation performs to reach a goal. Components: **Input → Activities → Resources → Business Rules → Output → Customer**.

Canonical examples in the decks: University Admission (Application → Document Verification → Fee Payment → Admission Approval → Student Registration) and Online Shopping.

## Event logs — the three mandatory fields
| Field | Role | Example |
|---|---|---|
| **Case ID** | one complete process instance | C001 |
| **Activity** | what happened | Verification |
| **Timestamp** | when it happened | 11:15 AM |

**Case = one process instance. Trace = the ordered sequence of activities for that case.** Two cases can share a trace; a rework loop produces a different trace (`Application → Verification → Rework → Approval`).

## Types of process mining
- **Discovery** — event log in, model out, no prior model.
- **Conformance** — compare log against an existing model to find deviations.
- **Enhancement / Extension** — enrich or repair an existing model using the log.

## Process models
A **process model** is a graphical or mathematical representation of how a process works, per the event log. It captures activities, their sequence, decisions, parallelism, conditions, and start/end points.

**Petri Net** — mathematical + graphical notation for sequence, choice, parallelism, synchronisation. Elements: **Places** (circles, states), **Transitions** (rectangles, activities), **Arcs** (directed connections), **Tokens** (dots, the current marking). A transition *fires* when every input place holds a token; firing consumes input tokens and produces output tokens.

**Workflow Net (WF-net)** — a Petri net restricted for business workflows: exactly one **source** place, exactly one **sink** place, and every node on a path from source to sink. **Soundness** = it can always complete, leaves no tokens behind, and has no dead transitions.

**Representational bias** — the chosen notation constrains what you can even express or discover. E.g. a notation with no construct for concurrency will render genuinely parallel behaviour as a tangle of sequences. It's a property of the *language*, not the log.

**BPMN** — the industry-standard business-facing notation (events, activities, gateways, pools/lanes, flows). Readable by non-technical stakeholders; Petri nets are the formally analysable counterpart.

**Dependency graph** — nodes = activities, edges = directly-follows relations, usually with frequencies. Simple and readable but cannot properly express AND/XOR splits.

**Causal net (C-net)** — activities plus explicit input/output **bindings**, expressing causal dependencies with less representational bias than a Petri net.

**Tools: ProM** (open-source, research, plugin-based) and **Disco** (commercial, Fluxicon, fast and user-friendly).

## BI and data mining cycle
Business understanding → Data understanding → Data preparation → Modelling → Evaluation → Deployment. The **data processing chain** moves raw source data through extraction, cleaning, transformation, and aggregation to analysis-ready form. **Dashboards** are the presentation layer — KPIs, trends, drill-down.

## Cluster analysis
**Unsupervised** — no labels, group by similarity. Contrast with classification (decision trees), which is supervised. Partitional (k-means), hierarchical (dendrogram, agglomerative/divisive), density-based (DBSCAN). Evaluation of mining results is where the confusion matrix metrics come back in.

---

# Gaps and cautions

1. **Slides 1–43 of the 130-slide deck were not uploaded.** The Apriori PDF starts at slide 44. If the association-rule theory build-up or a *second* Apriori variant lives in those slides, it isn't here.
2. **Slides 47–49 of the 49-slide deck** are also missing (the half-material PDF ends around slide 46), as are slides 1–5.
3. **The Addon PPTX has 31 slides of which ~15 are diagram-only** (Petri net / workflow net figures with no text layer). I have their titles and structure, but the specific net topologies in those figures were not readable as text. If a Petri-net *drawing* question is likely, review slides 9–13 and 24–26 of that deck yourself.
4. **The {Book, Uniform} vs {Bag, Uniform} slip** documented above — decide before the exam which reading you'd defend.
5. **The transposed confusion matrix** — check the axis labels on the paper.

# Highest-yield things to memorise

- $Info(D)$ for a 9/5 split = **0.940**, and Gain(age)/Gain(Outlook) = **0.246** — both worked datasets share these.
- Entropy of a pure node = **0** → leaf.
- min_sup % → **count** conversion, first thing, every time.
- Apriori pruning happens **before** counting.
- Support = "lower bound", Confidence = "upper bound" (your deck's phrasing).
- Recall for medical / FN-costly; Precision for FP-costly; F1 for imbalanced.
- The accuracy paradox: 96% accuracy, 50% precision.
