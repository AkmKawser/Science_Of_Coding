# Science of Coding

An exhaustive, high-performance algorithmic engineering manual and agentic AI skill system based on *Competitive Programming 4 (CP4)* by Steven Halim, Felix Halim, and Suhendry Effendy.

---

## 📖 Project Overview

The mission of **Science of Coding** is to create a complete, rigorous, and practical manual for mastering the art and science of competitive programming, algorithm design, and software problem-solving.

This repository features:
1. **The Science of Coding Manual**: Structured guides, mathematical proofs, pattern decompositions, and battle-tested code templates for standard and advanced algorithmic problems.
2. **`cpbook4` Agentic Skill**: A portable, self-contained AI agent skill that enables any Agentic AI (Antigravity, Claude Code, Cursor, Copilot, ChatGPT, or custom LLM harnesses) to retrieve exact formulas, theorems, and implementations from both CP4 books without context exhaustion or hallucinations.
3. **`chat.md`**: A chronological record of conversations, architectural decisions, and design sessions.

---

## 🧠 The `cpbook4` Agent Skill

The `cpbook4` skill encapsulates both volumes of *Competitive Programming 4*:
- **Book 1 (`skill/books/Part-1.pdf`)**: 329 pages  
  *Introduction, Built-in and Custom Linear/Non-linear Data Structures (UFDS, Fenwick Tree, Segment Tree), Core Paradigms (Complete Search, Divide & Conquer, Greedy, Dynamic Programming), and Graph Algorithms (DFS/BFS, MST, SSSP, APSP, Special Graphs).*
- **Book 2 (`skill/books/Part-2.pdf`)**: 352 pages  
  *Mathematics (Number Theory, Combinatorics, Probability, Game Theory, Matrix Power), String Processing (KMP, Suffix Trie/Tree/Array, Hashing, Manacher), Computational Geometry, Advanced Search & DP, Network Flow, Matching, NP-hard Problems, Problem Decomposition, and Rare Topics (Sparse Table, HLD, LCA, FFT/NTT, Simplex).*
- **Total Volume**: 681 pages, ~328,000 words (~436,000 tokens).

### Architecture & Mechanics

Loading ~436,000 tokens into an AI context window causes severe degradation and token bloat. The `cpbook4` skill uses a **3-Tier Precision Pipeline** described in detail in [`skill/ARCHITECTURE.md`](skill/ARCHITECTURE.md):

```
                   Task / User Query
                           │
                           ▼
                 Any Agentic AI System
                           │
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
  Tier 1: Instant TOC                 Tier 2: Search
  skill/references/table_of_contents.md  query_cpbook.py search
         │                                   │
         └─────────────────┬─────────────────┘
                           ▼
                  Tier 3: Extraction
               query_cpbook.py extract
                           │
                           ▼
                 skill/books/ (PDFs)
                           │
                           ▼
               100% Grounded Context
              (Zero Hallucination Code)
```

---

## 📂 Repository Structure

```
Science_Of_Coding/
├── .agent/
│   └── skills/
│       └── cpbook4/
│           └── SKILL.md            # Entrypoint for Antigravity native skill discovery
├── skill/                          # Standalone, portable Agent Skill package
│   ├── ARCHITECTURE.md             # Detailed architectural specification & mechanics
│   ├── SKILL.md                    # Universal agent skill instructions & decision matrix
│   ├── books/                      # Original CP4 PDF documents
│   │   ├── Part-1.pdf              # Book 1 (329 pages)
│   │   └── Part-2.pdf              # Book 2 (352 pages)
│   ├── references/                 # Table of contents and machine-readable outline trees
│   │   ├── table_of_contents.md    # Fast topic-to-page navigation map
│   │   ├── toc_book1.json          # Book 1 JSON outline tree
│   │   └── toc_book2.json          # Book 2 JSON outline tree
│   └── scripts/
│       └── query_cpbook.py         # Search and page extraction CLI utility
├── chat.md                         # Persistent project conversation & decision log
├── README.md                       # Repository overview and usage guide
└── LICENSE
```

---

## 🛠️ CLI Usage: Querying the Books

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

## 📜 Authors & References

- **Authors**: Steven Halim, Felix Halim, Suhendry Effendy
- **Official CP4 Portal & Errata**: [https://cpbook.net](https://cpbook.net)
- **Official Companion Code Repository**: [https://github.com/stevenhalim/cpbook-code](https://github.com/stevenhalim/cpbook-code)
