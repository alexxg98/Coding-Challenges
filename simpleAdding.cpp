/*
Solution to 'Simple Adding' Challenge using C++

Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
*/

#include <iostream>
using std::cout;
using std::cin;

//Using recursion as the solution
int SimpleAdding(int num){
  if(num==1){
    return 1;
  }
  return num + SimpleAdding(num-1);
}

/*
//Using loops as the solution
int FirstFactorial(int num){
  for (int i = num-1; i >= 1; i--){
    num += i;
  }
  return num;
}
*/

int main() {
  cout << "Simple Adding Challenge" << endl;
  int num;
  cout << "Enter a number: ";
  cin >> num;
  cout << SimpleAdding(num);
  return 0;
}
