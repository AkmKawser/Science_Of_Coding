# Types of Skills in Science of Coding (`type of skills.md`)

This document defines and standardizes the two foundational skill paradigms utilized in the **Science of Coding** engineering framework.

Each skill paradigm serves a specialized operational purpose within the agentic architecture, bridging theoretical foundations with real-world, structured problem solving.

---

```
                       ┌────────────────────────────────────────┐
                       │       SCIENCE OF CODING SKILLS         │
                       └───────────────────┬────────────────────┘
                                           │
                  ┌────────────────────────┴────────────────────────┐
                  │                                                 │
                  ▼                                                 ▼
       TYPE 1: PDF BOOK SKILLS                         TYPE 2: PROBLEM-SOLUTION SKILLS
      (Knowledge Grounding Hub)                        (Intake, Curation & Synthesis)
       Example: `cpbook4`                               Example: `ProblemSkill`
                  │                                                 │
  • Encapsulates complete textbooks                 • Ingests diverse sources (Web, PDFs,
  • Zero-token TOC routing                          • Multi-box input (`write here.docx`)
  • Surgical page extraction CLI                    • Dynamic HITL categorization
  • Mathematical proofs & invariant tables          • Mandatory template-driven solution
```

---

## 📚 Type 1: PDF Book Skills (Comprehensive Knowledge Grounding)

### 1. Concept & Purpose
A **PDF Book Skill** encapsulates an entire reference textbook or publication into a structured, agent-executable capability. Rather than dumping raw, unindexed book contents (which causes severe context degradation and high latency), the skill organizes the entire book into:
1. **Machine-Readable Routing Maps**: Exhaustive table of contents (`references/table_of_contents.md`, `toc_book1.json`, `toc_book2.json`) that allow the AI to pinpoint the exact volume, chapter, section, and page range with **zero token overhead**.
2. **Surgical Page Extraction CLI**: Dedicated Python extraction scripts (`scripts/query_cpbook.py`) that extract only the exact 3–5 pages relevant to the task (proofs, lemmas, data structure definitions, invariant tables).
3. **Collaborative Design Protocol**: Behavioral guardrails requiring the agent to present algorithmic trade-offs (Time/Space complexity, implementation cost) and ask the user for confirmation before coding when multiple algorithms apply.

### 2. Concrete Implementation in Repository
- **`cpbook4`**:
  - Located at: [`.agent/skills/cpbook4/`](cpbook4/)
  - Covers complete reference volumes:
    - *Foundations & Core Algorithms* (`books/Overall/Part-1.pdf`, 329 pages): Linear & non-linear data structures, complete search, greedy, dynamic programming, and graph algorithms.
    - *Advanced Systems & Mathematics* (`books/Overall/Part-2.pdf`, 352 pages): Mathematics, string processing, computational geometry, state-space search, network flow, and advanced data structures.
  - Architecture & Guide: [`.agent/skills/cpbook4/SkillArchitecture/README.md`](cpbook4/SkillArchitecture/README.md).

---

## 🛠️ Type 2: Problem-Solution Skills (Intake, Dynamic Classification & Synthesis)

### 1. Concept & Purpose
A **Problem-Solution Skill** handles the dynamic intake, curation, standardized formatting, and template-guided synthesis of practice and benchmark problems gathered from diverse channels.

Instead of ungrounded or unstructured code generation, the Problem-Solution Skill enforces:
1. **Multi-Source Ingestion**:
   - **Local Word Workbooks**: Staging documents with structured boxes ([`write here.docx`](../../Output/ProblemSkill/Source%20of%20Problem/write%20here.docx)) for links, text, and problem notes.
   - **Document Drops**: Ingestion folders ([`put the file here/`](../../Output/ProblemSkill/Source%20of%20Problem/put%20the%20file%20here/)) for offline PDF books, chapters, and worksheets.
   - **Online Platforms & Judges**: Live competitive programming judges (e.g., Codeforces, LeetCode, CSES, AtCoder, UVa, HackerRank).
2. **Dynamic 2-Tier Hierarchical Classification (HITL)**:
   - Reads real-time domains and subcategories from [`problem catagories.docx`](../../Output/ProblemSkill/problem%20catagories.docx).
   - Prompts the user interactively (Human-in-the-Loop) to verify the **Primary Category** and **Subcategory** before committing entries.
3. **Non-Destructive Archival Protocol**:
   - Reformats raw statements into standardized Markdown schema ([`problem formatting.md`](../../Output/ProblemSkill/problem%20formatting.md)) with explicit lowercase anchors and single-line clickable jump links in the master index table.
   - Enforces zero-data loss: source files and docx entries are **never deleted** until the record is 100% verified inside [`question bank.md`](../../Output/ProblemSkill/question%20bank.md).
4. **Mandatory Template Synthesis**:
   - Couples directly with [`Templates/`](../../Templates/) (e.g., [`Repetitive Structure Template.md`](../../Templates/Repetitive%20Structure%20Template.md)) to guide the agent through phased state derivation, invariant formulation, and verified code implementations in **Python 3** and **Java 21**.

### 2. Concrete Implementation in Repository
- **`ProblemSkill`**:
  - Located at: [`.agent/skills/ProblemSkill/`](ProblemSkill/)
  - Controls problem staging, queue inspection, selective box/file parsing, dynamic category loading, and atomic updates to [`Output/ProblemSkill/question bank.md`](../../Output/ProblemSkill/question%20bank.md).
  - Architecture & Guide: [`.agent/skills/ProblemSkill/SkillArchitecture/README.md`](ProblemSkill/SkillArchitecture/README.md).

---

## ⚖️ Summary Comparison

| Dimension | Type 1: PDF Book Skill | Type 2: Problem-Solution Skill |
| :--- | :--- | :--- |
| **Primary Goal** | Grounding theoretical knowledge & authoritative algorithms | Ingesting, organizing, classifying, & solving problems |
| **Primary Artifact** | Complete reference books (PDFs) & TOC index | Problem staging docs, question bank, & template blueprints |
| **Source Channels** | Comprehensive textbooks & published companion books | Online platforms, offline companion PDFs, copied text, URLs |
| **Core Mechanism** | Zero-token routing & surgical page-level CLI extraction | Dynamic HITL 2-level category prompt & atomic cleanup |
| **Output Delivery** | Invariant tables, mathematical proofs, candidate trade-offs | Structured problem entries, clickable jump index, verified code |
| **Representative Skill**| [`cpbook4`](cpbook4/) | [`ProblemSkill`](ProblemSkill/) |

