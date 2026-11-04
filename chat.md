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

## Session 12: Complete Rendering Fixes & Typography Normalization

### User Request
> "please fix the rendering problem"

### Actions Taken & Implementation Summary
1. **Sanitized Mermaid Syntax**:
   - Replaced illegal `<br/>` HTML tags and raw Unicode characters (`²`, `³`, `>`, `<`, `==>`, `->`, `&`) within the flowchart node strings that were triggering syntax errors and breaking diagram rendering.
   - Simplified all labels to strict, portable Mermaid syntax supported by GitHub, VS Code, and browser markdown engines.
2. **Normalized Typography & Zero Non-ASCII Font Glitches**:
   - Replaced curved quotation marks (`“`, `”`, `‘`, `’`), en/em dashes (`–`, `—`), and non-standard superscript numbers (`²`, `³`) with clean, universal standard ASCII characters (`^2`, `^3`, `"`, `'`, `-`, `--`).
   - Converted emoji markers to clean, universal square bracket labels (e.g. `[Guide]`, `[Decision Tree]`, `[Memory Trick]`, `[Python]`, `[Java]`), eliminating CP1252/UTF-8 character corruption on Windows systems.
3. **Automated Verification**:
   - Confirmed 0 non-ASCII font-breaking characters remaining in the document.
   - Tested that all 14 Python executable code blocks and all 13 Java classes compile and run with 100% success.












