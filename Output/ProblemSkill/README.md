# Problems Archive & Database

Welcome to the **Problems Database** of the *Science of Coding* project.

---

## 📌 Problem Ingestion Pipeline

To easily ingest problems from different sources:

```
                  ┌────────────────────────────────────────┐
                  │              Problem Input             │
                  └───────────────────┬────────────────────┘
                                      │
                 ┌────────────────────┴────────────────────┐
                 │                                         │
                 ▼                                         ▼
   Links, Pasted Text, Notes                  Files, PDFs, Documents
     `write here.docx`                         `put the file here/`
                 │                                         │
                 └────────────────────┬────────────────────┘
                                      │
                                      ▼
                        Agent Ingestion & Conversion
                    (Converts to `problem formatting.md`)
                                      │
                                      ▼
                          `question bank.md`
                     (Persistent Question Archive)
                                      │
                                      ▼
                           Automatic Cleanup
                (Purges `write here.docx` & `put the file here/`)
```

### Components:
1. **[`Source of Problem/`](Source%20of%20Problem/)**: The dedicated incoming staging directory.
   - **[`Source of Problem/write here.docx`](Source%20of%20Problem/write%20here.docx)**: Drop links, copy-pasted problem descriptions, or source URLs across 100 clean boxes.
   - **[`Source of Problem/put the file here/`](Source%20of%20Problem/put%20the%20file%20here/)**: Place PDF chapters, documents, or files containing problem statements here.
2. **[`problem catagories.docx`](problem%20catagories.docx)**: Dynamic registry of problem domains and algorithmic topics. Update this file to dynamically expand the categories offered during interactive HITL prompt selection.
3. **[`problem formatting.md`](problem%20formatting.md)**: The mandatory markdown schema governing how every problem must be formatted.
4. **[`question bank.md`](question%20bank.md)**: The centralized repository storing all ingested, formatted problem statements with full source attribution.
5. **Automatic Cleanup**: Once a problem's content is successfully copied and formatted into `question bank.md`, the agent clears the processed box in `write here.docx` or removes the processed file from `put the file here/`.

---

## 📌 Purpose & Storage Policy

This directory acts as the central, categorized repository for all practice, benchmark, and illustrative problems across algorithmic paradigms.

Whenever a problem is introduced, solved, or referenced—whether extracted from:
1. **Local Markdown Files** (`.md`)
2. **Online Competitive Programming Judges & Platforms** (e.g., Codeforces, LeetCode, CSES, AtCoder, HackerRank, UVa)
3. **Reference Textbooks & Publications** (e.g., Reference Volume 1, Reference Volume 2)

**A complete, self-contained copy of the problem statement MUST be stored in this directory (`Output/ProblemSkill/`) before or alongside solving it.**

---

## 🏷️ Problem File Protocol

Every problem added to this database must follow this structure:

### 1. File Naming Convention
Store problems organized by topic or directly named with descriptive titles:
- `Output/ProblemSkill/<topic>/<problem-title>.md` or `Output/ProblemSkill/<id>_<problem-title>.md`
- Example: `Output/ProblemSkill/repetitive-structures/sliding_window_maximum.md`

### 2. Mandatory Problem Header & Metadata
Each problem file must clearly state its origin and metadata:

```markdown
# [Problem Title]

## Metadata & Source
- **Source**: [Source Name, e.g., Codeforces Round 800 (Div. 2) / LeetCode #239 / Reference Book Vol 1, Page 145]
- **Source URL / Reference**: [URL or Book Volume & Page Number]
- **Topic**: [e.g., Repetitive Structures, Two Pointers, Dynamic Programming]
- **Difficulty**: [Easy / Medium / Hard / Rating]
- **Template Applied**: [Matching template from Templates/, e.g., Templates/Repetitive Structure Template.md]

---

## Problem Statement
[Full description of the problem statement]

## Input Specification
[Input format and constraints]

## Output Specification
[Expected output format]

## Sample Tests
### Sample Input
\`\`\`
[Input data]
\`\`\`

### Sample Output
\`\`\`
[Expected output]
\`\`\`

## Notes & Constraints
- Constraints (e.g., $N \le 10^5$, Time Limit: 2.0s)
- Notes & explanations of sample tests
```

---

## 📑 Problem Index

| ID | Problem Title | Topic | Source | Solution / Template Used |
| :--- | :--- | :--- | :--- | :--- |
| *000* | *(Initial problem index)* | *—* | *Repository Setup* | *[`README.md`](../../README.md)* |

