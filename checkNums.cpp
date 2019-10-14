/*
Solution to 'Check Nums' Challenge using C++

Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.
*/

#include <iostream>
#include <string>
using std::cout;
using std::cin;

string checkNums(int num1, int num2) {
  if(num1<num2){
    return "true";
  }
  else if(num1>num2){
    return "false";
  }
  else{
    return "-1";
  }
}

int main(void) {
  int input1, input2;
  cout << "Check Sums Challenge" << endl << "Enter num1: ";
  cin >> input1;
  cout << "Enter num2: ";
  cin >> input2;
  cout << "Is num1 less than num2?  " << CheckNums(input1, input2);
  return 0;
}
