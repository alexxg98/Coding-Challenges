/*
Solution to 'Check Nums' Challenge using Java

Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.
*/

import java.util.Scanner;

public class CheckNums {
  public static String check(int num1, int num2){
    if(num1<num2){
      return "true";
    }
    else{
      if (num1>num2) {
        return "false";
      }
      else{
        return "-1";
      }
    }
  }

  public static void main(String[] args) {
    System.out.printf("%s%n%s","Check Sums Challenge","Enter num1: ");
    Scanner input = new Scanner(System.in);
    int number1 = input.nextInt();
    System.out.print("Enter num2: ");
    int number2 = input.nextInt();
    input.close();
    System.out.printf("%s%s", "Is num1 less than num2? ==> ", check(number1, number2));
  }
}
