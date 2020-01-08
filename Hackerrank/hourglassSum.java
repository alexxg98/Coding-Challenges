/*
Solution in Java for Day 11: 2D Arrays in 30 Days of Coding on Hackerrank.

Calculate the hourglass sum for every hourglass in the 2D array, then print the maximum hourglass sum.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19

Explanation

Array contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
      /*For n sized, user input arrays
        int rows, cols;
        System.out.print("Number of rows: ");
        rows = scanner.nextInt();
        System.out.print("Number of columns: ");
        cols = scanner.nextInt();
        int[][] arr = new int[rows][cols];
      */
        int[][] arr = new int[6][6];
        int sum = (int)Double.NEGATIVE_INFINITY, tempSum = 0;
        //for (int i = 0; i < rows; i++) {
        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            //for (int j = 0; j < cols; j++) {
            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }
        //for (int i=0; i<cols-2;i++){
        for (int i=0; i<4;i++){
          //for (int j=0; j<cols;j++){
            for (int j=0; j<4;j++){
                tempSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
                if(tempSum>sum){
                    sum = tempSum;
                }
            }
        }
        System.out.print(sum);

        scanner.close();
    }
}
