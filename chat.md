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

## Session 10: Interview Memory Tricks & Font Rendering Fixes

### User Request
> "also add remembering trick for all topics how to remember in the interview. also some of the fonts are not rendering proeprly fix it."

### Actions Taken & Implementation Summary
1. **Added "3-Second Mental Hook" Interview Memory Tricks to All 13 Topics**:
   - **Graph Representations**: *"Excel Spreadsheet (AM) vs Phone Contact Book (AL) vs Flight Routes (EL)"*.
   - **Core Traversals**: *"Blind Maze Explorer (DFS) vs Stone in a Pond / Water Ripple (BFS for Shortest Unweighted Paths)"*.
   - **Topological Sort**: *"University Course Prerequisites & Kahn's In-Degree Zero Queue vs 3-Color DFS Back-Edges"*.
   - **Bipartite Graphs**: *"Two Rival Sports Teams & The No-Odd-Cycles Theorem"*.
   - **Tarjan's Lowlink (Bridges & AP)**: *"Single Point of Failure: `dfs_low[v] > dfs_num[u]` means no escape route, cut it and the bridge collapses"*.
   - **Strongly Connected Components**: *"Round-Trip Whirlpools: pop stack when `dfs_low[u] == dfs_num[u]` to condense into a clean DAG"*.
   - **Minimum Spanning Trees**: *"Electric Grid Cable Expansion: Kruskal (sort flat cables with UFDS) vs Prim (expand from city with Min-Heap)"*.
   - **Bellman-Ford**: *"The Time Travel Paradox: relax `V - 1` times; if distance decreases on pass `V`, an infinite money/time glitch exists"*.
   - **Floyd-Warshall**: *"The 3 Nested Loops with `k` on the OUTSIDE: Can I fly from City `i` to City `j` faster with a layover at Airport `k`?"*.
   - **Eulerian Tours**: *"The Seven Bridges of Königsberg: Tour requires all EVEN degrees; Path requires exactly TWO ODD degrees"*.
   - **Lowest Common Ancestor**: *"Binary Stepping Up the Family Tree: jump by powers of two (`2^k`) instead of single steps"*.
   - **Maximum Network Flow**: *"Water Pipes & The Golden Residual Edge Rule: pushing flow $+f$ forward MUST add $+f$ capacity backward to permit future cancellation"*.
   - **Bipartite Matching (MCBM)**: *"The Dating Game & Roommate Swap: if preference is taken, politely ask their partner to recursively find a new match"*.

2. **Font Rendering & Character Glitch Resolution**:
   - Fixed unescaped LaTeX math delimiters (`$...$`) which were causing font rendering glitches and illegible symbols in markdown viewings.
   - Cleaned up formatting into standard, universal monospaced code spans (e.g. `O(V + E)`, `O(V²)`, `V <= 1000`) that render with 100% clarity across VS Code, GitHub, and any web browser.
   - Verified that all 13 Python and 13 Java runnable code blocks remain intact.










