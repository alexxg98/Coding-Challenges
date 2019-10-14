# Solution to 'Simple Adding' Challenge using Python
#
# Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.

def simpleAdding(num):
    """Using recursion as the solution"""
    if num == 1:
        return 1
    else:
        return num + simpleAdding(num-1)

# def simpleAdding(num):
#   """Using loops as the solution"""
#     add = 0

#     for i in range(1,num+1):
#         add += i
#     return add

print("Simple Adding Challenge")
print("Enter a number: ")
input_num = int(input())
print("Factorial of", input_num, "is", simpleAdding(input_num))
