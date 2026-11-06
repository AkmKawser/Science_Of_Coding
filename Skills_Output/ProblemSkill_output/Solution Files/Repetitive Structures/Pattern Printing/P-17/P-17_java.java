/**
 * Problem ID: P-17
 * Problem Title: Pattern Printing: Pyramid #01 (starts with '1')
 * Category: Repetitive Structures
 * Subcategory: Pattern Printing
 * Problem Reference: Skills_Output/ProblemSkill_output/Problem Files/question bank.md#p-17
 * Applied Template: Skills_Input/Templates/Repetitive Structure Template.md
 * Complexity:
 *   Time Complexity: O(N^2)
 *   Space Complexity: O(1) auxiliary space (excluding standard output buffer)
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        if (line == null || line.trim().isEmpty()) {
            return;
        }

        StringTokenizer tokenizer = new StringTokenizer(line);
        if (!tokenizer.hasMoreTokens()) {
            return;
        }
        int n = Integer.parseInt(tokenizer.nextToken());

        // State Machine & Invariant Architecture:
        // - Minimal State Tuple: (i, j)
        //   * i: Free Stepper (Outer Loop), enumerates row index [1..N]
        //   * j: Free Walker (Inner Loop), enumerates column index [1..i]
        // - Fixed parameter: n (constant row limit)
        // - Derived value: val = j (instantaneous column value)
        // - Loop Invariant (Outer): After row i, rows 1..i of the pyramid are printed
        // - Loop Invariant (Inner): In row i, column j prints val = j
        // - Total Leaves (Executions): N * (N + 1) / 2
        StringBuilder out = new StringBuilder();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (j > 1) {
                    out.append("   ");
                }
                out.append(j);
            }
            out.append("\n");
        }

        System.out.print(out.toString());
    }
}

