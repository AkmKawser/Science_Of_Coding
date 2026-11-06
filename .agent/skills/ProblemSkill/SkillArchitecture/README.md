# Skill Architecture & Usage Instructions: `ProblemSkill`

This document defines the technical architecture, execution lifecycle, and human-in-the-loop (HITL) procedures for the **`ProblemSkill`**.

---

## 🏛️ System Architecture

`ProblemSkill` automates the intake, classification, and safe archival of algorithmic problems into [`Output/ProblemSkill/question bank.md`](../../../Output/ProblemSkill/question%20bank.md) without risk of data loss.

```mermaid
flowchart TD
    User([User Invocation: @skill:ProblemSkill]) --> Agent[Agentic AI System]
    
    subgraph StagingArea["Staging Area (Output/ProblemSkill/Source of Problem/)"]
        Docx["write here.docx / write here_new.docx<br/>(100 Clean Themed Boxes for Links & Text)"]
        Files["put the file here/<br/>(PDFs, Book Chapters, Docs)"]
    end
    
    Agent -->|1. Inspects Queue: python ingest_manager.py --status| StagingArea
    
    subgraph TargetScope["Target Isolation"]
        TAll["Process All Items"]
        TSingle["Selective Target:<br/>- Specific Box # (e.g., Box 001)<br/>- Specific File (e.g., sample.pdf)"]
    end
    
    Agent --> TargetScope
    
    subgraph DynamicCategories["Dynamic Category Registry (problem catagories.docx)"]
        CatTree["Hierarchical Categories:<br/>- Primary Categories (e.g., DP, Graphs)<br/>- Nested Subcategories (e.g., 2D Grid, SSSP)"]
    end
    
    TargetScope --> DynamicCategories
    
    DynamicCategories --> HITL{"Human-in-the-Loop (HITL) Prompt:<br/>Ask User to Confirm Category & Subcategory"}
    
    HITL -->|User Selection Confirmed| Formatter["Transform into Markdown Schema<br/>(problem formatting.md)"]
    
    subgraph PersistentDatabase["Permanent Archive"]
        QBank["Output/ProblemSkill/question bank.md<br/>1. Appends Problem Specification<br/>2. Updates Master Index Table"]
    end
    
    Formatter --> PersistentDatabase
    
    PersistentDatabase --> Verification{"Write Verified on Disk?"}
    
    Verification -->|Verified True| AtomicCleanup["Atomic Non-Destructive Cleanup:<br/>- Clear targeted Box ONLY from docx<br/>- Remove targeted File ONLY from put the file here/<br/>*All other boxes and files untouched*"]
    Verification -->|Write Incomplete| Abort["ABORT Cleanup - Zero Data Loss Guarantee"]
```

---

## 📖 Operational Instructions for Agents

### 1. Ingestion Triggers
- General check: `@skill:ProblemSkill` or `"check if there are any problems to process"`
- Targeted Box: `@skill:ProblemSkill process Box 1 from the doc`
- Targeted File: `@skill:ProblemSkill process Recursion_Vs_Iteration_Complete_Codes.pdf`

### 2. Status Discovery via CLI
```bash
python Output/skill/scripts/ingest_manager.py --status
```
Outputs:
- Number of filled boxes in `write here.docx` with text previews.
- Number and file sizes of documents inside `put the file here/`.
- Summary list of dynamic categories.

### 3. Dynamic Category Extraction via CLI
```bash
python Output/skill/scripts/ingest_manager.py --categories
```
Extracts the real-time 2-level hierarchy (Primary Category $\to$ Subcategories) from [`problem catagories.docx`](../../problems/problem%20catagories.docx) to present in the user prompt.

### 4. Interactive HITL Selection Protocol
- **NEVER guess the topic or subcategory**.
- Present the dynamically loaded categories and prompt the user:
  > *"Which Primary Category and Subcategory does this problem belong to?"*
- Await user confirmation before appending to `question bank.md`.

### 5. Formatting Standards ([`problem formatting.md`](../../problems/problem%20formatting.md))
Format each problem entry with:
- Unique Problem ID & Title
- Metadata: Primary Category, Subcategory, Source, Source Link/Ref, Difficulty, Matching Template from `Templates/`
- Problem Statement
- Input / Output Specifications
- Sample Tests with Explanations
- Constraints and Edge Cases

### 6. Zero-Loss Non-Destructive Cleanup
- **Rule**: NEVER delete a source file or clear a docx box until the entry is 100% written and verified inside `question bank.md`.
- **Atomic Scope**: Delete ONLY the processed target file or clear ONLY the processed box; never wipe the whole staging directory.
