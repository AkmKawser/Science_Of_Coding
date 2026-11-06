# Solution Derivation: P-3 - Series Summation: 1 + 3 + 5 + 7 + .............

## 📌 Metadata & Problem Reference
- **Problem ID**: P-3
- **Problem Title**: Series Summation: 1 + 3 + 5 + 7 + .............
- **Primary Category**: Repetitive Structures
- **Subcategory**: Pattern Printing
- **Applied Template**: [`Skills_Input/Templates/Repetitive Structure Template.md`](../../../../../Skills_Input/Templates/Repetitive%20Structure%20Template.md)
- **Problem Statement Link**: [`question bank.md#p-3`](../../../Problem%20Files/question%20bank.md#p-3)
- **Source**: `Recursion Vs Iteration, Part 1 (Series #3)`

---

## 🧠 Phase 1: State Definition & Variable Role Classification

### 1. Variable Discovery & Extraction Analysis
We systematically trace the semantic tokens and arithmetic laws in the problem statement:
- **Linguistic Trigger: *"positive integer $N$ as input"***:
  - Discovered entity: `n`.
  - *Diagnostic Test 1 (Fixed Test)*: `n` is supplied at invocation time and remains completely invariant over the loop lifecycle. Hence, **Fixed**.
- **Linguistic Trigger: *"odd numbers series: $1 + 3 + 5 + 7 + \dots$"***:
  - Discovered entities: `i` (index of the term from $1$ to $N$) and `term` (the actual odd integer generated at index $i$).
  - *Diagnostic Test 2 (Derived Test)* on `term`: Can `term` be expressed as a closed-form formula of current variables without consulting loop history? Yes, $\text{term} = 2i - 1$. Because it is an instantaneous mapping, it requires no state retention or separate loop. Hence, **Derived**.
  - *Diagnostic Test 3 (Free Test)* on `i`: Does `i` traverse an independent arithmetic progression $[1, N]$? Yes, $i$ advances by $+1$ each iteration, controlling the primary domain progression. Hence, **Free** (Stepper).
- **Linguistic Trigger: *"calculate the sum of the series"***:
  - Discovered entity: `total`.
  - *Diagnostic Test 4 (Carried Test)* on `total`: Does `total` require passing its value across iteration boundaries? Yes, $\text{total}_i = \text{total}_{i-1} + (2i - 1)$. Without preserving `total` across iterations, intermediate sums are lost. Hence, **Carried** (Gatherer).

### 2. Candidate Variables Inventory
- `n`: Total number of terms in the sequence (given input parameter).
- `i`: Current iteration counter / index of the term ($1 \le i \le n$).
- `term`: Value of the $i$-th term in the odd-integer sequence ($\text{term} = 2i - 1$).
- `total`: Running cumulative sum of all terms from term $1$ through term $i$.

### 3. Variable Roles & Classification Table

| Variable | Role | Class | Justification & Lifecycle |
| :--- | :--- | :--- | :--- |
| `n` | Fixed Value | **Fixed** | Given once via standard input; remains unchanged throughout execution. |
| `i` | Stepper | **Free** | Enumerates discrete values across $[1, n]$; requires its own loop. |
| `term` | Derived Value | **Derived** | Mathematical formula $\text{term} = 2i - 1$; computed fresh on the fly, needs no loop. |
| `total` | Gatherer | **Carried** | Accumulates successive terms: $\text{total}_{\text{new}} = \text{total}_{\text{old}} + (2i - 1)$; maintained across iterations. |

### 4. True Minimal State Formulation
Filtering out fixed context variables and derived instant values, the minimal "pause-and-resume note" (state tuple) is:

$$\text{State} = (i, \text{total})$$

- **Free variable**: $i$ (controls progression)
- **Carried variable**: $\text{total}$ (accumulates result across iterations)

**Loop Requirement**: Since there is **exactly 1 free variable** ($i$), the problem requires **exactly 1 loop**.

---

## 🌲 Phase 2: State-Space & Relationship Derivation

### 1. Loop Bounds & Arithmetic Intervals
- Lower Bound: $i_{\text{start}} = 1$
- Upper Bound: $i_{\text{end}} = n$
- Step Increment: $\Delta i = +1$
- Total Iterations / Steps: $n - 1 + 1 = n$
- Term Generation Rule: $\text{term}_i = 2i - 1$

### 2. State-Space Tree (Linear Trace for $n = 5$)

```
                   Root (Start: i=1, total=0)
                            │
               ┌────────────┴────────────┐
             i = 1       term = 1     total = 1  ───> Print "1"
               │
             i = 2       term = 3     total = 4  ───> Print "3"
               │
             i = 3       term = 5     total = 9  ───> Print "5"
               │
             i = 4       term = 7     total = 16 ───> Print "7"
               │
             i = 5       term = 9     total = 25 ───> Print "9"
                            │
                      Leaf (End: i=5)
                 Final Output: "Sum = 25"
```

---

## ⚖️ Phase 3: Mathematical Invariant Formulation

### 1. Loop Invariant
At the start of each iteration with counter index $i \in [1, n + 1]$:
$$\text{total} = \sum_{k=1}^{i-1} (2k - 1) = (i - 1)^2$$

### 2. Inductive Verification Steps
- **Initialization ($i = 1$)**:
  $$\text{total} = (1 - 1)^2 = 0$$
  Matches the initial accumulator state prior to executing the first iteration.
- **Maintenance ($i \to i + 1$)**:
  Assume invariant holds before iteration $i$: $\text{total} = (i - 1)^2$.
  During iteration $i$, the term $2i - 1$ is evaluated and added:
  $$\text{total}' = \text{total} + (2i - 1) = (i - 1)^2 + 2i - 1 = (i^2 - 2i + 1) + 2i - 1 = i^2 = ((i + 1) - 1)^2$$
  The property holds for index $i + 1$.
- **Termination ($i = n + 1$)**:
  The loop terminates immediately when $i = n + 1$. Substituting into the invariant:
  $$\text{total} = ((n + 1) - 1)^2 = n^2 = \sum_{k=1}^{n} (2k - 1)$$
  The computed value is mathematically exact for the sum of the first $n$ positive odd integers ($n^2$).

---

## 🔍 Phase 4: Boundary Audits & Failure Mode Checks

| Edge / Boundary Case | Expected Behavior | Code Handling |
| :--- | :--- | :--- |
| **Minimum Bound ($N = 1$)** | Single term `1` printed; `Sum = 1`. | Loop runs once for $i=1$; $\text{total} = 1^2 = 1$. Handled correctly. |
| **Empty / Invalid Input ($N \le 0$)** | Handled by problem constraints ($1 \le N \le 10^4$). | Guarded by early return on empty input. |
| **Maximum Bound ($N = 10^4$)** | $\text{total} = (10^4)^2 = 10^8 = 100,000,000$. | Fits comfortably in 32-bit signed integer ($\approx 2.14 \times 10^9$). Java uses explicit `long` to prevent any overflow. |
| **Whitespace Formatting** | Strictly space-separated terms with no trailing space. | Python uses `" ".join(terms)`; Java uses `StringBuilder` with conditional separator. |

---

## ⏱️ Phase 5: Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$
  - Total leaves in the linear execution tree: $N$.
  - Each step carries out $\mathcal{O}(1)$ arithmetic and string formatting operations.
- **Auxiliary Space Complexity**: $\mathcal{O}(1)$
  - Only two scalar registers (`i` and `total`) are maintained in memory across the loop.

