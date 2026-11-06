# Skill Outputs Directory (`Output/`)

Each specialized skill in this project is designed to receive specific inputs and produce structured, reproducible outputs. Under `Output/`, every skill maintains its own isolated output repository (`<SkillName>_output/`).

---

## 📁 Directory Architecture

```
Output/
├── ProblemSkill_output/            # Dedicated output repository for ProblemSkill
│   ├── Source of Problem/          # Ingestion staging area (write here.docx, put the file here/)
│   ├── problem catagories.docx     # Dynamic 2-level taxonomy hierarchy
│   ├── problem formatting.md       # Standard schema & blueprint for problem entries
│   ├── question bank.md            # Canonical central repository of formatted problems
│   └── README.md                   # Problem schema, metadata standards, and indexing protocols
│
└── cpbook4_output/                 # Dedicated output repository for cpbook4
    ├── query/                      # Deep-dive query manuals, decision trees, and roadmaps
    └── README.md                   # Reference-grounded template derivations and query solutions
```

---

## 🎯 Skill-Specific Output Protocols

1. **`Output/ProblemSkill_output/`**:
   - **Input**: Problem statements from multi-box Word documents (`Source of Problem/write here.docx`), external offline PDF companion files (`Source of Problem/put the file here/`), or online problem URLs.
   - **Output**: Cleanly ingested, categorized, and linked problems added to [`question bank.md`](ProblemSkill_output/question%20bank.md), classified dynamically against [`problem catagories.docx`](ProblemSkill_output/problem%20catagories.docx).

2. **`Output/cpbook4_output/`**:
   - **Input**: Algorithmic queries, paradigm inquiries, and code decomposition prompts cross-referenced against the reference library in [`Input/books/`](../Input/books/).
   - **Output**: Verified step-by-step solutions derived using the templates in [`Input/Templates/`](../Input/Templates/), deep-dive query roadmaps in [`query/`](cpbook4_output/query/), complete with state definitions, variable role tables, state-space trees, invariant proofs, and complexity bounds.
