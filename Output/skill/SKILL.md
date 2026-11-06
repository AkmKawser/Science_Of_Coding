---
name: ProblemSkill
description: Dedicated skill for managing and formatting problems into question bank.md. Inspects 'Output/problems/Source of Problem/', parses specified files or box numbers, presents dynamic categories from 'problem catagories.docx' via Human-in-the-Loop (HITL) prompt, and safely ingests entries into question bank.md without data loss.
---

# Problem Ingestion & Question Bank Control Skill (`ProblemSkill`)

The **`ProblemSkill`** controls the entire lifecycle of problem ingestion into [`Output/problems/question bank.md`](../../problems/question%20bank.md) from the staging directory ([`Output/problems/Source of Problem/`](../../problems/Source%20of%20Problem/)).

---

## 🎯 Primary Triggers & Capabilities

Activate this skill when:
1. The user mentions `@skill:ProblemSkill` or presses Enter using the skill to check, format, or process problems.
2. The user requests to process a specific file path or document (e.g., in `put the file here/`).
3. The user requests to process a specific box or problem number from `write here.docx` (e.g., *"process Problem #001"*).

---

## 🤝 Human-in-the-Loop (HITL) Topic & Domain Consultation

Whenever processing a problem (from `write here.docx` or `put the file here/`), the agent **MUST NOT** guess the category arbitrarily.

### Dynamic Category Protocol:
1. **Dynamic Category Loading**:
   - The agent reads the real-time categories from [`Output/problems/problem catagories.docx`](../../problems/problem%20catagories.docx) using:
     ```bash
     python Output/skill/scripts/ingest_manager.py --categories
     ```
2. **Interactive Consultation (HITL Prompt)**:
   - Present the dynamically retrieved category list to the user and ask:
     > *"Which problem category/domain from `problem catagories.docx` does this problem belong to?"*
   - Or use the `ask_question` tool with the options populated dynamically from `problem catagories.docx`.
3. **Dynamic User Expansion**:
   - The user may update `problem catagories.docx` at any time with new domains. The agent must always reflect the updated list on demand.

---

## 🚨 CRITICAL RULE: Non-Destructive Ingestion

1. **Selective Ingestion**:
   - When a specific file or box number is requested, the agent **ONLY** processes that specific target. All other files and doc boxes remain completely untouched.
2. **Zero Data Loss Guarantee**:
   - **NEVER** delete any file from `put the file here/` or clear any box in `write here.docx` until the complete entry is 100% formatted and verified on disk in [`question bank.md`](../../problems/question%20bank.md).

---

## 🛠️ Step-by-Step Workflow

### Step 1: Discover Pending Queue
Run the status command to inspect filled boxes and pending files:
```bash
python Output/skill/scripts/ingest_manager.py --status
```

### Step 2: Target Isolation
- Isolate the requested target (e.g., Box #001 or a specific file like `Recursion_Vs_Iteration_Complete_Codes.pdf`).

### Step 3: HITL Category Selection
- Fetch the dynamic category list from `problem catagories.docx` and consult the user to confirm the problem domain.

### Step 4: Reformat according to `problem formatting.md`
Format into the strict schema defined in [`problem formatting.md`](../../problems/problem%20formatting.md):
- `# Problem [ID]: [Title]`
- `## 📌 Metadata & Source Attribution` (Source, link, confirmed category, difficulty, target template)
- `## 📝 Problem Statement`
- `## 📥 Input Specification`
- `## 📤 Output Specification`
- `## 🧪 Sample Tests`
- `## ⚙️ Constraints & System Limits`
- `## 💡 Notes & Special Edge Cases`

### Step 5: Append to `question bank.md` & Update Table
- Add the entry to [`Output/problems/question bank.md`](../../problems/question%20bank.md).
- Append a new row to the **Master Problem Index** table at the top.

### Step 6: Atomic Verified Cleanup
- Only after `question bank.md` is updated, remove the processed file from `put the file here/` or clear only that specific box in `write here.docx`.
