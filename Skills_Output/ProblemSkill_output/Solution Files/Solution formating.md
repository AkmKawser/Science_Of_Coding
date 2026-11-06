# Problem Solution Output Formatting Specification (`Solution formating.md`)

This document defines the strict, required architecture and formatting standards for algorithmic solutions generated in **`ProblemSkill_output/Solution Files/`**.

---

## 🏛️ Directory & Folder Architecture

All solutions are organized into a clean 2-level directory tree matching the **Primary Category** and **Subcategory** defined in [`problem catagories.docx`](../Problem%20Files/problem%20catagories.docx).

### Hierarchy:
```
Skills_Output/ProblemSkill_output/Solution Files/
└── <Primary Category>/
    └── <Subcategory>/
        └── <Problem-ID>/                 # Dedicated folder for each problem
            ├── <Problem-ID>_python.py       # Standalone, runnable Python 3 solution
            ├── <Problem-ID>_java.java       # Standalone, runnable Java 21 solution
            └── <Problem-ID>_derivation.md   # Step-by-step template derivation & mathematical proof
```

### Folder Naming Guidelines:
- Primary category and subcategory folder names correspond directly to the classification in `question bank.md` and `problem catagories.docx`:
  - E.g., `Repetitive Structures/Pattern Printing/P-1/`
  - E.g., `Two Pointers & Sliding Window/Variable-Size Window/P-10/`
  - E.g., `Dynamic Programming/2D Grid & Interval DP/P-25/`
  - E.g., `Graph Algorithms/Shortest Paths (SSSP)/P-50/`

---

## 🏷️ File Naming Conventions

The file names are strictly based on the unpadded **Problem ID** from [`question bank.md`](../Problem%20Files/question%20bank.md) (formatted without leading zeroes, e.g., `P-1`, `P-2`, `P-10`):

| Artifact | File Naming Pattern | Concrete Example (`P-1`) |
| :--- | :--- | :--- |
| **Python Solution** | `<Problem-ID>_python.py` | `P-1_python.py` |
| **Java Solution** | `<Problem-ID>_java.java` | `P-1_java.java` |
| **Derivation Document** | `<Problem-ID>_derivation.md` | `P-1_derivation.md` |

> [!IMPORTANT]
> The Python and Java solution files are distinct and kept completely separate to ensure full independence and language-idiomatic syntax.

---

## 📋 Derivation Document Schema (`<Problem-ID>_derivation.md`)

Every derivation file must rigorously execute the phased steps defined in the matching template under [`Skills_Input/Templates/`](../../../Skills_Input/Templates/) (e.g., [`Repetitive Structure Template.md`](../../../Skills_Input/Templates/Repetitive%20Structure%20Template.md)):

```markdown
# Solution Derivation: [Problem ID] - [Problem Title]

## 📌 Metadata
- **Problem ID**: [e.g., P-1]
- **Category**: [Primary Category]
- **Subcategory**: [Subcategory]
- **Applied Template**: [`Skills_Input/Templates/<Template Name>.md`](../../../Skills_Input/Templates/)
- **Problem Reference**: [`question bank.md#<problem-id-lowercase>`](../../Problem%20Files/question%20bank.md#p-1)

---

## 🧠 Phase 1: State Definition & Role Classification
1. **Variable Discovery & Extraction Analysis**:
   - **Textual Triggers & Raw Entities**: Detailed narrative trace of how words, mathematical formulas, and constraints in the problem statement led to candidate variables.
   - **Diagnostic Decision Tree Verification**: Step-by-step application of the 4 diagnostic tests for each variable:
     - **Fixed Test**: Does it change during execution?
     - **Derived Test**: Is it purely a function of other existing variables at the current step without memory of previous steps?
     - **Free Test**: Does it advance independently along an arithmetic range or coordinate axis to dictate a loop iteration space?
     - **Carried Test**: Does its current value depend strictly on its value from the prior iteration (accumulated/maintained across time)?
2. **Candidate Variables Inventory**: All variables considered.
3. **Variable Roles Table**:
   | Variable | Role | Class (Free / Carried / Derived / Fixed) | Justification & Lifecycle |
   | :--- | :--- | :--- | :--- |
4. **True Minimal State**:
   $$\text{State} = (\text{Free Variables}, \text{Carried Variables})$$
   - Explicitly justify why Free and Carried variables form the minimal state (the "Pause-and-Resume Note") while Fixed and Derived variables are excluded.
   - State the exact loop count based on the number of Free variables.

---

## 🌲 Phase 2: State-Space & Relationship Derivation
1. **Relationship Mapping**: Dependencies between outer and inner loops.
2. **State-Space Tree Diagram**: High-resolution graphical image diagram (`<Problem-ID>_state_space_tree.png`) representing state transitions, action branches, and termination leaf.
   - **Explicit Tree Type**: Both the derivation document and the rendered graphical image diagram must explicitly declare the tree type (e.g. `Type 1: Linear Chain / Degenerate Tree (b = 1)` for single loops, `Type 2: Hierarchical 2D Coordinate Tree (Nested Loops)` for matrix/patterns, or `Type 3: Binary Decision Tree (b = 2)` for choice/backtracking).
   > [!IMPORTANT]
   > State-space trees must NEVER be text or ASCII art diagrams. They must be generated as graphical images (`.png`) and linked using Markdown image tags: `![<Problem-ID> State-Space Tree Trace](<Problem-ID>_state_space_tree.png)`.
3. **Loop Bounds & Iteration Spaces**: Formal arithmetic intervals for every stepper/walker.

---

## ⚖️ Phase 3: Mathematical Invariant Formulation
- **Initialization Invariant**: Invariant holds before entering the loop.
- **Maintenance Invariant**: Invariant holds across every iteration.
- **Termination Invariant**: Guarantees correct output when loop terminates.

---

## 🔍 Phase 4: Boundary Audits & Failure Mode Checks
- Check empty / minimum inputs ($N=0, 1$).
- Check maximum input limits.
- Check off-by-one errors and edge configurations.

---

## ⏱️ Phase 5: Complexity Analysis
- **Time Complexity**: Exact leaf count calculation and Big-O notation.
- **Space Complexity**: Auxiliary memory and state footprint.
```

---

## 🐍 Python Solution Standards (`<Problem-ID>_python.py`)

- **Language Version**: Python 3.10+
- **Input Handling**: Fast I/O (`sys.stdin.read` or `sys.stdin.readline`).
- **Structure**:
  - Top docstring with Problem ID, Title, and Complexity bounds.
  - Core algorithmic function adhering strictly to the minimal state.
  - `if __name__ == "__main__":` runner handling competitive programming test execution.

```python
"""
Problem ID: P-1
Problem Title: Sum of Numbers from 1 to N
Category: Repetitive Structures / Linear Accumulation
Template: Skills_Input/Templates/Repetitive Structure Template.md
Complexity: Time O(N), Space O(1)
"""

import sys

def solve() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    # State: (i, total) where i is Stepper (Free), total is Gatherer (Carried)
    total = 0
    for i in range(1, n + 1):
        total += i
    
    print(total)

if __name__ == "__main__":
    solve()
```

---

## ☕ Java Solution Standards (`<Problem-ID>_java.java`)

- **Language Version**: Java 21
- **Input Handling**: Fast reading (`BufferedReader`, `StringTokenizer`).
- **Structure**:
  - Class named cleanly (e.g., `Main` or `P1_Solution`).
  - Strict type safety, 64-bit integer handling (`long` where sum can overflow 32-bit int).
  - Explicit comments referencing state variables and invariant checkpoints.

```java
/**
 * Problem ID: P-1
 * Problem Title: Sum of Numbers from 1 to N
 * Category: Repetitive Structures / Linear Accumulation
 * Template: Skills_Input/Templates/Repetitive Structure Template.md
 * Complexity: Time O(N), Space O(1)
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int n = Integer.parseInt(line.trim());
        
        // State: (i, total) where i is Stepper (Free), total is Gatherer (Carried)
        long total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        
        System.out.println(total);
    }
}
```

---

## 🔄 Linkage with Question Bank

Whenever a problem in `question bank.md` is solved:
1. The derivation file is written to `Skills_Output/ProblemSkill_output/Solution Files/<Category>/<Subcategory>/<ID>_derivation.md`.
2. The independent Python file is placed at `<ID>_python.py`.
3. The independent Java file is placed at `<ID>_java.java`.
4. The entry in `question bank.md` can optionally link directly to its solution folder.

