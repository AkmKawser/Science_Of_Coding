"""
Problem ID: P-1
Problem Title: Series Summation: 1 + 2 + 3 + 4 + .............
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
    
    # State Definition:
    # State tuple = (i, total)
    # - i: Stepper (Free variable, controls loop index from 1 to N)
    # - total: Gatherer (Carried variable, accumulates sum of terms)
    # - n: Fixed value
    
    terms = []
    total = 0
    
    for i in range(1, n + 1):
        terms.append(str(i))
        total += i
    
    # Output Specification:
    # Line 1: Sequence terms separated by space
    # Line 2: Sum = <value>
    print(" ".join(terms))
    print(f"Sum = {total}")

if __name__ == "__main__":
    solve()

