import argparse
import os
import sys
import pypdf

# Ensure standard output handles UTF-8 on Windows terminals safely
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except AttributeError:
        pass

def extract_pages(pdf_path, start_page, end_page, output_file=None):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}", file=sys.stderr)
        sys.exit(1)

    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)

    if start_page < 0:
        start_page = 0
    if end_page >= total_pages:
        end_page = total_pages - 1

    extracted_text = []
    for p in range(start_page, end_page + 1):
        text = reader.pages[p].extract_text() or ""
        header = f"\n--- [Page {p}] ---\n"
        extracted_text.append(header + text)

    result = "\n".join(extracted_text)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Successfully extracted pages {start_page} to {end_page} into {output_file}")
    else:
        print(result)

def search_text(pdf_path, query, max_matches=10):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}", file=sys.stderr)
        sys.exit(1)

    reader = pypdf.PdfReader(pdf_path)
    query_lower = query.lower()
    matches = 0

    print(f"Searching for '{query}' in {pdf_path} (total pages: {len(reader.pages)})...")
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if query_lower in text.lower():
            matches += 1
            print(f"\n[Match #{matches}] Page {idx}:")
            pos = text.lower().find(query_lower)
            start_snippet = max(0, pos - 150)
            end_snippet = min(len(text), pos + len(query) + 150)
            snippet = text[start_snippet:end_snippet].replace("\n", " ")
            print(f"...{snippet}...")
            if matches >= max_matches:
                print(f"\nReached max matches limit ({max_matches}).")
                break

    if matches == 0:
        print("No matches found.")

def main():
    parser = argparse.ArgumentParser(description="Query or extract content from CP4 Book 1 and Book 2 PDFs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract_p = subparsers.add_parser("extract", help="Extract text from a range of pages")
    extract_p.add_argument("--book", type=int, choices=[1, 2], required=True, help="Book number (1 or 2)")
    extract_p.add_argument("--start", type=int, required=True, help="Start page index (0-based)")
    extract_p.add_argument("--end", type=int, required=True, help="End page index (0-based, inclusive)")
    extract_p.add_argument("--output", type=str, default=None, help="Output file path (optional)")

    search_p = subparsers.add_parser("search", help="Search keyword across a book")
    search_p.add_argument("--book", type=int, choices=[1, 2], required=True, help="Book number (1 or 2)")
    search_p.add_argument("--query", type=str, required=True, help="Search phrase or keyword")
    search_p.add_argument("--limit", type=int, default=5, help="Maximum number of matches to return")

    args = parser.parse_args()

    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
    book_file = "Part-1.pdf" if args.book == 1 else "Parttt-2.pdf"
    book_path = os.path.join(workspace_root, book_file)
    if not os.path.exists(book_path):
        alt_path = os.path.join(workspace_root, "Books", f"Part-{args.book}.pdf")
        if os.path.exists(alt_path):
            book_path = alt_path

    if args.command == "extract":
        extract_pages(book_path, args.start, args.end, args.output)
    elif args.command == "search":
        search_text(book_path, args.query, args.limit)

if __name__ == "__main__":
    main()
