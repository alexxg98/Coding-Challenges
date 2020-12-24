// Solution for Java Loops II problem (Java > Introduction) on Hackerrank.
//
// Given t queries in the form of a, b, and n, print the series corresponding to the given a, b, and n values as a single line of n spaces-separated integers.
//
// (a + (2^0)*b), (a + (2^0)*b + (2^1)*b), ... (a + (2^0)*b + (2^1)*b + ... + (2^(n-1))*b)
//
// Sample input
// 2
// 0 2 10
// 5 3 5
//Sample Output:
// 2 6 14 30 62 126 254 510 1022 2046
// 8 14 26 50 98
//Explanation:
// There are two queries.
// First query, first number. 0 + (2^0)*2 = 2
// First query, second number. 0 + (2^0)*2 + (2^1)*2 = 6
// First query, third number. 0 + (2^0)*2 + (2^1)*2 + (2^2)*2 = 6
// ...
// Second query, first number. 5 + (2^0)*3 = 8
// Second query, second number. 5 + (2^0)*3 + (2^1)*3 = 14
// Second query, second number. 5 + (2^0)*3 + (2^1)*3 + (2^2)*3 = 26
// ...

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int temp = a;
            for(int x=0; x<n; x++){
                System.out.printf("%d ", temp+((int)Math.pow(2,x))*b);
                temp = temp+((int)Math.pow(2,x))*b;
            }
            System.out.printf("%n");
        }
        in.close();
    }
}
