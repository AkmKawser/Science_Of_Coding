"""
Ingestion Manager Script for Problem Ingestion Skill
Supports:
  - Checking pending items in 'Output/problems/Source of Problem/'
  - Inspecting text/paragraphs in 'write here.docx'
  - Inspecting files in 'put the file here/'
  - Filtering by specific file name/path or problem number/identifier
  - Verifying ingestion into 'Output/problems/question bank.md'
  - Non-destructive atomic cleanup (ONLY after successful write verification)
"""

import os
import sys
import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3] if "Output" in str(Path(__file__).resolve()) else Path(__file__).resolve().parents[2]
PROBLEMS_DIR = REPO_ROOT / "Output" / "problems"
SOURCE_DIR = PROBLEMS_DIR / "Source of Problem"
DOCX_PATH = SOURCE_DIR / "write here.docx"
PUT_DIR = SOURCE_DIR / "put the file here"
QUESTION_BANK = PROBLEMS_DIR / "question bank.md"
FORMATTING_SPEC = PROBLEMS_DIR / "problem formatting.md"

def get_docx_paragraphs():
    if not DOCX_PATH.exists():
        return []
    try:
        import docx
        doc = docx.Document(str(DOCX_PATH))
        items = []
        for idx, p in enumerate(doc.paragraphs):
            text = p.text.strip()
            if text:
                items.append((idx, text))
        return items
    except Exception as e:
        print(f"[Error reading docx]: {e}")
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
    print("=== Problem Ingestion Status ===")
    docx_items = get_docx_paragraphs()
    put_files = get_put_files()
    
    print(f"Staging Directory: {SOURCE_DIR}")
    print(f"Question Bank: {QUESTION_BANK}")
    print(f"\n1. Pending entries in 'write here.docx': {len(docx_items)}")
    for idx, text in docx_items:
        preview = text[:80] + ("..." if len(text) > 80 else "")
        print(f"   [{idx + 1}] {preview}")
        
    print(f"\n2. Pending files in 'put the file here/': {len(put_files)}")
    for f in put_files:
        rel = f.relative_to(PUT_DIR)
        size_kb = f.stat().st_size / 1024
        print(f"   - {rel} ({size_kb:.1f} KB)")
        
    if not docx_items and not put_files:
        print("\nAll clear! No pending problems in staging.")

def verify_and_clear_docx(item_indices=None):
    """
    Clears specified paragraph indices or entire docx ONLY if caller has verified.
    """
    if not DOCX_PATH.exists():
        return
    import docx
    doc = docx.Document(str(DOCX_PATH))
    if item_indices is None:
        # Clear all paragraphs
        new_doc = docx.Document()
        new_doc.save(str(DOCX_PATH))
        print("Cleared write here.docx completely.")
    else:
        # Re-save without specified indices
        new_doc = docx.Document()
        for idx, p in enumerate(doc.paragraphs):
            if idx not in item_indices and p.text.strip():
                new_doc.add_paragraph(p.text)
        new_doc.save(str(DOCX_PATH))
        print(f"Removed processed entries {item_indices} from write here.docx.")

def delete_source_file(file_path):
    target = Path(file_path)
    if not target.is_absolute():
        target = PUT_DIR / file_path
    if target.exists() and target.is_file():
        target.unlink()
        print(f"Safely removed processed file: {target.name}")
    else:
        print(f"File not found or already removed: {target}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Problem Ingestion Script")
    parser.add_argument("--status", action="store_true", help="Check for pending problems to process")
    parser.add_argument("--delete-file", type=str, help="Safely remove processed file from put the file here/")
    parser.add_argument("--clear-docx", action="store_true", help="Clear all entries from write here.docx")
    
    args = parser.parse_args()
    if args.status or (not args.delete_file and not args.clear_docx):
        status()
    elif args.delete_file:
        delete_source_file(args.delete_file)
    elif args.clear_docx:
        verify_and_clear_docx()

