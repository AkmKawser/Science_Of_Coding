# Skill Architecture & Usage Instructions: `cpbook4`

This document defines the technical architecture, execution pipeline, and usage guidelines for the **`cpbook4`** skill.

---

## 🏛️ System Architecture

The `cpbook4` skill connects any agentic AI system to deep algorithmic knowledge without suffering from context exhaustion, token window degradation, or hallucinations.

```mermaid
flowchart TD
    User([User Prompt / Engineering Task]) --> Agent[Agentic AI System]
    
    subgraph KnowledgeSources["Tri-Source Knowledge Ingestion"]
        direction TB
        Books["Curated Textbooks (Skills_Input/books/)<br/>- Part-1.pdf (Volume 1, 329 pages)<br/>- Part-2.pdf (Volume 2, 352 pages)"]
        Router["Zero-Token Fast Router<br/>(table_of_contents.md)"]
        CLISearch["Precision Extraction CLI<br/>(python query_cpbook.py)"]
        Router --> CLISearch
        Books --> CLISearch
        
        LLM["Pre-trained Reasoning & Memory"]
        Web["Targeted Web Search & Docs"]
    end
    
    Agent --> KnowledgeSources
    
    subgraph TemplateSynthesis["Mandatory Template Output Layer (Skills_Input/Templates/)"]
        direction TB
        TSelect["Select Matching Topic Template<br/>(e.g., Repetitive Structure Template)"]
        TSteps["Execute Phased Mental Model:<br/>1. Candidate Variable Inventory<br/>2. Role Classification (Free, Carried, Derived, Fixed)<br/>3. Minimal State Formulation<br/>4. State-Space Tree Construction<br/>5. Loop Invariants & Failure Audits"]
        TSelect --> TSteps
    end
    
    KnowledgeSources --> TemplateSynthesis
    
    TemplateSynthesis --> Consensus{"Collaborative Consensus?<br/>(Ask User if Multiple Choices Exist)"}
    Consensus -->|User Confirms Design| CodeOutput["Deterministic, Verified Code Output<br/>(Python 3 & Java 21)"]
```

---

## 📖 Operational Instructions for Agents

### 1. Collaborative Design Check (Mandatory Rule)
- **Rule**: If a problem has multiple viable algorithmic solutions (e.g., Fenwick Tree vs Segment Tree, Dijkstra vs SPFA, Kruskal vs Prim, Memoized DP vs Tabulated DP), the agent **MUST** present the candidate trade-offs (Time, Space, Implementation complexity) and ask the user for their preference before writing code.

### 2. Surgical Retrieval via CLI
Instead of dumping full PDF chapters, use the precision CLI:
```bash
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py search --book 1 --query "Fenwick" --limit 5
python .agent/skills/SkillsOnFixedResources/cpbook4/scripts/query_cpbook.py extract --book 1 --start 143 --end 148
```

### 3. Template Enforcement
Every algorithmic solution generated must strictly follow the phases in [`Skills_Input/Templates/`](../../../../../Skills_Input/Templates/).
