# Problem Formatting Specification (`problem formatting.md`)

This document defines the strict, required schema for converting raw problem sources (links, copied text, PDF book excerpts) into structured entries inside [`Output/problems/question bank.md`](question%20bank.md).

---

## 📋 Markdown Entry Schema

Every problem ingested into `question bank.md` must adhere to the following template:

```markdown
---

<a id="[problem-id-lowercase]"></a>
# Problem [ID]: [Problem Title]

## 📌 Metadata & Source Attribution
- **Problem ID**: [Unique ID or sequential number, e.g., P-001]
- **Problem Title**: [Exact title of the problem]
- **Primary Category**: [Primary Domain from problem catagories.docx, e.g., Dynamic Programming]
- **Subcategory**: [Subcategory from problem catagories.docx, e.g., 2D Grid & Interval DP]
- **Source**: [Source Name, e.g., Codeforces / LeetCode / CSES / Book Volume & Page]
- **Source Link / Reference**: [URL link, PDF filename, or Book Chapter/Page]
- **Difficulty**: [Easy / Medium / Hard / Rating]
- **Target Template**: [Matching template from Templates/, e.g., Templates/Repetitive Structure Template.md]

---

## 📝 Problem Statement
[Full, unaltered text of the problem description and background story.]

---

## 📥 Input Specification
[Detailed format of input data, number of test cases, variable bounds, and constraints.]

---

## 📤 Output Specification
[Exact format expected for output, precision requirements, whitespace rules.]

---

## 🧪 Sample Tests

### Sample 1
#### Input
\`\`\`
[Sample input data]
\`\`\`

#### Output
\`\`\`
[Sample output data]
\`\`\`

#### Explanation
[Explanation of why the output is correct for this sample, if provided or deducible.]

---

## ⚙️ Constraints & System Limits
- Time Limit: [e.g., 1.0 second / 2.0 seconds]
- Memory Limit: [e.g., 256 MB / 512 MB]
- Variable Constraints:
  - $N \le 10^5$
  - Elements: $-10^9 \le A[i] \le 10^9$

---

## 💡 Notes & Special Edge Cases
- [Any specific corner cases mentioned in the source or observed, e.g., $N=1$, empty strings, disconnected graphs.]
```

---

## 🔄 Ingestion & Cleanup Protocol

When processing input from `write here.docx` or `put the file here/`:
1. **Extraction**:
   - Extract raw text, problem links, or PDF excerpts.
2. **Formatting & Linking**:
   - Convert the extracted content into the markdown format defined above, inserting `<a id="p-xxx"></a>` directly above the `# Problem P-XXX:` header.
   - Add a row to the **Master Problem Index** table with both ID and Title formatted as clickable links pointing to the anchor: `| [P-XXX](#p-xxx) | [Problem Title](#p-xxx) | ...`.
   - Append the entry into [`Output/problems/question bank.md`](question%20bank.md).
3. **Purge / Cleanup**:
   - Once successfully extracted and formatted into `question bank.md`, clear the content from `write here.docx` (reset to empty document) or delete/move the source file from `put the file here/`.
