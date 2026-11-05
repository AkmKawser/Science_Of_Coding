---
name: cpbook4
description: Complete algorithmic knowledge base, data structures, and reference skill. Provides algorithms, data structures, paradigms, problem decomposition, code patterns, and direct page-level reference querying capabilities.
---

# Algorithmic Engineering Skill (`cpbook4`)

This skill points directly to the canonical standalone package in the [`skill/`](../../../skill/) directory.

### 🚨 Mandatory Agent Behavioral Rule: Collaborative Design Decisions
**Never generate code blindly without user consensus when architectural choices exist.**
Whenever multiple data structures or algorithmic options are viable:
1. List the candidate approaches with clear Big-O and practical trade-offs.
2. Ask the user for their preferred design choice before generating code.

### Quick Links & Tools
- **Architecture & Operational Guide**: [`skill/ARCHITECTURE.md`](../../../skill/ARCHITECTURE.md)
- **Primary Specification & Decision Matrix**: [`skill/SKILL.md`](../../../skill/SKILL.md)
- **Reference Volumes**:
  - Volume 1: [`skill/books/Overall/Part-1.pdf`](../../../skill/books/Overall/Part-1.pdf)
  - Volume 2: [`skill/books/Overall/Part-2.pdf`](../../../skill/books/Overall/Part-2.pdf)
- **Topic & Page Navigation**: [`skill/references/table_of_contents.md`](../../../skill/references/table_of_contents.md)
- **Query & Page Extractor Utility**:
  ```bash
  python skill/scripts/query_cpbook.py search --book 1 --query "Segment Tree" --limit 3
  python skill/scripts/query_cpbook.py extract --book 1 --start 143 --end 148
  ```
