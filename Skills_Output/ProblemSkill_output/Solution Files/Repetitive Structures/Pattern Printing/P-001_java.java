/**
 * Problem ID: P-001
 * Problem Title: Series Summation: 1 + 2 + 3 + 4 + .............
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

        // State Definition:
        // State tuple = (i, total)
        // - i: Stepper (Free variable, controls loop index from 1 to N)
        // - total: Gatherer (Carried variable, accumulates sum of terms; uses long to prevent 32-bit overflow)
        // - n: Fixed value
        StringBuilder sequenceBuilder = new StringBuilder();
        long total = 0;

        for (int i = 1; i <= n; i++) {
            if (i > 1) {
                sequenceBuilder.append(" ");
            }
            sequenceBuilder.append(i);
            total += i;
        }

        // Output Specification:
        // Line 1: Sequence terms separated by space
        // Line 2: Sum = <value>
        System.out.println(sequenceBuilder.toString());
        System.out.println("Sum = " + total);
    }
}
