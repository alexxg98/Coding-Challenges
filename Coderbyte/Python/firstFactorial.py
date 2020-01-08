# Solution to 'First Factorial' Challenge using Python
#
# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
# For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.

def firstFactorial(num):
    """Using recursion as the solution"""
    if num == 1:
        return 1
    else:
        return num * firstFactorial(num-1)

# def firstFactorial(num):
#   """Using loops as the solution"""
#     factorial = 1

#     for i in range(1,num+1):
#         factorial *= i
#     return factorial


print("Enter a number: ")
input_num = int(input())
print("Factorial of", input_num, "is", firstFactorial(input_num))
