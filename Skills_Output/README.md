# Skills Output Hub (`Skills_Output/`)

Each specialized skill in this project is designed to receive specific inputs from [`Skills_Input/`](../Skills_Input/) and produce structured, reproducible outputs. Under `Skills_Output/`, each skill maintains its own isolated output repository (`<SkillName>_output/`).

---

## 📁 Directory Architecture

```
Skills_Output/
├── ProblemSkill_output/            # Dedicated output repository for ProblemSkill
│   ├── Problem Files/              # Problem statements, categories, and question bank
│   │   ├── Source of Problem/      # Ingestion staging (write here.docx, put the file here/)
│   │   ├── problem catagories.docx # Dynamic 2-level taxonomy hierarchy
│   │   ├── problem formatting.md   # Standard schema for problem statements
│   │   ├── question bank.md        # Canonical repository of formatted problems
│   │   └── README.md               # Problem schema standards and guidelines
│   ├── Solution Files/             # Categorized algorithmic solutions by Category/Subcategory
│   │   └── README.md               # Solutions directory guide
│   ├── output formating.md         # Formatting specifications for code & derivations
│   └── README.md                   # ProblemSkill output overview
│
└── cpbook4_output/                 # Dedicated output repository for cpbook4
    ├── query/                      # Deep-dive query manuals, decision trees, and roadmaps
    └── README.md                   # Reference-grounded template derivations and query solutions
```

---

## 🎯 Skill-Specific Output Protocols

1. **`Skills_Output/ProblemSkill_output/`**:
   - **Problem Files**: Ingested, classified against `problem catagories.docx`, and archived in [`question bank.md`](ProblemSkill_output/Problem%20Files/question%20bank.md).
   - **Solution Files**: Template-derived solutions structured by Primary Category and Subcategory in separate Python (`<ID>_python.py`) and Java (`<ID>_java.java`) files, alongside `<ID>_derivation.md`, adhering to [`output formating.md`](ProblemSkill_output/output%20formating.md).

2. **`Skills_Output/cpbook4_output/`**:
   - **Input**: Algorithmic queries and code decomposition prompts cross-referenced against [`Skills_Input/books/`](../Skills_Input/books/).
   - **Output**: Verified solutions derived using [`Skills_Input/Templates/`](../Skills_Input/Templates/) and query manuals in [`query/`](cpbook4_output/query/).
