---
name: cpbook4
description: Complete algorithmic knowledge base, data structures, and reference skill. Provides algorithms, data structures, paradigms, problem decomposition, code patterns, and direct page-level reference querying capabilities.
---

# Algorithmic Engineering Skill (`cpbook4`)

This skill embeds comprehensive algorithmic domain knowledge, conceptual depth, algorithm implementations, and problem-solving methodologies for computer science and software engineering.

It is structured to be completely **agent-agnostic**—fully functional with any agentic AI system (Antigravity, Claude Code, Cursor, Copilot, ChatGPT, or custom LLM harnesses).

---

## 1. Skill Capabilities & Core References

The skill directly references the reference library stored in this repository:
1. **Foundations & Core Algorithms (`skill/books/Overall/Part-1.pdf`)**: 329 pages.
   - Fundamentals, problem types, time/space complexity analysis.
   - Built-in & custom linear and non-linear data structures (UFDS, Fenwick Tree, Segment Tree).
   - Core paradigms: Complete Search, Divide and Conquer, Greedy, Dynamic Programming.
   - Graph algorithms: Traversals (DFS/BFS), MST, SSSP (Dijkstra, Bellman-Ford), APSP (Floyd-Warshall), Special Graphs (DAG, Tree, Bipartite, Eulerian).
2. **Advanced Systems & Mathematics (`skill/books/Overall/Part-2.pdf`)**: 352 pages.
   - Mathematics: Number theory (Primes, Sieve, GCD/LCM, Modular arithmetic, Extended Euclidean), Combinatorics, Probability, Game theory, Matrix power.
   - String Processing: Edit distance, LCS, KMP, Suffix Trie/Tree/Array, Rabin-Karp hashing, Manacher.
   - Computational Geometry: Points, lines, circles, polygons, Convex Hull (Graham scan, Monotone chain), 3D geometry.
   - Advanced Topics: Advanced Search & State-Space search, Advanced DP optimizations, Network Flow (Edmonds-Karp, Dinic, modeling), Bipartite Matching (MCBM), NP-hard problem handling, Problem Decomposition.
   - Rare Topics: Sliding window, Sparse Table, Square Root Decomposition, Heavy-Light Decomposition (HLD), LCA, Tree Isomorphism, FFT/NTT, Pollard's rho, Chinese Remainder Theorem, Lucas' Theorem, Simplex Linear Programming, Hungarian algorithm, Edmonds' Blossom.

---

## 2. Fast Navigation & Reference Map

Agents should consult the detailed topic mapping located at:
- [`references/table_of_contents.md`](references/table_of_contents.md)
- [`references/toc_book1.json`](references/toc_book1.json)
- [`references/toc_book2.json`](references/toc_book2.json)

### Core Algorithm Decision Matrix

| Problem Trait / Constraint | Recommended Data Structure / Paradigm | Reference Chapter |
| :--- | :--- | :--- |
| Static range minimum/sum queries ($O(1)$ query, $O(N \log N)$ prep) | **Sparse Table** | Volume 2, Ch 9.3 |
| Dynamic point updates + Range sum queries ($O(\log N)$) | **Fenwick (Binary Indexed) Tree** | Volume 1, Ch 2.4.3 |
| Dynamic range updates + Range queries ($O(\log N)$) | **Segment Tree with Lazy Propagation** | Volume 1, Ch 2.4.4 |
| Disjoint sets, cycle detection in undirected graphs | **Union-Find Disjoint Sets (UFDS)** | Volume 1, Ch 2.4.2 |
| Shortest path with non-negative edge weights | **Dijkstra's Algorithm** | Volume 1, Ch 4.4.2 |
| Shortest path with negative weight cycles | **Bellman-Ford / SPFA** | Volume 1, Ch 4.4.3 |
| Substring search, repeated occurrences | **KMP Algorithm / Rolling Hash** | Volume 2, Ch 6.4, 6.6 |
| All substring queries, LCP, lexicographical order | **Suffix Array + Kasai's LCP** | Volume 2, Ch 6.5 |
| Maximum matching in bipartite graphs | **Hopcroft-Karp / Dinic Flow** | Volume 2, Ch 8.4, 9.26 |
| Fast polynomial multiplication, string matching with wildcards | **Fast Fourier Transform (FFT / NTT)** | Volume 2, Ch 9.11 |
| Tree path queries / updates | **Heavy-Light Decomposition (HLD)** | Volume 2, Ch 9.5 |
| $N \le 20$, exhaustive subset state transition | **Bitmask Dynamic Programming** | Volume 2, Ch 8.3.1 |
| $N \approx 40$, subset sum or split problem | **Meet in the Middle** | Volume 2, Ch 8.2.3 |

---

## 3. Querying & Extracting from the Reference Library

When the agent requires verbatim problem descriptions, proofs, mathematical derivations, or sample implementations directly from the PDFs, use the bundled query utility:

### Location:
`scripts/query_cpbook.py`

### Usage:

1. **Extracting Specific Pages**:
   ```bash
   python scripts/query_cpbook.py extract --book 1 --start 133 --end 142
   ```
   *Options:*
   - `--book`: `1` (Volume 1) or `2` (Volume 2)
   - `--start`: 0-based start page index
   - `--end`: 0-based end page index (inclusive)
   - `--output`: (Optional) path to save the extracted markdown/text file

2. **Searching for Keywords/Topics**:
   ```bash
   python scripts/query_cpbook.py search --book 2 --query "Heavy-Light Decomposition" --limit 5
   ```

---

## 4. Problem Solving Workflow & Collaborative Design Protocol

### 🚨 Mandatory Agent Behavioral Rule: Collaborative Design Decisions
**Never generate code blindly without user consensus when architectural choices exist.**
If more than one data structure, algorithm, or paradigm can solve the user's problem:
1. **Identify the Candidates**: List the applicable options (e.g., Fenwick Tree vs. Segment Tree, Kruskal vs. Prim, Top-Down Memoization vs. Bottom-Up Tabulation, Dijkstra vs. SPFA).
2. **Present Trade-offs**: Detail Time Complexity, Space Complexity, Implementation Overhead, and Cache Locality for each.
3. **Ask the User**: Explicitly ask the user which approach aligns best with their specific constraints, performance targets, or stylistic preferences before writing the final code.

---

### 🚨 Mandatory Problem Preservation Protocol (`problems/` Database)
Whenever a problem is provided, tackled, or analyzed—regardless of whether it originates from a local markdown file, an online judge (Codeforces, LeetCode, CSES, AtCoder, etc.), or a reference book:
1. **Store a Copy**: You MUST create and preserve a self-contained copy of the problem statement inside the `problems/` directory.
2. **Attribute the Source**: Explicitly document the source name (e.g., platform name, contest, problem number, or book volume and page) and URL/citation in the problem metadata.
3. **Apply Template**: Map and apply the corresponding template from `Templates/` to formulate the solution.

---

### Algorithmic Problem Solving Framework:
Adhere to the rigorous 3-step mastery framework:

1. **Input Bounds & Complexity Analysis**:
   - Check $N$:
     - $N \le 10 \implies O(N!)$ or $O(N^6)$ (Permutations, Brute Force)
     - $N \le 20 \implies O(2^N)$ or $O(N^2 2^N)$ (Bitmask DP)
     - $N \le 500 \implies O(N^3)$ (Floyd-Warshall, Matrix DP)
     - $N \le 5000 \implies O(N^2)$ (Quadratic DP, Nested Loops)
     - $N \le 10^5 \implies O(N \log N)$ or $O(N)$ (Sorting, Segment Tree, Greedy, D&C)
     - $N \le 10^9 \implies O(\log N)$ or $O(1)$ (Binary Search, Math, Matrix Exponentiation)
2. **Identification of Invariants & Paradigms**:
   - Verify greedy choice property and optimal substructure before committing to Greedy.
   - For DP, define the exact state tuple $S$, base cases, and transition recurrence.
3. **Template & Robustness**:
   - Guard against integer overflow: use 64-bit integers (`long long` in C++, `int` in Python 3).
   - Fast I/O routines for high-volume inputs.
   - Corner cases: $N=0, 1$, disconnected components, negative weights, multiple edges/self-loops.
