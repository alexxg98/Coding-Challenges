/*
Solution to 'First Factorial' Challenge using C++

Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
*/

#include <iostream>
using std::cout;
using std::cin;

//Using recursion as the solution
int FirstFactorial(int num){
  if(num==1){
    return 1;
  }
  return num * FirstFactorial(num-1);
}

/*
//Using loops as the solution
int FirstFactorial(int num){
  for (int i = num-1; i >= 1; i--){
    num *= i;
  }
  return num;
}
*/

int main() {
  int num;
  cout << "Enter a number: ";
  cin >> num;
  cout << FirstFactorial(num);
  return 0;
}
