"""
Ingestion & Category Manager Script for ProblemSkill
Supports:
  - Checking pending items in 'Output/problems/Source of Problem/'
  - Inspecting boxes in 'write here.docx'
  - Inspecting files in 'put the file here/'
  - Reading dynamic categories and nested subcategories from 'Output/problems/problem catagories.docx'
  - Formatting entries into 'Output/problems/question bank.md' with chosen Category & Subcategory
  - Safe, non-destructive atomic cleanup ONLY after verified writes
"""

import os
import sys
import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
PROBLEMS_DIR = REPO_ROOT / "Output" / "problems"
SOURCE_DIR = PROBLEMS_DIR / "Source of Problem"
DOCX_PATH = SOURCE_DIR / "write here.docx"
PUT_DIR = SOURCE_DIR / "put the file here"
CATEGORIES_DOCX = PROBLEMS_DIR / "problem catagories.docx"
QUESTION_BANK = PROBLEMS_DIR / "question bank.md"
FORMATTING_SPEC = PROBLEMS_DIR / "problem formatting.md"

def load_categories():
    """
    Dynamically loads categories and subcategories from 'Output/problems/problem catagories.docx'.
    Returns a dict: { PrimaryCategory: [ (Subcategory, Description), ... ] }
    """
    if not CATEGORIES_DOCX.exists():
        return {
            "Repetitive Structures": [("Single Loop", "Linear scans"), ("Nested Loops", "Grids & dependent ranges")],
            "Dynamic Programming": [("1D Linear", "Sequences"), ("2D Grid", "Grids/Intervals")],
            "Graph Algorithms": [("Traversals", "DFS/BFS"), ("Shortest Paths", "Dijkstra/Bellman-Ford")]
        }
    try:
        import docx
        doc = docx.Document(str(CATEGORIES_DOCX))
        hierarchy = {}
        if doc.tables:
            table = doc.tables[0]
            # Check column count
            for row in table.rows[1:]:  # skip header
                cells = [c.text.strip() for c in row.cells]
                if len(cells) >= 4:
                    # Format: #, Primary Category, Subcategory, Description
                    primary = cells[1]
                    subcat = cells[2].replace("↳", "").strip()
                    desc = cells[3]
                    if primary not in hierarchy:
                        hierarchy[primary] = []
                    if subcat and (subcat, desc) not in hierarchy[primary]:
                        hierarchy[primary].append((subcat, desc))
                elif len(cells) >= 3:
                    primary = cells[1]
                    desc = cells[2]
                    if primary not in hierarchy:
                        hierarchy[primary] = []
                    hierarchy[primary].append((primary, desc))
        return hierarchy
    except Exception as e:
        print(f"[Warning loading categories]: {e}")
        return {"General": [("Algorithms", "Standard algorithms")]}

def list_categories(detailed=True):
    hierarchy = load_categories()
    print("=== Dynamic Problem Categories & Subcategories (from problem catagories.docx) ===")
    for idx, (primary, subcats) in enumerate(hierarchy.items(), 1):
        print(f"[{idx:02d}] 📁 {primary}")
        if detailed:
            for s_idx, (sub_name, desc) in enumerate(subcats, 1):
                print(f"      ↳ [{idx}.{s_idx}] {sub_name} - {desc}")
    return hierarchy

def get_docx_boxes():
    if not DOCX_PATH.exists():
        return []
    try:
        import docx
        doc = docx.Document(str(DOCX_PATH))
        boxes = []
        for idx, table in enumerate(doc.tables):
            hdr = table.cell(0, 0).text.strip()
            body = table.cell(1, 0).text.strip()
            if body:
                boxes.append((idx + 1, hdr, body))
        return boxes
    except Exception as e:
        print(f"[Error reading docx boxes]: {e}")
        return []

def get_put_files():
    if not PUT_DIR.exists():
        return []
    files = []
    for f in PUT_DIR.iterdir():
        if f.is_file() and f.name.lower() != "readme.md":
            files.append(f)
        elif f.is_dir():
            for sub_f in f.rglob("*"):
                if sub_f.is_file() and sub_f.name.lower() != "readme.md":
                    files.append(sub_f)
    return files

def status():
    print("=== Problem Ingestion Status (ProblemSkill) ===")
    boxes = get_docx_boxes()
    put_files = get_put_files()
    
    print(f"Staging Directory: {SOURCE_DIR}")
    print(f"Question Bank:     {QUESTION_BANK}")
    print(f"Categories File:   {CATEGORIES_DOCX}")
    
    print(f"\n1. Filled Boxes in 'write here.docx': {len(boxes)}")
    for num, hdr, body in boxes:
        preview = body.replace("\n", " ")[:70] + ("..." if len(body) > 70 else "")
        print(f"   [Box #{num:03d}] {hdr} -> {preview}")
        
    print(f"\n2. Files in 'put the file here/': {len(put_files)}")
    for f in put_files:
        rel = f.relative_to(PUT_DIR)
        size_kb = f.stat().st_size / 1024
        print(f"   - {rel} ({size_kb:.1f} KB)")
        
    if not boxes and not put_files:
        print("\nAll clear! No pending problems in staging.")
        
    print("\n--- Available Category & Subcategory Registry ---")
    list_categories(detailed=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Problem Ingestion Script")
    parser.add_argument("--status", action="store_true", help="Check for pending problems to process")
    parser.add_argument("--categories", action="store_true", help="List dynamic problem categories and subcategories")
    args = parser.parse_args()
    
    if args.categories:
        list_categories(detailed=True)
    else:
        status()
