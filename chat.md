# Science of Coding - Conversation and Project Log

This document records all instructions, architectural decisions, and agent conversations for the **Science of Coding** project.

---

## Session 1: Skill Creation and Reference Initialization

### User Request
> "In this project my task is to create a complete mannual for science of coding. I will use these two books for reference. So you have to 1st create a skill that will contain these two books. its not gonna be a claude code specific skill. it will be a generic skill that can be used with any agentic ai. skills name will be cpbook4.@[Part-1.pdf] @[Parttt-2.pdf] also Create 1 chat.md file where all the conversation with the agent will be stored."

### Actions Taken & Implementation Summary
1. **Repository & File Analysis**:
   - Inspected source PDFs:
     - `Part-1.pdf` (Book 1, 329 pages): Covers Introduction, Data Structures and Libraries, Problem Solving Paradigms (Complete Search, Divide & Conquer, Greedy, DP), and Graph algorithms (Traversals, MST, SSSP, APSP, Special Graphs).
     - `Parttt-2.pdf` (Book 2, 352 pages): Covers Mathematics, String Processing, Computational Geometry, More Advanced Topics (State-Space Search, DP optimizations, Network Flow, Matching, NP-hard problems, Decomposition), and Rare Topics (Sparse Table, HLD, FFT, Pollard's Rho, etc.).
   - Replicated clean copies under `Books/` (`Part-1.pdf` and `Part-2.pdf`).

2. **Generic Skill Architecture (`cpbook4`)**:
   - Structured according to the universal Agent Skill specification (`SKILL.md` frontmatter + markdown body + references + utility scripts):
     - `.agent/skills/cpbook4/SKILL.md`: Main specification containing problem classification rules, complexity reference guides, algorithm decision matrices, and usage instructions.
     - `.agent/skills/cpbook4/references/table_of_contents.md`: Exhaustive index of all chapters, sections, sub-sections, and PDF page mappings across both volumes.
     - `.agent/skills/cpbook4/references/toc_book1.json` and `toc_book2.json`: Machine-readable outline structures for agent parsing.
     - `.agent/skills/cpbook4/scripts/query_cpbook.py`: Agent-executable CLI utility supporting UTF-8 safe keyword searching and precise page-range extraction directly from both books.
   - Provided cross-agent compatibility copies at:
     - `.claude/skills/cpbook4/SKILL.md`
     - `cpbook4_SKILL.md`

3. **Status**:
   - Generic skill `cpbook4` initialized and operational.
   - `chat.md` log established for tracking ongoing development of the *Science of Coding* manual.

---

## Session 11: Master Graph & Tree Decision Tree Diagram

### User Request
> "can you also add a decision tree diagram of the whole graph and tree segement so that it beomes easy what to chose at what codition"

### Actions Taken & Implementation Summary
1. **Added Master Decision Tree Flowchart**:
   - Integrated a comprehensive **Mermaid decision tree flowchart** directly into [`query/001_graph_and_tree_learning_roadmap.md`](query/001_graph_and_tree_learning_roadmap.md).
   - Structured around real interview conditions (Tree vs General Graph $\to$ Query Type $\to$ Algorithm).
2. **Added Quick-Lookup Interview Trigger Table**:
   - Tabular quick-reference mapping exact problem statement trigger phrases to their matching algorithms and time bounds.

---

## Session 13: Enhancing Interview Trigger Table with Real Examples & Plain-English Solutions

### User Request
> "in the [Summary] Quick-Lookup Interview Trigger Table create a colomn and provide one example problem in short term and another coloum provide how it solves it using the algorithm in normal language term"

### Actions Taken & Implementation Summary
1. **Added Two New Pedagogical Columns to the Quick-Lookup Table**:
   - **Column 5 (`Real-World Example Problem`)**: Anchors each trigger phrase to a canonical competitive programming or interview challenge (e.g. *LeetCode 1091: Shortest Path in Binary Matrix*, *LeetCode 210: Course Schedule II*, *LeetCode 1192: Critical Connections in a Network*, *LeetCode 1584: Min Cost to Connect All Points*, *LeetCode 236: Lowest Common Ancestor*).
   - **Column 6 (`Plain-English Intuitive Solution`)**: Explains the exact mechanism in simple, jargon-free conversational terms:
     - *Tree Diameter*: *"Pick any node at random, find furthest node X. From X, run DFS again to find Y. Path X to Y is the longest highway in the tree."*
     - *BFS*: *"Drop a stone at start. Like water ripples expanding 1 tile outward every second, the moment a ripple touches the exit tile, you have reached it in the absolute fewest steps possible."*
     - *Kahn's Toposort*: *"Put courses with 0 prerequisites in a queue. Take each course, cross it off, and reduce prerequisites for subsequent courses until done."*
     - *Dijkstra*: *"Keep a scoreboard of shortest times and a Priority Queue. Always pick the unvisited node with the smallest recorded time, send signals, and relax neighbors."*
     - *Bellman-Ford*: *"Try improving every flight route in the world V - 1 times. If any price can still decrease on the V-th round, you found an infinite money glitch (negative cost cycle)."*
     - *Kruskal*: *"Put all cables in a price-sorted list from cheapest to most expensive. Greedily plug in the cheapest cable unless it connects two cities already linked together."*
     - *Tarjan Bridges*: *"Track your arrival timestamp and the oldest ancestor your kids can reach via side roads. If your child has no side road back to someone older than you, your cable is a critical bridge."*
     - *Kuhn's Matching*: *"Try matching Worker A to their favorite job. If occupied by B, politely ask B to switch to their second choice. If B can switch, A takes the job!"*
2. **Updated Master File**:
   - Verified that [`query/001_graph_and_tree_learning_roadmap.md`](query/001_graph_and_tree_learning_roadmap.md) renders with 100% clean formatting and zero font issues.













