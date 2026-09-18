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

# Syllabus coverage audit

Every syllabus line checked against what is actually in the three files. **✅ = in your material. ⚠️ = thin/implicit. ❌ = absent.**

| # | Syllabus topic | Status | Where |
|---|---|---|---|
| 1 | Types of Process Mining | ✅ solid | Half deck **15–18** (Discovery / Conformance Checking / Enhancement, with the Event Logs→Model→Diagnostics flowchart); Addon **24–25** |
| 2 | Introduction to business intelligence | ✅ solid | Half deck **20** (BI definition), **21** (BI Architecture + Components of BI) |
| 3 | Decision Trees | ✅ **very strong** | Half deck **22–46**, incl. two full ID3 numericals |
| 4 | Association Rule Learning | ✅ **very strong** | Apriori deck **44–76**, two full worked examples |
| 5 | **Cluster Analysis** | ❌ **ABSENT** | Not in any of the three files |
| 6 | Evaluation of Mining Results | ⚠️ partial | Apriori deck **77–89** = confusion matrix + accuracy/precision/recall/F1 only. No cross-validation, holdout, ROC/AUC, or cluster-validity content |
| 7 | BI and data mining cycle | ⚠️ partial | Half deck **19** (7-step BPM workflow: Information Systems → Generate Event Logs → Data Cleaning → Process Mining Algorithms → Model Discovery → Performance Analysis → Process Improvement) and **21**. No CRISP-DM-style cycle slide |
| 8 | Dashboards | ⚠️ **mention only** | One box in the BI architecture (half deck **21**, step 6) and the Disco interface (Addon **26**). No dedicated slide |
| 9 | Data processing chain | ⚠️ implicit | Same two pipelines as #7. Nothing *titled* "data processing chain" |
| 10 | Preparing/Aggregating/Generating Event Logs | ✅ mostly | Half deck **13–14** (event log + Case ID/Activity/Timestamp/**Resource** example); Addon **4–6**; Addon **25** step 1 "prepare the event log (cleaning, sorting, standardization)". "Aggregating" is never its own slide |
| 11 | Petri Nets | ✅ solid | Addon **7–13** |
| 12 | Workflow Nets | ✅ solid | Addon **14–23**, incl. WF-net definition and 7 benefits |
| 13 | Process Model Notations | ⚠️ implicit | No slide by that title, but covered in effect by the four notations below + the "same process, four views" comparison on Addon **28** |
| 14 | Process Discovery Algorithms | ✅ solid | Addon **24–25**: **Alpha Miner** (earliest; sequence, choice, parallelism), **Heuristics Miner** (frequency, handles noise), **Inductive Miner** (recursive, sound models), **Fuzzy Miner** (simplifies complex models) |
| 15 | ProM and Disco | ✅ solid | Addon **26** — both workflows, 5-step procedures, interface mock-ups, loan-approval example |
| 16 | Representational Bias | ✅ solid | Addon **28** |
| 17 | BPMN | ✅ solid | Addon **29** — Event / Activity / Gateway / Sequence Flow / Message Flow + admission example |
| 18 | Dependency Graphs | ✅ solid | Addon **30** |
| 19 | Causal Nets | ✅ solid | Addon **31** |

**Verdict: 13 of 19 solidly covered, 5 thin, 1 completely missing.** Both mid-term units are represented and all three numericals are fully supported. The one real hole is **Cluster Analysis**.

---

# Theory revision

> **Provenance note.** Sections marked **[slides]** are taken from your uploaded material. Sections marked **[added]** are standard course content I supplied to fill a syllabus gap — your lecturer may treat these differently, so verify before relying on them.

## DIKW hierarchy **[slides]**
**Data → Information → Knowledge → Wisdom.** Data = raw facts; Information = processed/contextual; Knowledge = patterns and experience applied; Wisdom = judgement about what *should* be done.

## Business process fundamentals **[slides]**
A **business process** is a sequence of activities an organisation performs to reach a goal. Components: **Input → Activities → Resources → Business Rules → Output → Customer**.

Canonical examples in the decks: University Admission (Application → Document Verification → Fee Payment → Admission Approval → Student Registration) and Online Shopping.

**Need for Business Process Analysis** (half deck 12) — organisations need continuous evaluation, asking: Where are delays occurring? Which activity consumes the most time? Which employee performs best? Where are bottlenecks? Which process should be automated? *Answering these requires Process Analysis, which leads to Business Process Mining.*

**Business Process Mining** = a **data-driven technique** that discovers, monitors and improves business processes using **event logs** generated by information systems. The event log is its **primary data source**.

## Business Intelligence **[slides]**
**BI** = the process of **collecting, storing, analyzing and presenting business data to support informed decision-making** — it turns *business historical data* into *decision-making ability*.

**BI Architecture (7 stages, half deck 21):**
`Data Sources → ETL (Extract, Transform, Load) → Data Warehouse → Data Mining → Reports → Dashboards → Decision Making`

**Components of BI:** Operational Databases, ETL, Data Warehouse, **OLAP**, Data Mining, Dashboards & Reports, Business Decisions.

This 7-stage pipeline is the closest thing in your material to both the "data processing chain" and the "BI and data mining cycle" — if either is asked, reproduce this chain.

**Data Science vs Process Mining mapping (half deck 19)** — a likely 2-mark table:

| Data Science | Process Mining |
|---|---|
| Data Collection | Event Logs |
| Data Cleaning | Log Preprocessing |
| Machine Learning | Predictive Process Mining |
| Visualization | Process Maps |
| Analytics | Performance Analysis |
| Artificial Intelligence | Process Automation |

## Event logs — the three mandatory fields **[slides]**
| Field | Role | Example |
|---|---|---|
| **Case ID** | one complete process instance | C001 |
| **Activity** | what happened | Verification |
| **Timestamp** | when it happened | 11:15 AM |

**Case = one process instance. Trace = the ordered sequence of activities for that case.** Two cases can share a trace; a rework loop produces a different trace (`Application → Verification → Rework → Approval`).

## Types of process mining **[slides]**

The deck's flowchart: `Event Logs → Process Discovery → Process Model →` then either `Conformance Checking → Diagnostics` or `Enhancement → New Process Model`.

1. **Process Discovery** — creates process models automatically from event logs. **Input:** Event Log. **Output:** Business Process Model. (Learn it in exactly this input/output form — that's how the slide states it.)
2. **Conformance Checking** — compares the **discovered** process with the organisation's **predefined** process. Purpose: detect deviations, ensure compliance, identify unauthorised activities. Slide example: expected `Application → Verification → Approval → Payment` vs actual `Application → Payment → Approval` ⇒ **deviations identified**.
3. **Process Enhancement** — improves an existing process using insights from event logs. Purpose: reduce delays, improve performance, optimise resources, increase efficiency.

## Process discovery algorithms **[slides]**

| Algorithm | Characteristic |
|---|---|
| **Alpha Miner** | Earliest algorithm; discovers sequence, choice, parallelism from causal relations |
| **Heuristics Miner** | Uses frequency/dependency info; **handles noise** in real logs |
| **Inductive Miner** | Recursively splits the log, builds a **process tree**; guarantees **sound** models |
| **Fuzzy Miner** | Simplifies complex models by showing only the main behaviour |

What discovery can find: sequence, choice/decision, parallelism, **loops/rework**, and skipped/uncommon behaviour.

**ProM** — open-source, plugin-based framework (import XES/CSV → choose plugin → configure → run → analyse); ideal for research and in-depth analysis. **Disco** — commercial (Fluxicon), auto-generates a process map, filter/drill-down, performance analysis, export reports; best for business users and fast exploration.

## Process models
A **process model** is a graphical or mathematical representation of how a process works, per the event log. It captures activities, their sequence, decisions, parallelism, conditions, and start/end points.

**Petri Net** — mathematical + graphical notation for sequence, choice, parallelism, synchronisation. Elements: **Places** (circles, states), **Transitions** (rectangles, activities), **Arcs** (directed connections), **Tokens** (dots, the current marking). A transition *fires* when every input place holds a token; firing consumes input tokens and produces output tokens.

**Workflow Net (WF-net)** — a Petri net restricted for business workflows: exactly one **source** place, exactly one **sink** place, and every node on a path from source to sink. **Soundness** = it can always complete, leaves no tokens behind, and has no dead transitions.

**WF-net benefits (Addon 21):** clear formal model; supports correctness and performance analysis; detects **deadlocks and bottlenecks**; ensures proper start and completion; useful for automation; widely used in process mining tools.

## The four types of process models **[slides]**

### 1. Representational Bias (Addon 28)
*Different process models represent the same reality in different ways; this difference in representation is called representational bias.* The same process can be modelled in different notations and structures; **each notation highlights certain aspects and hides others**, which biases how we perceive and analyse the process. The slide shows **one process in four views** — BPMN, Petri Net, Process Tree, Dependency Graph. **Key takeaway: no single model is complete; the choice of notation depends on purpose and audience.**

### 2. BPMN (Addon 29)
A standard notation for modelling business processes graphically and understandably, used by **both business users and technical teams**.

| Symbol | Element | Meaning |
|---|---|---|
| Circle | **Event** | Something that happens (start, end) |
| Rounded rectangle | **Activity** | A task or work |
| Diamond | **Gateway** | A decision or branching |
| Solid arrow | **Sequence Flow** | Order of activities |
| Dashed arrow | **Message Flow** | Communication between pools |

Slide example — admission: `Start → Submit Application → Verify Documents → [Documents OK?] → No: Request Correction (loops back) / Yes: Fee Payment → Admission Approval → End`.

### 3. Dependency Graphs (Addon 30)
Show relationships and dependencies between activities — which must occur before or after others. **Nodes = activities; edges = dependency relations** (sequence, precedence, concurrency). Useful for analysing process structure and detecting parallel or dependent tasks.

Slide example: A (Application) → B (Verification) → then **C (Payment) and D (Approval) in parallel** → both required before E (Registration).

### 4. Causal Nets (Addon 31)
**Causal nets extend Petri nets by adding causal relations between events**, representing causality, concurrency and choice. Features: model causal relations (not just sequence), capture concurrency and choice, **more expressive than traditional Petri nets**, suited to complex real-world processes. Same A–E example, annotated `A causes B`, `B causes C`, `B causes D`, `C and D cause E`.

## Cluster analysis **[added — NOT in your uploaded material]**
> Your syllabus lists this but **none of the three files covers it.** Treat the following as a minimal safety net and get the real slides.

**Unsupervised** — no labels; group records by similarity. Contrast with classification (decision trees), which is **supervised**. Main families: **partitional** (k-means — choose k, assign to nearest centroid, recompute, repeat), **hierarchical** (dendrogram; agglomerative bottom-up or divisive top-down), **density-based** (DBSCAN — finds arbitrary shapes, labels outliers). In process mining it is used for **trace clustering**: grouping similar cases so each cluster can be mined into a simpler, more comprehensible model.

---

# Gaps and cautions

1. **Cluster Analysis is entirely missing** from all three files despite being on the syllabus. Biggest hole — get those slides.
2. **Evaluation of Mining Results is only half-covered** — you have the confusion matrix, but nothing on cross-validation, holdout/train-test split, or ROC/AUC. If the syllabus phrase is broader than the confusion matrix, you're exposed.
3. **Dashboards and the data processing chain** appear only as boxes inside the BI architecture pipeline. Enough for a 2-mark mention, thin for a 5-mark answer.
4. **Slides 1–43 of the 130-slide deck were not uploaded** (the Apriori PDF starts at slide 44). Cluster analysis and the BI cycle may well live there — worth checking before assuming they were never taught.
5. **Slides 47–49 of the 49-slide deck** are missing (that PDF ends at ~46), as are slides 1–5.
6. **The {Book, Uniform} vs {Bag, Uniform} slip** documented above — decide which reading you'd defend.
7. **The transposed confusion matrix** — check the axis labels on the paper.

# Highest-yield things to memorise

- $Info(D)$ for a 9/5 split = **0.940**, and Gain(age)/Gain(Outlook) = **0.246** — both worked datasets share these.
- Entropy of a pure node = **0** → leaf.
- min_sup % → **count** conversion, first thing, every time.
- Apriori pruning happens **before** counting.
- Support = "lower bound", Confidence = "upper bound" (your deck's phrasing).
- Recall for medical / FN-costly; Precision for FP-costly; F1 for imbalanced.
- The accuracy paradox: 96% accuracy, 50% precision.
