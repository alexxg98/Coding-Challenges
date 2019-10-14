/*
Solution to 'Simple Adding' Challenge using Java

Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
*/

import java.util.Scanner;

public class SimpleAdding {
  //Using recursion as the solution
  public static int adding(int num){
    if(num==1){
      return 1;
    }
    return num + adding(num-1);
  }

  //Using loops as the solution
//   public static int adding(int num){
//     for (int i = num-1; i >= 1; i--){
//       num += i;
//     }
//     return num;
//   }

  public static void main(String[] args) {
    System.out.println("Simple Adding Challenge");
    System.out.print("Enter a number: ");
    Scanner input = new Scanner(System.in);
    int number = input.nextInt();
    input.close();
    System.out.println(adding(number));
  }
}
