/*
Solution to 'First Factorial' Challenge using Java

Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
*/

import java.util.Scanner;

public class firstFactorial {
  public static int factorial(int num){
    if(num==1){
      return 1;
    }
    return num * factorial(num-1);
  }

//   public static int factorial(int num){
//     for (int i = num-1; i >= 1; i--){
//       num *= i;
//     }
//     return num;
//   }

  public static void main(String[] args) {
    System.out.print("Enter a number: ");
    Scanner input = new Scanner(System.in);
    int number = input.nextInt();
    input.close();
    System.out.println(factorial(number));
  }
}
