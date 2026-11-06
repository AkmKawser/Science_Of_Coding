/**
 * Problem ID: P-3
 * Problem Title: Series Summation: 1 + 3 + 5 + 7 + .............
 * Category: Repetitive Structures
 * Subcategory: Pattern Printing
 * Applied Template: Skills_Input/Templates/Repetitive Structure Template.md
 * Complexity:
 *   Time Complexity: O(N)
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
        // - Minimal State Tuple: (i, total)
        //   * i: Free Stepper, enumerates discrete iteration space [1..N]
        //   * total: Carried Gatherer, accumulates sequence terms across iterations (uses 64-bit long)
        // - Invariant: total = sum(2 * k - 1 for k in 1..i-1) before step i; total = sum(2 * k - 1 for k in 1..i) after step i
        // - Base Case: i = 1, total = 0 (neutral identity for addition)
        // - Transition: (i, total) -> (i + 1, total + 2L * i - 1L)
        // - Progress Metric: (N - i) strictly shrinks by 1 on each pass
        // - Termination: i > N (exits when i = N + 1, total holds sum of first N odd terms = N^2)
        // - Fixed parameter: n (constant constraint)
        // - Derived value: term = 2L * i - 1L (instantaneous odd number formula)
        StringBuilder sequenceBuilder = new StringBuilder();
        long total = 0;

        for (int i = 1; i <= n; i++) {
            long term = 2L * i - 1L;
            if (i > 1) {
                sequenceBuilder.append(" ");
            }
            sequenceBuilder.append(term);
            total += term;
        }

        // Output Specification:
        // Line 1: Sequence terms separated by space
        // Line 2: Sum = <value>
        System.out.println(sequenceBuilder.toString());
        System.out.println("Sum = " + total);
    }
}

