# Detailed Table of Contents & Topic Index: CP4 (Competitive Programming 4)
**Authors**: Steven Halim, Felix Halim, Suhendry Effendy

---

## BOOK 1: Fundamental Data Structures & Core Problem-Solving Paradigms
- **File Reference**: `skill/books/Overall/Part-1.pdf` (Total Pages: 329)

### Chapter 1: Introduction (PDF Page 30)
- **1.1 Competitive Programming**: Overview, goals, skills required (page 30).
- **1.2 The Competitions**:
  - 1.2.1 International Olympiad in Informatics (IOI) (page 32)
  - 1.2.2 International Collegiate Programming Contests (ICPC) (page 33)
  - 1.2.3 Other Programming Contests (page 35)
- **1.3 Tips to be Competitive**:
  - 1.3.1 Tip 1: Type Code Faster! (page 35)
  - 1.3.2 Tip 2: Quickly Identify Problem Types (page 37)
  - 1.3.3 Tip 3: Do Algorithm Analysis (Time and Space Complexity, Big-O calculation) (page 39)
  - 1.3.4 Tip 4: Master Programming Languages (C++, Java, Python, OCaml) (page 44)
  - 1.3.5 Tip 5: Master the Art of Testing Code (Edge cases, stress testing, test generation) (page 47)
  - 1.3.6 Tip 6: Practice and More Practice (page 50)
  - 1.3.7 Tip 7: Team Work (for ICPC) (page 51)
- **1.4 Getting Started: The Easy Problems**:
  - 1.4.1 Anatomy of a Programming Contest Problem (page 52)
  - 1.4.2 Typical Input/Output Routines (Fast I/O in C++, Java, Python) (page 52)
  - 1.4.3 Time to Start the Journey (page 55)
  - 1.4.4 Getting Our First Accepted (AC) Verdict (page 56)
- **1.5 Basic String Processing Skills** (page 60)
- **1.6 The Ad Hoc Problems**: Game Simulation, Card Games, Time/Date manipulation, Real Life simulation (page 62)
- **1.7 Solutions to Non-Starred Exercises** (page 70)
- **1.8 Chapter Notes** (page 80)

---

### Chapter 2: Data Structures and Libraries (PDF Page 82)
- **2.1 Overview and Motivation** (page 82)
- **2.2 Linear DS with Built-in Libraries**:
  - 2.2.1 Array (Vector, 1D/2D/3D static & dynamic arrays) (page 84)
  - 2.2.2 Special Sorting Problems (Inversion counting, custom comparators) (page 88)
  - 2.2.3 Bitmask (Bit manipulation, bitwise operations, subsets generation) (page 91)
  - 2.2.4 Big Integer (Python & Java built-in capabilities) (page 95)
  - 2.2.5 Linked Data Structures (Singly, Doubly linked list) (page 98)
  - 2.2.6 Special Stack-based Problems (Monotonic stack, expression parsing, parentheses matching) (page 100)
- **2.3 Non-Linear DS with Built-in Libraries**:
  - 2.3.1 Binary Heap (Priority Queue, min/max heap, custom comparator) (page 107)
  - 2.3.2 Hash Table (Direct Addressing, `unordered_map`, `unordered_set`, collision resolution) (page 110)
  - 2.3.3 Balanced Binary Search Tree (bBST) (`std::set`, `std::map`, AVL/Red-Black fundamentals) (page 113)
  - 2.3.4 Order Statistics Tree (GNU C++ `pb_ds` tree with `find_by_order` and `order_of_key`) (page 116)
- **2.4 DS with Our Own Libraries**:
  - 2.4.1 Graph Data Structures (Adjacency Matrix, Adjacency List, Edge List) (page 123)
  - 2.4.2 Union-Find Disjoint Sets (UFDS / DSU with path compression & union by rank) (page 128)
  - 2.4.3 Fenwick (Binary Indexed) Tree (Point update, range sum query, 2D Fenwick, RURQ) (page 133)
  - 2.4.4 Segment Tree (Range Minimum Query RMQ, Range Sum, Lazy Propagation) (page 143)
- **2.5 Solution to Non-Starred Exercises** (page 153)
- **2.6 Chapter Notes** (page 156)

---

### Chapter 3: Problem Solving Paradigms (PDF Page 158)
- **3.1 Overview and Motivation** (page 158)
- **3.2 Complete Search (Brute Force / Exhaustive Search)**:
  - 3.2.1 Iterative Complete Search (Nested loops, permutation generation) (page 160)
  - 3.2.2 Recursive Complete Search / Backtracking (N-Queens, Sudoku, subset sum) (page 164)
  - 3.2.3 Complete Search Tips (Pruning, symmetry breaking, precomputation) (page 168)
  - 3.2.4 Complete Search in Programming Contests (page 172)
- **3.3 Divide and Conquer**:
  - 3.3.1 Interesting Usages of Binary Search (Bisection, `std::lower_bound`, Bisection method on floating points) (page 177)
  - 3.3.2 Ternary Search (Unimodal functions, finding extrema) (page 181)
  - 3.3.3 Divide and Conquer in Programming Contests (page 182)
- **3.4 Greedy**:
  - 3.4.1 Classic Examples (Interval scheduling / Activity selection, Coin Change, Fractional Knapsack) (page 184)
  - 3.4.2 Greedy Algorithm in Programming Contests (page 190)
- **3.5 Dynamic Programming (DP)**:
  - 3.5.1 DP Illustration (Memoization top-down vs Tabulation bottom-up) (page 193)
  - 3.5.2 Classical Examples:
    - Max 1D/2D Range Sum (Kadane's algorithm)
    - 0-1 Knapsack and Unbounded Knapsack
    - Longest Increasing Subsequence (LIS in $O(n^2)$ and $O(n \log k)$)
    - Coin Change (Minimal coins, number of ways)
    - Traveling Salesperson Problem (TSP with bitmask DP) (page 202)
  - 3.5.3 Non-Classical Examples (page 213)
  - 3.5.4 Dynamic Programming in Programming Contests (page 216)
- **3.6 Solution to Non-Starred Exercises** (page 219)
- **3.7 Chapter Notes** (page 220)

---

### Chapter 4: Graph (PDF Page 222)
- **4.1 Overview and Motivation** (page 222)
- **4.2 Graph Traversal**:
  - 4.2.2 Depth First Search (DFS) (page 224)
  - 4.2.3 Breadth First Search (BFS) (page 226)
  - 4.2.4 Finding Connected Components (Undirected Graph) (page 227)
  - 4.2.5 Flood Fill (Implicit 2D Grid Graph) (page 228)
  - 4.2.6 Topological Sort (Kahn's algorithm, DFS-based post-order) (page 229)
  - 4.2.7 Bipartite Graph Check (2-Coloring via BFS/DFS) (page 231)
  - 4.2.8 Cycle Check (Directed Graph back-edges, Undirected Graph) (page 232)
  - 4.2.9 Finding Articulation Points and Bridges (Tarjan's DFS Lowlink algorithm) (page 234)
  - 4.2.10 Finding Strongly Connected Components (SCC) (Tarjan's and Kosaraju's algorithms) (page 237)
- **4.3 Minimum Spanning Tree (MST)**:
  - 4.3.1 Kruskal's Algorithm (with UFDS) (page 244)
  - 4.3.2 Prim's Algorithm (Priority Queue) (page 248)
  - 4.3.3 Variants: Second best MST, Minimum Spanning Subgraph, Minimax/Maximin paths (page 250)
- **4.4 Single-Source Shortest Paths (SSSP)**:
  - 4.4.1 On Unweighted Graph (BFS) (page 254)
  - 4.4.2 On Weighted Graph without Negative Weight: Dijkstra's Algorithm (page 256)
  - 4.4.3 On Graph with Negative Weight: Bellman-Ford (page 263)
  - 4.4.4 Shortest Path Faster Algorithm (SPFA) (page 265)
- **4.5 All-Pairs Shortest Paths (APSP)**:
  - 4.5.2 Floyd-Warshall Algorithm (Transitive closure, min cycle) (page 271)
- **4.6 Special Graphs**:
  - 4.6.1 Directed Acyclic Graph (DAG) (SSSP on DAG, longest path) (page 278)
  - 4.6.2 Tree (Diameter of tree, Tree centers, SSSP on tree) (page 284)
  - 4.6.3 Bipartite Graph (page 286)
  - 4.6.4 Eulerian Graph (Hierholzer's algorithm) (page 289)
- **4.7 & 4.8 Solutions and Chapter Notes** (page 296)

---

## BOOK 2: Advanced Topics, Mathematics, Strings, Geometry & Hard Problems
- **File Reference**: `skill/books/Overall/Part-2.pdf` (Total Pages: 352)

### Chapter 5: Mathematics (PDF Page 8)
- **5.2 Ad Hoc Mathematics**: Base numbers conversion, roman numerals, sequence generation (page 9)
- **5.3 Number Theory**:
  - 5.3.1 Prime Numbers (Sieve of Eratosthenes) (page 17)
  - 5.3.2 Probabilistic Prime Testing (Miller-Rabin) (page 19)
  - 5.3.3 Prime Factorization (Trial division, Wheel factorization) (page 19)
  - 5.3.4 Functions Involving Prime Factors (Number of divisors $\tau(n)$, Sum of divisors $\sigma(n)$, Euler's Phi / Totient $\phi(n)$) (page 21)
  - 5.3.6 GCD & LCM (Euclidean Algorithm) (page 23)
  - 5.3.9 Modular Arithmetic & Modular Inverses (Fermat's Little Theorem) (page 25)
  - 5.3.10 Extended Euclidean Algorithm (Linear Diophantine Equations) (page 27)
- **5.4 Combinatorics**:
  - 5.4.1 Fibonacci Numbers (page 33)
  - 5.4.2 Binomial Coefficients ($\binom{n}{k}$, Pascal's triangle, Lucas' theorem) (page 34)
  - 5.4.3 Catalan Numbers ($C_n = \frac{1}{n+1}\binom{2n}{n}$) (page 35)
- **5.5 Probability Theory**: Expected value, linearity of expectation (page 40)
- **5.6 Cycle-Finding**: Floyd's Tortoise and Hare algorithm, Brent's algorithm (page 43)
- **5.7 Game Theory (Basic)**: Minimax, Nim games, Sprague-Grundy theorem, impartial games (page 47)
- **5.8 Matrix Power**: Matrix multiplication, binary exponentiation, accelerating linear recurrences / DP (page 50)

---

### Chapter 6: String Processing (PDF Page 60)
- **6.2 Ad Hoc String (Harder)** (page 61)
- **6.3 String Processing with DP**:
  - 6.3.1 String Alignment / Edit Distance (Levenshtein distance) (page 64)
  - 6.3.2 Longest Common Subsequence (LCS) (page 66)
- **6.4 String Matching**:
  - 6.4.2 Knuth-Morris-Pratt (KMP) Algorithm & Prefix Function (page 68)
  - 6.4.3 2D Grid String Matching (page 71)
- **6.5 Suffix Trie / Tree / Array**:
  - 6.5.1 Suffix Trie (page 73)
  - 6.5.2 Suffix Tree (Ukkonen's algorithm concept) (page 75)
  - 6.5.4 Suffix Array ($O(n \log^2 n)$ and $O(n \log n)$ construction, LCP array via Kasai's algorithm) (page 78)
  - 6.5.5 Applications (Substrings matching, LRS, LCS of two strings) (page 86)
- **6.6 String Matching with Hashing**:
  - Polynomial Rolling Hash, Rabin-Karp Algorithm, handling collisions with double hash (page 90)
- **6.7 Anagram and Palindrome**: Manacher's Algorithm for Longest Palindromic Substring (page 94)

---

### Chapter 7: (Computational) Geometry (PDF Page 100)
- **7.2 Basic Geometry Objects**:
  - 7.2.1 Points: Distance, rotation, dot/cross products (page 103)
  - 7.2.2 Lines: Slopes, intersections, projections, distances to lines/segments (page 106)
  - 7.2.3 Circles: Tangents, intersections, circumcircle, incircle (page 111)
  - 7.2.4 Triangles: Area (Heron's), law of sines/cosines (page 113)
  - 7.2.5 Quadrilaterals (page 116)
- **7.3 Algorithms on Polygons**:
  - 7.3.1 Representation (Vector of points) (page 119)
  - 7.3.2 Perimeter & Area (Shoelace formula) (page 119)
  - 7.3.4 Convexity check (page 121)
  - 7.3.5 Point in Polygon check (Ray-casting / winding number) (page 122)
  - 7.3.6 Cutting Polygon with a Line (Sutherland-Hodgman) (page 123)
  - 7.3.7 Convex Hull (Graham scan, Monotone Chain algorithm) (page 125)
- **7.4 3D Geometry**: Spherical coordinates, great circle distance (page 131)

---

### Chapter 8: More Advanced Topics (PDF Page 136)
- **8.2 Advanced Search**:
  - 8.2.1 Backtracking with Bitmask (page 137)
  - 8.2.2 State-Space Search (0-1 BFS, Dijkstra on implicit state space) (page 140)
  - 8.2.3 Meet in the Middle (Subsetting $2^{40} \to 2 \cdot 2^{20}$) (page 142)
- **8.3 Advanced DP Techniques**:
  - 8.3.1 DP with Bitmask (Hamiltonian path, assignment problem) (page 146)
  - 8.3.3 Negative Parameter handling with Offset (page 147)
  - 8.3.4 - 8.3.8 State compression, dropping redundant states, binary search transition speedup (page 148)
- **8.4 Network Flow**:
  - 8.4.2 Ford-Fulkerson Method (page 152)
  - 8.4.3 Edmonds-Karp Algorithm ($O(V E^2)$) (page 154)
  - 8.4.4 Dinic's Algorithm ($O(V^2 E)$) (page 156)
  - 8.4.5 Flow Graph Modeling: Max Flow Min Cut theorem, Vertex capacities, Multi-source/multi-sink (page 159)
- **8.5 Graph Matching**:
  - Maximum Cardinality Bipartite Matching (MCBM) via Augmenting Path / Flow (page 168)
  - Weighted MCBM & Min Cost Max Flow (page 172)
- **8.6 NP-Hard/Complete Problems**:
  - TSP, Max Independent Set, Min Vertex Cover, Min Set Cover, 2-SAT / 3-SAT, Steiner Tree (page 178)
- **8.7 Problem Decomposition**:
  - Binary search + greedy/graph/geometry/data structure, multi-step problem solving (page 195)

---

### Chapter 9: Rare Topics (PDF Page 216)
- **9.2 Sliding Window** (Two pointers, monotonic queue) (page 218)
- **9.3 Sparse Table** (Static RMQ in $O(1)$ query, $O(n \log n)$ preprocessing) (page 221)
- **9.4 Square Root Decomposition & Mo's Algorithm** (Offline range queries) (page 224)
- **9.5 Heavy-Light Decomposition (HLD)** (Queries on trees via Segment Tree) (page 228)
- **9.7 Matrix Chain Multiplication** (page 234)
- **9.8 Lowest Common Ancestor (LCA)** (Binary Lifting) (page 237)
- **9.9 Tree Isomorphism** (AHU algorithm) (page 240)
- **9.11 Fast Fourier Transform (FFT / NTT)** (Fast polynomial multiplication in $O(n \log n)$) (page 244)
- **9.12 Pollard's rho Algorithm** (Sub-exponential integer factorization) (page 248)
- **9.13 Chinese Remainder Theorem (CRT)** (page 250)
- **9.14 Lucas' Theorem** (Binomial coefficients modulo prime $p$) (page 252)
- **9.16 Combinatorial Game Theory** (Nimbers, Grundy value computation) (page 255)
- **9.17 Gaussian Elimination** (Linear systems, Modulo 2 XOR basis) (page 258)
- **9.19 Closest Pair Problem** ($O(n \log n)$ divide and conquer) (page 264)
- **9.20 A* and IDA* Informed Search** (page 267)
- **9.23 Dynamic Programming Optimization** (Convex Hull Trick, Divide and Conquer DP, Knuth Optimization) (page 273)
- **9.24 Push-Relabel Algorithm** ($O(V^3)$ or $O(V^2 \sqrt{E})$ max flow) (page 277)
- **9.25 Min Cost Max Flow (MCMF)** (Successive shortest path algorithm) (page 280)
- **9.26 Hopcroft-Karp Algorithm** ($O(\sqrt{V} E)$ bipartite matching) (page 283)
- **9.27 Kuhn-Munkres (Hungarian) Algorithm** ($O(V^3)$ assignment) (page 285)
- **9.28 Edmonds' Blossom Algorithm** (General graph matching) (page 288)
- **9.29 Chinese Postman Problem** (page 291)
- **9.30 Constructive & 9.31 Interactive Problems** (page 294)
- **9.32 Linear Programming (Simplex Algorithm)** (page 298)
- **9.33 Gradient Descent** (page 301)

