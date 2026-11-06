"""
Problem ID: P-2
Problem Title: Series Summation: 2 + 4 + 6 + 8 + .............
Category: Repetitive Structures
Subcategory: Pattern Printing
Applied Template: Skills_Input/Templates/Repetitive Structure Template.md
Complexity:
  Time Complexity: O(N)
  Space Complexity: O(1) auxiliary space
"""

import sys

def solve() -> None:
    # Fast I/O reading
    input_text = sys.stdin.read().split()
    if not input_text:
        return
    
    n = int(input_text[0])
    
    # State Machine & Invariant Architecture:
    # - Minimal State Tuple: (i, total)
    #   * i: Free Stepper, enumerates discrete iteration space [1..N]
    #   * total: Carried Gatherer, accumulates sequence terms across iterations
    # - Invariant: total = sum(2 * k for k in 1..i-1) before step i; total = sum(2 * k for k in 1..i) after step i
    # - Base Case: i = 1, total = 0 (neutral identity for addition)
    # - Transition: (i, total) -> (i + 1, total + 2 * i)
    # - Progress Metric: (N - i) strictly shrinks by 1 on each pass
    # - Termination: i > N (exits when i = N + 1, total holds sum of first N even terms)
    # - Fixed parameter: n (constant constraint)
    # - Derived value: term = 2 * i (instantaneous even number formula)
    
    terms = []
    total = 0
    
    for i in range(1, n + 1):
        term = 2 * i
        terms.append(str(term))
        total += term
    
    # Output Specification:
    # Line 1: Sequence terms separated by space
    # Line 2: Sum = <value>
    print(" ".join(terms))
    print(f"Sum = {total}")

if __name__ == "__main__":
    solve()

