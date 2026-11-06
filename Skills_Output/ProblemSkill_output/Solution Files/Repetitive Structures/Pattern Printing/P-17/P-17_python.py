"""
Problem ID: P-17
Problem Title: Pattern Printing: Pyramid #01 (starts with '1')
Category: Repetitive Structures
Subcategory: Pattern Printing
Problem Reference: Skills_Output/ProblemSkill_output/Problem Files/question bank.md#p-17
Applied Template: Skills_Input/Templates/Repetitive Structure Template.md
Complexity:
  Time Complexity: O(N^2)
  Space Complexity: O(1) auxiliary space (excluding standard output buffer)
"""

import sys

def solve() -> None:
    # Fast I/O reading
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # State Machine & Invariant Architecture:
    # - Minimal State Tuple: (i, j)
    #   * i: Free Stepper (Outer Loop), enumerates row index [1..N]
    #   * j: Free Walker (Inner Loop), enumerates column index [1..i]
    # - Fixed parameter: n (constant row bound)
    # - Derived value: val = j (instantaneous column value)
    # - Loop Invariant (Outer): After row i, rows 1..i of the pyramid are printed
    # - Loop Invariant (Inner): In row i, column j prints val = j
    # - Total Leaves (Executions): N * (N + 1) / 2
    
    for i in range(1, n + 1):
        row_tokens = [str(j) for j in range(1, i + 1)]
        print("   ".join(row_tokens))

if __name__ == "__main__":
    solve()
