/*Solution to Day 10 in Coding for 30 Days on Hackerrank.

Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .
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
        int n = scanner.nextInt();
        int max1 = 1, max = 1;
        char prev = '0';
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        String binaryNum = Integer.toBinaryString(n);
        for(int i=0; i<binaryNum.length(); i++){
            if(i==0){
                prev = binaryNum.charAt(0);
            }
            else if(binaryNum.charAt(i)=='1' && prev=='1'){
                max1++;
                prev = binaryNum.charAt(i);
                if(max1>max){
                    max=max1;
                }
            }
            else{
                max1 = 1;
                prev = binaryNum.charAt(i);
            }
        }
        System.out.print(max);
        scanner.close();
    }
}
