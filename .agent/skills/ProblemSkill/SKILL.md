---
name: ProblemSkill
description: Dedicated skill for the Output folder to monitor, selectively extract, and format problems from 'Output/problems/Source of Problem/' into 'question bank.md'. Supports querying pending items, selective ingestion of specific files or problem numbers, and non-destructive atomic cleanup only after verified writes.
---

# Problem Ingestion & Processing Skill (`ProblemSkill`)

The **`ProblemSkill`** manages and automates problem ingestion into [`Output/problems/question bank.md`](../../problems/question%20bank.md) from the staging directory ([`Output/problems/Source of Problem/`](../../problems/Source%20of%20Problem/)).

---

## 🎯 When to Use & Capabilities

Trigger this skill whenever:
1. You mention `@skill:ProblemSkill` to check whether there are any pending problems or source documents to be processed.
2. You mention `@skill:ProblemSkill` with a **specific folder path or filename** (e.g., `Recursion_Vs_Iteration_Complete_Codes.pdf` or a relative path in `put the file here/`).
3. You mention `@skill:ProblemSkill` with a **specific problem number or title** from the `write here.docx` document (e.g., *"process problem 2 from the doc"*).

---

## 🚨 MANDATORY PROTOCOLS

### 1. Selective Processing
- If a specific file or problem number/entry is mentioned, the agent **MUST ONLY** process that specific item into `question bank.md`.
- All other files in `put the file here/` and all other entries in `write here.docx` must remain completely untouched.

### 2. Zero-Loss Non-Destructive Ingestion
- **NEVER destroy, delete, or remove any file or text from `write here.docx` or `put the file here/` until the entry is fully extracted, formatted, and verified inside `question bank.md`**.
- Cleanup is atomic:
  - If a file is processed, delete **only that specific file** after `question bank.md` is updated.
  - If a specific problem number from `write here.docx` is processed, remove **only that specific text/entry** from `write here.docx`, leaving all other entries intact.

---

## 🛠️ Step-by-Step Execution Guide

### Step 1: Check Pending Queue
To discover all pending items awaiting processing:
```bash
python Output/skill/scripts/ingest_manager.py --status
```
This inspects:
- Text paragraphs and URLs inside `Output/problems/Source of Problem/write here.docx`
- Files and PDFs inside `Output/problems/Source of Problem/put the file here/`

### Step 2: Filter by User Target
- **General Check / Process All**: If no specific target is given, list pending items and proceed sequentially.
- **Specific File**: If the user provides a path or filename, target that exact file inside `put the file here/`.
- **Specific Problem Number / Text**: If the user specifies a problem index (e.g., #1, #2) or title from the doc, isolate that paragraph.

### Step 3: Format according to `problem formatting.md`
Transform the target problem into the required format specified in [`Output/problems/problem formatting.md`](../../problems/problem%20formatting.md):
- `# Problem [ID]: [Title]`
- `## 📌 Metadata & Source Attribution` (Source, link/book reference, topic, difficulty, target template)
- `## 📝 Problem Statement`
- `## 📥 Input Specification`
- `## 📤 Output Specification`
- `## 🧪 Sample Tests` (Input, Output, Explanation)
- `## ⚙️ Constraints & System Limits`
- `## 💡 Notes & Special Edge Cases`

### Step 4: Write to `question bank.md` & Update Index
1. Append the formatted problem to [`Output/problems/question bank.md`](../../problems/question%20bank.md).
2. Add a new row to the **Master Problem Index** table at the top of `question bank.md`.

### Step 5: Verified Non-Destructive Cleanup
Verify that the entry in `question bank.md` is complete and saved on disk. Only then:
- For a targeted file:
  ```bash
  python Output/skill/scripts/ingest_manager.py --delete-file "<filename>"
  ```
- For a targeted docx entry:
  Update `write here.docx` to remove only that specific entry while preserving the remaining text.
