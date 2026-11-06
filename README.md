# Science of Coding

An exhaustive, high-performance algorithmic engineering manual and agentic AI skill system designed for rigorous software problem-solving and deterministic code generation.

---

## 🎯 Core Philosophy & Project Objective

> *"The objective of this project is to establish deterministic control and architectural transparency over agentic coding models, rather than passively accepting unverified AI-generated code. Whenever multiple valid designs or algorithmic trade-offs exist, the agent must proactively engage the developer—presenting architectural options, evaluating time/space trade-offs, and seeking explicit consensus before implementing code."*

### Moving from Black-Box AI to Collaborative Engineering

Modern LLM-powered coding assistants frequently suffer from two fatal failure modes:
1. **Unchecked Assumption Making**: Agents unilaterally choose an arbitrary design, implementation pattern, or complexity profile without consulting the developer about constraints, trade-offs, or production idioms.
2. **Context Hallucination & Suboptimal Patterns**: Agents generate superficial or subtly flawed code because their advice is not tethered to authoritative data structures, mathematical proofs, and invariant analysis.

**Science of Coding** solves this by establishing a **Human-in-the-Loop, Invariant-Grounded Engineering Framework**:
- **Proactive Design Consultations**: When more than one algorithmic paradigm or data structure is applicable (e.g., iterative vs. recursive DP, Fenwick Tree vs. Segment Tree, Dijkstra vs. SPFA, Kruskal vs. Prim), the agent is **mandated** to present the candidate options alongside their trade-offs (time complexity, space overhead, implementation complexity, cache locality) and request the user's architectural preference before writing code.
- **Authoritative Reference Grounding**: All algorithmic reasoning is anchored to mathematically verified invariants and optimal Big-O bounds.

---

## 📖 Key Deliverables

1. **The Science of Coding Manual**: Structured guides, mathematical proofs, pattern decompositions, and battle-tested code templates with side-by-side runnable implementations in **Python 3** and **Java 21**.
2. **`Templates/` Directory (Agent Solution Blueprints)**: Explicit step-by-step methodologies and conceptual frameworks instructing the agent on *how* to deconstruct, design, and verify code systematically.
3. **`cpbook4` Agentic Skill**: A portable, self-contained AI agent skill that enables any Agentic AI (Antigravity, Claude Code, Cursor, Copilot, ChatGPT, or custom LLM harnesses) to retrieve exact formulas, theorems, and implementations on demand without context exhaustion or hallucinations.
4. **`query/` Knowledgebase**: A dedicated library of deep-dive query documents featuring visual decision trees, interview memory mnemonics, and real-world problem mappings.
5. **`Upcoming Updates/` Roadmap**: A centralized milestone tracker with task status boxes for planned features and upcoming manuals.
6. **`chat.md`**: A chronological record of all conversations, architectural decisions, and design sessions.

---

## 🧩 Templates: Guiding Agent Problem-Solving

The primary purpose of the [`Templates/`](Templates/) directory is to **instruct the agent on the exact mental model and step-by-step procedure required to solve a problem**. Rather than allowing the agent to jump straight to writing ungrounded loops or ad-hoc logic, each template provides:
- **Core Conceptual Foundations**: Formal definitions (e.g., What is a state? What are the variable roles? What are state transitions and invariants?).
- **Step-by-Step Problem-Solving Recipes**: Strict, phased instructions (e.g., Phase 1: List Candidate Variables $\to$ Classify Roles $\to$ Define the Minimal State; Phase 2: Map Relationships & Draw the State Tree; Phase 3: Synthesize Loops; Phase 4: Mathematical Verification & Edge Case Auditing).
- **Failure Mode & Edge Case Prevention**: Detailed catalogs of common implementation traps, off-by-one errors, and invariant violations to check against before code generation.

### Available Templates

- [`Templates/Repetitive Structure Template.md`](Templates/Repetitive%20Structure%20Template.md): A comprehensive blueprint for designing and deriving loops, nested iterations, multi-variable states, and state-space trees from first principles.

---

## 🧠 The `cpbook4` Agent Skill

The `cpbook4` skill encapsulates comprehensive reference libraries:
- **Foundations & Core Algorithms**: 329 pages  
  *Introduction, Built-in and Custom Linear/Non-linear Data Structures (UFDS, Fenwick Tree, Segment Tree), Core Paradigms (Complete Search, Divide & Conquer, Greedy, Dynamic Programming), and Graph Algorithms (DFS/BFS, MST, SSSP, APSP, Special Graphs).*
- **Advanced Systems & Mathematics**: 352 pages  
  *Mathematics (Number Theory, Combinatorics, Probability, Game Theory, Matrix Power), String Processing (KMP, Suffix Trie/Tree/Array, Hashing, Manacher), Computational Geometry, Advanced Search & DP, Network Flow, Matching, NP-hard Problems, Problem Decomposition, and Rare Topics (Sparse Table, HLD, LCA, FFT/NTT, Simplex).*
- **Total Volume**: 681 pages, ~328,000 words (~436,000 tokens).

### 4-Tier Precision Retrieval & Problem-Solving Architecture

Loading ~436,000 tokens into an AI context window causes severe degradation and token bloat. Furthermore, retrieving raw algorithmic theory without a structured decomposition methodology causes agents to generate hasty, unverified code. 

**Science of Coding** solves this through a **4-Tier Precision Pipeline** described in detail in [`skill/ARCHITECTURE.md`](skill/ARCHITECTURE.md):

```
                        Task / User Coding Problem
                                    │
                                    ▼
                          Any Agentic AI System
        (Blends Trained LLM Knowledge + Web Search + Textbooks)
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         │                                                     │
         ▼                                                     ▼
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│     KNOWLEDGE RETRIEVAL LAYER   │           │    TEMPLATE-DRIVEN SYNTHESIS    │
│  1. Curated Reference Textbooks │           │         (MANDATORY OUTPUT)      │
│     - Table of Contents Router  │           │                                 │
│     - CLI Search & Page Extract │           │  Templates/*.md                 │
│  2. Web Search & Live Retrieval │           │  - Step-by-Step Problem Solving │
│  3. Model Pre-trained Reasoning │           │  - State Invariants & Roles     │
└────────────────┬────────────────┘           │  - State-Space Tree Derivation  │
                 │                            │  - Failure Mode Audits          │
                 │                            └────────────────┬────────────────┘
                 │                                             │
                 └──────────────────────┬──────────────────────┘
                                        ▼
                        Collaborative Design Consensus
                    (Propose Options & Ask User Before Coding)
                                        │
                                        ▼
                         Template-Formatted Output
                       (100% Deterministic & Verified)
```

#### Architecture Principles & Operational Flow:
1. **Tri-Source Knowledge Absorption**: The agentic AI absorbs theoretical and domain knowledge from three complementary streams:
   - **Curated Textbooks (`skill/books/`)**: Surgical page extractions (`query_cpbook.py extract`) for mathematically verified proofs, data structure layouts, and invariant formulas.
   - **Model Pre-trained Knowledge**: The LLM's intrinsic reasoning, language idioms, and algorithm patterns.
   - **Targeted Web Search**: Online judge lookups and real-time documentation checks for niche edge cases.
2. **Mandatory Template-Driven Output Formulation**: While knowledge is gathered from multiple sources, **the agent is strictly mandated to format its output through the modular templates in `Templates/`**. The agent cannot produce arbitrary, unstructured code. It must systematically follow each phase established in the relevant template (e.g., defining candidate variables, assigning variable roles, defining the true state, building the state-space tree, deriving bounds, and verifying edge cases).
3. **Continuous Template Expansion**: The `Templates/` directory is an evolving library where specialized templates will be added for every major problem type (Repetitive Structures, State-Space Search, Divide & Conquer, Dynamic Programming, and Graph Traversals).

---

## 📂 Repository Structure

```
Science_Of_Coding/
├── .agent/
│   └── skills/
│       └── cpbook4/
│           └── SKILL.md            # Entrypoint for Antigravity native skill discovery
├── Templates/                      # Methodological blueprints guiding agent problem-solving
│   └── Repetitive Structure Template.md # Step-by-step guide for states, loops, and trees
├── Upcoming Updates/               # Roadmap, milestone checklist, and feature tracking
│   └── Upcoming Updates.md         # Serialized progress tracking template
├── query/                          # Deep-dive algorithmic manuals & query outputs
│   ├── 001_graph_and_tree_learning_roadmap.md
│   └── 002_data_structures_master_manual.md
├── skill/                          # Standalone, portable Agent Skill package
│   ├── ARCHITECTURE.md             # Detailed architectural specification & mechanics
│   ├── SKILL.md                    # Universal agent skill instructions & decision matrix
│   ├── books/                      # Curated coding & reference books library
│   │   ├── Flowchart/              # Flowchart & programming techniques
│   │   ├── Overall/                # Comprehensive algorithm references
│   │   │   ├── Part-1.pdf          # Volume 1 (329 pages)
│   │   │   └── Part-2.pdf          # Volume 2 (352 pages)
│   │   └── Programming Logic/      # Programming logic & loop patterns
│   ├── references/                 # Table of contents and machine-readable outline trees
│   │   ├── table_of_contents.md    # Fast topic-to-page navigation map
│   │   ├── toc_book1.json          # Book 1 JSON outline tree
│   │   └── toc_book2.json          # Book 2 JSON outline tree
│   └── scripts/
│       └── query_cpbook.py         # Search and page extraction CLI utility
├── chat.md                         # Persistent project conversation & decision log
└── README.md                       # Repository overview and usage guide
```

---

## 🤖 How to Use the `cpbook4` Skill with Agentic AIs

The `cpbook4` skill enforces the **collaborative design protocol**: when multiple approaches exist, the agent must consult you before implementing.

### 1. Google Antigravity
Antigravity automatically discovers skills inside `.agent/skills/`:
- **Auto-Discovery**: Pre-configured at [`.agent/skills/cpbook4/SKILL.md`](.agent/skills/cpbook4/SKILL.md).
- **Interactive Prompts**:
  - *"Using @skill:cpbook4, I need to design a system for dynamic range minimum queries with updates. Present the available options and ask me which one fits best before writing code."*
  - *"Using cpbook4 and `Templates/Repetitive Structure Template.md`, decompose this multi-variable nested loop problem step by step."*
- **Agent Behavior**: Antigravity reads the decision trees in `SKILL.md`, references the appropriate methodology in `Templates/`, executes `query_cpbook.py` behind the scenes, presents the available algorithmic options, and waits for your confirmation.

### 2. Claude Code
Claude Code discovers skills via `.claude/skills/` or prompt inclusion:
- **Workspace Setup**:
  ```bash
  # Windows PowerShell
  New-Item -ItemType Directory -Force -Path ".claude\skills\cpbook4"
  Copy-Item -Path "skill\SKILL.md" -Destination ".claude\skills\cpbook4\SKILL.md"
  ```
- **Project Rule in `CLAUDE.md`**:
  ```markdown
  When handling algorithmic or data structure tasks:
  1. Always consult the cpbook4 skill in `skill/SKILL.md` and relevant blueprints in `Templates/`.
  2. If more than one viable design or data structure exists, present the trade-offs and ask the user for their preferred design before coding.
  3. Query books using: python skill/scripts/query_cpbook.py search|extract
  ```
- **Prompt Invocation**:
  > *"Consult `skill/SKILL.md` and outline the possible approaches for Maximum Bipartite Matching. Ask me how I want to structure the code before implementation."*

### 3. OpenAI Codex / Cursor / Custom Agent Frameworks
For Cursor, Copilot Workspace, OpenAI Codex, or LangChain agents:
- **System Instructions (`.cursorrules` / `AGENTS.md`)**:
  ```markdown
  ### Algorithmic Design Protocol:
  1. Consult `skill/SKILL.md` and `skill/references/table_of_contents.md`.
  2. For structured problem decomposition, follow the guidelines in `Templates/`.
  3. Query exact reference pages using: python skill/scripts/query_cpbook.py search|extract
  4. MANDATORY: If more than one algorithmic solution exists (e.g., Kruskal vs. Prim, Top-Down vs. Bottom-Up DP, Fenwick vs. Segment Tree), present the options with time/space trade-offs and ASK the user which design they prefer before generating code.
  ```

---

## 🛠️ CLI Usage: Querying the Books Directly

You or any AI agent can query and extract text from the books on demand using Python (requires `pypdf`):

### 1. Keyword / Phrase Search
Scan either book for specific algorithms, problem references, or keywords:
```bash
python skill/scripts/query_cpbook.py search --book 1 --query "Fenwick" --limit 5
python skill/scripts/query_cpbook.py search --book 2 --query "Heavy-Light Decomposition" --limit 3
```

### 2. Surgical Page Extraction
Extract verbatim pages (text, proofs, code) into console or to a file:
```bash
# Print pages 143 to 148 of Book 1 (Segment Tree)
python skill/scripts/query_cpbook.py extract --book 1 --start 143 --end 148

# Save Dinic's Algorithm pages from Book 2 to a file
python skill/scripts/query_cpbook.py extract --book 2 --start 156 --end 160 --output dinic.txt
```

---

## 🔒 Copyright & Terms of Use

**Copyright © 2026. All rights reserved.**

This repository and all its contents—including but not limited to the manuals, query guides, architectural designs, agentic templates, decision trees, and code implementations—are proprietary copyrighted material. **No unauthorized copying, distribution, reproduction, modification, or commercial use is permitted without explicit prior written consent from the author.**
