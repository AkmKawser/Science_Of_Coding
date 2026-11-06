# Solution Derivation: P-001 - Series Summation: 1 + 2 + 3 + 4 + .............

## 📌 Metadata & Problem Reference
- **Problem ID**: P-001
- **Problem Title**: Series Summation: 1 + 2 + 3 + 4 + .............
- **Primary Category**: Repetitive Structures
- **Subcategory**: Pattern Printing
- **Applied Template**: [`Skills_Input/Templates/Repetitive Structure Template.md`](../../../../Skills_Input/Templates/Repetitive%20Structure%20Template.md)
- **Problem Statement Link**: [`question bank.md#p-001`](../../Problem%20Files/question%20bank.md#p-001)
- **Source**: `Recursion Vs Iteration, Part 1 (Series #1)`

---

## 🧠 Phase 1: State Definition & Variable Role Classification

### 1. Candidate Variables Inventory
- `n`: Total number of terms to generate and sum (given input).
- `i`: Current iteration counter / index of the term being generated.
- `term`: The value of the $i$-th element in the sequence ($i$).
- `total`: Running cumulative sum of all terms from $1$ up to the current term $i$.

### 2. Variable Roles & Classification Table

| Variable | Role | Class | Justification & Lifecycle |
| :--- | :--- | :--- | :--- |
| `n` | Fixed Value | **Fixed** | Read once from standard input; unchanging throughout loop execution. |
| `i` | Stepper | **Free** | Enumerates discrete values across range $[1, n]$; requires its own loop. |
| `term` | Derived Value | **Derived** | Trivial direct identity $\text{term} = i$; no separate loop needed. |
| `total` | Gatherer | **Carried** | Accumulates successive terms: $\text{total}_{\text{new}} = \text{total}_{\text{old}} + i$; must be retained across iterations. |

### 3. True Minimal State Formulation
Filtering out fixed and derived variables, the minimal resume-note (state tuple) required to pause and continue execution is:

$$\text{State} = (i, \text{total})$$

- Free variable: $i$
- Carried variable: $\text{total}$

Because there is **exactly 1 free variable** ($i$), this algorithm requires **exactly 1 loop**.

---

## 🌲 Phase 2: State-Space & Relationship Derivation

### 1. Loop Bounds & Arithmetic Intervals
- Lower Bound: $i_{\text{start}} = 1$
- Upper Bound: $i_{\text{end}} = n$
- Step Size: $\Delta i = +1$
- Total Iterations: $n - 1 + 1 = n$

### 2. State-Space Tree (Linear Trace for $n = 5$)

```
                   Root (Start: i=1, total=0)
                            │
               ┌────────────┴────────────┐
             i = 1                   total = 1  ───> Print "1"
               │
             i = 2                   total = 3  ───> Print "2"
               │
             i = 3                   total = 6  ───> Print "3"
               │
             i = 4                   total = 10 ───> Print "4"
               │
             i = 5                   total = 15 ───> Print "5"
                            │
                      Leaf (End: i=5)
                 Final Output: "Sum = 15"
```

---

## ⚖️ Phase 3: Mathematical Invariant Formulation

### 1. Loop Invariant
At the start of each iteration with counter $i \in [1, n + 1]$:
$$\text{total} = \sum_{k=1}^{i-1} k = \frac{(i - 1) \cdot i}{2}$$

### 2. Verification Steps
- **Initialization ($i = 1$)**:
  $$\text{total} = \sum_{k=1}^{0} k = 0$$
  The accumulator is correctly initialized to neutral value $0$.
- **Maintenance ($i \to i + 1$)**:
  Before step $i$, $\text{total} = \frac{(i - 1)i}{2}$. During the iteration, the term $i$ is added:
  $$\text{total}' = \frac{(i - 1)i}{2} + i = \frac{i(i - 1 + 2)}{2} = \frac{i(i + 1)}{2}$$
  The invariant holds for index $i + 1$.
- **Termination ($i = n + 1$)**:
  Loop stops when $i = n + 1$. Substituting into the invariant:
  $$\text{total} = \frac{n(n + 1)}{2} = \sum_{k=1}^{n} k$$
  The computed value exactly matches the mathematical sum of the arithmetic series.

---

## 🔍 Phase 4: Boundary Audits & Failure Mode Checks

| Edge / Boundary Case | Expected Behavior | Code Handling |
| :--- | :--- | :--- |
| **Minimum Bound ($N = 1$)** | Output single term `1` and `Sum = 1`. | Loop runs exactly once ($i=1$); correct. |
| **Empty / Zero Input ($N \le 0$)** | Empty sequence or termination. | Guarded by problem constraints $1 \le N \le 10^4$. |
| **Maximum Bound ($N = 10^4$)** | $\text{total} = \frac{10^4 \cdot 10001}{2} = 50,005,000$. | Fits within 32-bit signed integer ($\approx 2 \times 10^9$ limit). In Java, `long` is explicitly used for safety. |
| **Whitespace Formatting** | Terms space-separated; no trailing spaces. | Handled via `" ".join()` in Python and `StringBuilder` in Java. |

---

## ⏱️ Phase 5: Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$
  - Total leaves in the state-space tree: $N$.
  - Each iteration performs $\mathcal{O}(1)$ arithmetic additions and string formatting operations.
- **Auxiliary Space Complexity**: $\mathcal{O}(1)$
  - Only two scalar registers (`i` and `total`) are maintained throughout the iteration.

