# ProblemSkill Outputs (`ProblemSkill_output/`)

This directory houses all outputs produced and managed by the [`ProblemSkill`](../../.agent/skills/SkillsOnDynamicResources/ProblemSkill/SKILL.md).

---

## 📁 Internal Organization

1. **[`Problem Files/`](Problem%20Files/)**:
   - Central archive for problem ingestion, staging, classification, and persistent storage.
   - Contains:
     - `Source of Problem/`: Staging documents (`write here.docx`, `put the file here/`).
     - `problem catagories.docx`: Dynamic taxonomy registry.
     - `problem formatting.md`: Problem entry specification.
     - `question bank.md`: Master question repository.

2. **[`Solution Files/`](Solution%20Files/)**:
   - Hierarchically organized by `Primary Category / Subcategory /`.
   - Separate code files for Python (`<ID>_python.py`) and Java (`<ID>_java.java`).
   - Phased derivation documents (`<ID>_derivation.md`) grounded in templates.

3. **[`Solution formating.md`](Solution%20formating.md)**:
   - Mandatory specification governing naming conventions (unpadded IDs, e.g. `P-1`), directory structure, and derivation phases for all solutions.

