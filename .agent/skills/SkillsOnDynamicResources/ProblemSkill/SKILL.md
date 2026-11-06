---
name: ProblemSkill
description: Dedicated skill for managing and formatting problems into question bank.md. Inspects 'Output/ProblemSkill_output/Source of Problem/', parses specified files or box numbers, presents dynamic categories and nested subcategories from 'problem catagories.docx' via Human-in-the-Loop (HITL) prompt, and safely ingests entries into question bank.md without data loss.
---

# Problem Ingestion & Question Bank Control Skill (`ProblemSkill`)

The **`ProblemSkill`** controls the entire lifecycle of problem ingestion into [`Output/ProblemSkill_output/question bank.md`](../../../../Output/ProblemSkill_output/question%20bank.md) from the staging directory ([`Output/ProblemSkill_output/Source of Problem/`](../../../../Output/ProblemSkill_output/Source%20of%20Problem/)).

For complete architectural details and visual flowcharts, consult:
- **Skill Architecture & Guide**: [`SkillArchitecture/README.md`](SkillArchitecture/README.md)

---

## 🎯 Primary Triggers & Capabilities

Activate this skill when:
1. The user mentions `@skill:ProblemSkill` or presses Enter using the skill to check, format, or process problems.
2. The user requests to process a specific file path or document (e.g., in `put the file here/`).
3. The user requests to process a specific box or problem number from `write here.docx` (e.g., *"process Problem #001"*).

---

## 🤝 Human-in-the-Loop (HITL) Category & Subcategory Consultation

Whenever processing a problem (from `write here.docx` or `put the file here/`), the agent **MUST NOT** guess the category or subcategory arbitrarily.

### Dynamic Hierarchical Category Protocol:
1. **Dynamic Category Loading**:
   - The agent reads the real-time categories and nested subcategories from [`Output/ProblemSkill_output/problem catagories.docx`](../../../../Output/ProblemSkill_output/problem%20catagories.docx) using:
     ```bash
     python .agent/skills/SkillsOnDynamicResources/ProblemSkill/scripts/ingest_manager.py --categories
     ```
2. **Interactive Consultation (HITL Prompt)**:
   - Present the dynamically retrieved primary categories and subcategories to the user (e.g. `Dynamic Programming ↳ 2D Grid & Interval DP` or `Graph Algorithms ↳ Shortest Paths (SSSP)`).
   - Use the `ask_question` tool or prompt selection to ask the user to confirm the exact **Category** and **Subcategory**.
3. **Dynamic User Expansion**:
   - The user may update `problem catagories.docx` at any time with new primary categories or new subcategories. The agent dynamically parses the updated hierarchy.

---

## 🚨 CRITICAL RULE: Non-Destructive Ingestion

1. **Selective Ingestion**:
   - When a specific file or box number is requested, the agent **ONLY** processes that specific target. All other files and doc boxes remain completely untouched.
2. **Zero Data Loss Guarantee**:
   - **NEVER** delete any file from `put the file here/` or clear any box in `write here.docx` until the complete entry is 100% formatted and verified on disk in [`question bank.md`](../../../../Output/ProblemSkill_output/question%20bank.md).

---

## 🛠️ Step-by-Step Workflow

### Step 1: Discover Pending Queue
Run the status command to inspect filled boxes and pending files:
```bash
python .agent/skills/SkillsOnDynamicResources/ProblemSkill/scripts/ingest_manager.py --status
```

### Step 2: Target Isolation
- Isolate the requested target (e.g., Box #001 or a specific file like `Recursion_Vs_Iteration_Complete_Codes.pdf`).

### Step 3: HITL Category & Subcategory Selection
- Fetch the dynamic category & subcategory hierarchy from `problem catagories.docx` and consult the user to confirm both the **Primary Category** and **Subcategory**.

### Step 4: Reformat according to `problem formatting.md`
Format into the strict schema defined in [`problem formatting.md`](../../../../Output/ProblemSkill_output/problem%20formatting.md):
- `# Problem [ID]: [Title]`
- `## 📌 Metadata & Source Attribution`
  - **Category**: [Primary Category]
  - **Subcategory**: [Subcategory]
  - **Source**: [Source name]
  - **Source Link / Ref**: [URL or book page]
  - **Difficulty**: [Easy / Medium / Hard]
  - **Target Template**: [Matching template from Input/Templates/, e.g., Input/Templates/Repetitive Structure Template.md]
- `## 📝 Problem Statement`
- `## 📥 Input Specification`
- `## 📤 Output Specification`
- `## 🧪 Sample Tests`
- `## ⚙️ Constraints & System Limits`
- `## 💡 Notes & Special Edge Cases`

### Step 5: Append to `question bank.md` & Update Table
- Add the entry to [`Output/ProblemSkill_output/question bank.md`](../../../../Output/ProblemSkill_output/question%20bank.md).
- Append a new row to the **Master Problem Index** table at the top including both Category and Subcategory.

### Step 6: Atomic Verified Cleanup
- Only after `question bank.md` is updated, remove the processed file from `put the file here/` or clear only that specific box in `write here.docx`.
