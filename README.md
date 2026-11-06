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
2. **`Skills_Input/` Directory (Central Ingestion & Reference Assets)**:
   - **`Skills_Input/books/`**: Curated textbooks and domain books (Flowchart, Overall algorithms, Programming Logic & Loops).
   - **`Skills_Input/Templates/`**: Explicit step-by-step methodologies and conceptual frameworks instructing the agent on *how* to deconstruct, design, and verify code systematically.
3. **`Skills_Output/` Directory (Skill-Specific Outputs Hub)**:
   - Each skill maintains its own isolated output repository under `Skills_Output/` (`<SkillName>_output/`).
   - **`Skills_Output/ProblemSkill_output/`**:
     - `Problem Files/`: Ingestion staging area (`Source of Problem/`), dynamic taxonomy (`problem catagories.docx`), formatting specifications (`problem formatting.md`), and the central [`question bank.md`](Skills_Output/ProblemSkill_output/Problem%20Files/question%20bank.md).
     - `Solution Files/`: Solutions categorized by Primary Category and Subcategory in separate Python (`<ID>_python.py`) and Java (`<ID>_java.java`) files, plus `<ID>_derivation.md` following [`output formating.md`](Skills_Output/ProblemSkill_output/output%20formating.md).
   - **`Skills_Output/cpbook4_output/`**: Houses reference-grounded algorithmic solutions, proofs, and deep-dive query roadmaps in [`query/`](Skills_Output/cpbook4_output/query/).
4. **`.agent/skills/` (Centralized Agent Skills Hub)**:
   - **`SkillsOnFixedResources/cpbook4/`**: Deep algorithmic knowledge base, data structures, and reference skill with surgical page extraction.
   - **`SkillsOnDynamicResources/ProblemSkill/`**: Autonomous ingestion skill managing staging inspection, selective problem parsing, dynamic HITL category selection, question bank updates, and solution file generation.
   - **`type of skills.md`**: Architectural manual documenting the design paradigms of fixed vs. dynamic resource skills.
5. **`Upcoming Updates/` Roadmap**: A centralized milestone tracker with task status boxes for planned features and upcoming manuals.
6. **`chat.md`**: A chronological record of all conversations, architectural decisions, and design sessions.

---

## 🧩 Templates: Guiding Agent Problem-Solving

The primary purpose of the [`Skills_Input/Templates/`](Skills_Input/Templates/) directory is to **instruct the agent on the exact mental model and step-by-step procedure required to solve a problem**. Rather than allowing the agent to jump straight to writing ungrounded loops or ad-hoc logic, each template provides:
- **Core Conceptual Foundations**: Formal definitions (e.g., What is a state? What are the variable roles? What are state transitions and invariants?).
- **Step-by-Step Problem-Solving Recipes**: Strict, phased instructions (e.g., Phase 1: List Candidate Variables $\to$ Classify Roles $\to$ Define the Minimal State; Phase 2: Map Relationships & Draw the State Tree; Phase 3: Synthesize Loops; Phase 4: Mathematical Verification & Edge Case Auditing).
- **Failure Mode & Edge Case Prevention**: Detailed catalogs of common implementation traps, off-by-one errors, and invariant violations to check against before code generation.

### Available Templates

- [`Skills_Input/Templates/Repetitive Structure Template.md`](Skills_Input/Templates/Repetitive%20Structure%20Template.md): A comprehensive blueprint for designing and deriving loops, nested iterations, multi-variable states, and state-space trees from first principles.

---

## 🗄️ `Skills_Output/`: Skill-Specific Outputs Archive

The [`Skills_Output/`](Skills_Output/) directory houses dedicated output repositories for each skill:

### 1. `Skills_Output/ProblemSkill_output/`:
- **`Problem Files/`**: Central problem repository preserving clean copies of statements with source attribution, dynamic categories, and sample tests.
- **`Solution Files/`**: Multi-language, template-grounded solutions organized as:
  `Solution Files/<Primary Category>/<Subcategory>/` with separate `<ID>_python.py`, `<ID>_java.java`, and `<ID>_derivation.md` files as specified in [`output formating.md`](Skills_Output/ProblemSkill_output/output%20formating.md).

### 2. `Skills_Output/cpbook4_output/`:
- Solutions provide minimal state definitions, variable role tables, state-space trees, invariant checks, and runnable reference implementations in **Python 3** and **Java 21**.
- Houses query manuals and algorithmic roadmaps under [`Skills_Output/cpbook4_output/query/`](Skills_Output/cpbook4_output/query/).

---

## 🧠 The `cpbook4` Agent Skill

The `cpbook4` skill encapsulates comprehensive reference libraries:
- **Foundations & Core Algorithms**: 329 pages  
  *Introduction, Built-in and Custom Linear/Non-linear Data Structures (UFDS, Fenwick Tree, Segment Tree), Core Paradigms (Complete Search, Divide & Conquer, Greedy, Dynamic Programming), and Graph Algorithms (DFS/BFS, MST, SSSP, APSP, Special Graphs).*
- **Advanced Systems & Mathematics**: 352 pages  
  *Mathematics (Number Theory, Combinatorics, Probability, Game Theory, Matrix Power), String Processing (KMP, Suffix Trie/Tree/Array, Hashing, Manacher), Computational Geometry, Advanced Search & DP, Network Flow, Matching, NP-hard Problems, Problem Decomposition, and Rare Topics (Sparse Table, HLD, LCA, FFT/NTT, Simplex).*
- **Total Volume**: 681 pages, ~328,000 words (~436,000 tokens).

### 4-Tier Precision Retrieval & Problem-Solving Architecture

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
│     - CLI Search & Page Extract │           │  Skills_Input/Templates/*.md    │
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

---

## 📂 Repository Structure

```
Science_Of_Coding/
├── .agent/
│   └── skills/                             # Central Agent Skills Hub
│       ├── type of skills.md               # Guide explaining Fixed vs Dynamic resource skills
│       ├── SkillsOnFixedResources/         # Skills bound to static references & books
│       │   └── cpbook4/                    # Algorithmic engineering knowledge base & CLI
│       │       ├── SKILL.md                # Specification & algorithm decision matrix
│       │       ├── SkillArchitecture/      # Technical architecture & agent instructions
│       │       ├── references/             # Table of contents & outline trees
│       │       └── scripts/                # Surgical query CLI (query_cpbook.py)
│       └── SkillsOnDynamicResources/       # Skills bound to dynamic intake & staging
│           └── ProblemSkill/               # Problem intake, classification, & solution skill
│               ├── SKILL.md                # Ingestion protocol & solution triggers
│               ├── SkillArchitecture/      # Lifecycle architecture & execution workflow
│               └── scripts/                # Status discovery & safe cleanup (ingest_manager.py)
├── Skills_Input/                           # Central Input & Reference Space
│   ├── books/                              # Curated coding & reference books library
│   │   ├── Flowchart/                      # Flowchart & programming techniques
│   │   ├── Overall/                        # Comprehensive algorithm references (Part-1.pdf, Part-2.pdf)
│   │   └── Programming Logic/              # Programming logic & loop patterns
│   └── Templates/                          # Methodological blueprints guiding agent problem-solving
│       └── Repetitive Structure Template.md # Step-by-step guide for states, loops, and trees
├── Skills_Output/                          # Central archive for skill-specific outputs
│   ├── README.md                           # Directory overview and output protocols
│   ├── ProblemSkill_output/                # Dedicated output workspace for ProblemSkill
│   │   ├── README.md                       # ProblemSkill output guide
│   │   ├── output formating.md             # Code & derivation formatting specification
│   │   ├── Problem Files/                  # Problem database with full source attribution
│   │   │   ├── README.md                   # Problem metadata schemas and indexing table
│   │   │   ├── problem catagories.docx     # Dynamic 2-tier Category & Subcategory registry
│   │   │   ├── problem formatting.md       # Markdown schema required for all ingested problems
│   │   │   ├── question bank.md            # Master persistent repository of ingested problems
│   │   │   └── Source of Problem/          # Staging area for incoming problems
│   │   │       ├── write here.docx         # 100 colorful structured boxes for links & text
│   │   │       └── put the file here/      # Drop PDFs and offline problem files here
│   │   └── Solution Files/                 # Categorized solutions (Python, Java, Derivations)
│   │       └── README.md                   # Solution archive guide
│   └── cpbook4_output/                     # Dedicated output workspace for cpbook4
│       ├── README.md                       # Output overview marker
│       └── query/                          # Deep-dive algorithmic manuals & query outputs
│           ├── 001_graph_and_tree_learning_roadmap.md
│           └── 002_data_structures_master_manual.md
├── Upcoming Updates/                       # Roadmap, milestone checklist, and feature tracking
│   └── Upcoming Updates.md                 # Serialized progress tracking template
├── chat.md                                 # Persistent project conversation & decision log
└── README.md                               # Repository overview and usage guide
```

---

## 🤖 How to Use the Skills with Agentic AIs

### 1. `cpbook4` (`SkillsOnFixedResources`)
- **Auto-Discovery**: Pre-configured at [`.agent/skills/SkillsOnFixedResources/cpbook4/SKILL.md`](.agent/skills/SkillsOnFixedResources/cpbook4/SKILL.md).
- **Interactive Prompts**:
  - *"Using @skill:cpbook4, I need to design a system for dynamic range minimum queries with updates. Present the available options and ask me which one fits best before writing code."*
  - *"Using cpbook4 and `Skills_Input/Templates/Repetitive Structure Template.md`, decompose this multi-variable nested loop problem step by step."*

### 2. `ProblemSkill` (`SkillsOnDynamicResources`)
- **Auto-Discovery**: Pre-configured at [`.agent/skills/SkillsOnDynamicResources/ProblemSkill/SKILL.md`](.agent/skills/SkillsOnDynamicResources/ProblemSkill/SKILL.md).
- **Interactive Prompts**:
  - *"Check if there are any pending problems to process."*
  - *"Process Box 1 from write here.docx using @skill:ProblemSkill."*
  - *"Solve problem P-001 in question bank.md and format the outputs according to output formating.md."*

---

## 🛠️ CLI Usage: Querying the Books Directly

You or any AI agent can query and extract text from the books on demand using Python (requires `pypdf`):

### 1. Keyword / Phrase Search
Scan either book for specific algorithms, problem references, or keywords:
```bash
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py search --book 1 --query "Fenwick" --limit 5
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py search --book 2 --query "Heavy-Light Decomposition" --limit 3
```

### 2. Surgical Page Extraction
Extract verbatim pages (text, proofs, code) into console or to a file:
```bash
# Print pages 143 to 148 of Book 1 (Segment Tree)
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py extract --book 1 --start 143 --end 148

# Save Dinic's Algorithm pages from Book 2 to a file
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py extract --book 2 --start 156 --end 160 --output dinic.txt
```

---

## 🔒 Copyright & Terms of Use

**Copyright © 2026. All rights reserved.**

This repository and all its contents—including but not limited to the manuals, query guides, architectural designs, agentic templates, decision trees, and code implementations—are proprietary copyrighted material. **No unauthorized copying, distribution, reproduction, modification, or commercial use is permitted without explicit prior written consent from the author.**
