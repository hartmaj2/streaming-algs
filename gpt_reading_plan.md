# 📘 SplineSketch Preparation — Reading Plan (TODO)

## 🎯 Goal
Build the **minimum theoretical basis** required to rigorously understand the *SplineSketch* paper.

---

# ✅ 1. Core Foundations (MUST COMPLETE)

## ☐ Chapter 2 — Summaries for Sets
**Purpose:** Understand the *streaming model and abstraction*

- ☐ Understand **summary vs exact computation**
- ☐ Understand operations:
  - ☐ UPDATE
  - ☐ QUERY
  - ☐ MERGE
- ☐ Understand **randomization in summaries**
- ☐ Skim Morris Counter (intuition only)

---

## ☐ Chapter 3 — Summaries for Multisets
**Purpose:** Understand *data representation and heavy hitters*

### Mandatory:
- ☐ Understand **frequency vector model**
  - $v_x = \text{frequency of } x$
- ☐ Understand **multiset as vector**

### Critical:
- ☐ Study **Misra–Gries algorithm**
  - ☐ Space bound: $O(1/\varepsilon)$
  - ☐ Error guarantee: additive error
  - ☐ Why it finds heavy hitters

### Optional:
- ☐ Skim Count-Min / Count Sketch (intuition only)

---

## ☐ Chapter 4 — Summaries for Ordered Data ⭐ (MOST IMPORTANT)
**Purpose:** Directly matches SplineSketch problem

### MUST understand:
- ☐ Rank definition:
  $$
  \text{rank}(x) = \sum_{y < x} v_y
  $$
- ☐ Quantile queries
- ☐ Relationship:
  $$
  \text{CDF}(x) = \frac{\text{rank}(x)}{n}
  $$

### Error guarantees:
- ☐ Understand:
  $$
  \pm \varepsilon n \text{ rank error}
  $$

### Algorithms:
- ☐ Study **GK summary (deterministic)**
- ☐ Study **KLL summary (randomized)**

### Key understanding:
- ☐ Why summaries use **samples**
- ☐ Why resulting CDF is a **step function**

---

# ⚠️ 2. Theoretical Context (IMPORTANT)

## ☐ Chapter 10 — Lower Bounds
**Purpose:** Understand limitations of summaries

- ☐ Understand:
  - ☐ Communication complexity idea
  - ☐ Why summaries need space
- ☐ Key takeaway:
  $$
  \Omega(1/\varepsilon) \text{ space lower bound}
  $$

---

# ⚙️ 3. Optional Deepening

## ☐ Chapter 6 — Vector / Linear Algebra Summaries
**Purpose:** Alternative perspective

- ☐ Vector ↔ frequency distribution equivalence
- ☐ Norm interpretation of summaries
- ☐ Inner product intuition (optional)

---

# ❌ 4. Skip (Not Relevant)

- ☐ Chapter 5 — Geometric summaries
- ☐ Chapter 7 — Graph summaries
- ☐ Chapter 9 — Applications (ANN, etc.)

---

# 🧠 5. Conceptual Checklist (MUST BE ABLE TO ANSWER)

## Fundamentals
- ☐ Why exact quantiles require linear space
- ☐ Why approximation is necessary

## Definitions
- ☐ Define rank and quantile formally
- ☐ Explain ε-error guarantee

## Structural understanding
- ☐ Why summaries are **mergeable**
- ☐ Why GK/KLL use **sampling**

## Insight (critical)
- ☐ Why:
  - sampling → step CDF
  - interpolation → smooth CDF

---

# 🔗 6. Mapping to SplineSketch

## After completing above:

- ☐ Understand SplineSketch as:
  - ☐ Quantile summary (Chapter 4)
  - ☐ + Heavy hitters (Chapter 3)
  - ☐ + Function approximation (NEW)

---

# 🚨 7. Readiness Criteria

You are ready to study SplineSketch iff:

- ☐ You can derive rank/CDF relationship
- ☐ You understand GK/KLL guarantees
- ☐ You understand Misra–Gries guarantees
- ☐ You understand ε-error formally

If any item is missing → STOP and review.

---

# 📌 Final Note

> SplineSketch = classical quantile summary  
> + adaptive partitioning  
> + spline interpolation

Focus on:
- structure
- guarantees
- differences from GK/KLL