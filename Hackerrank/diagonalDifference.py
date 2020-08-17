# Solution in python for Diagonal Difference problem (Algorithms > Warmup) on Hackerrank.
#
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# Sample Input:
# 1 2 3
# 4 5 6
# 9 8 9
# Sample Output:
# 2
# Explanation:
# First diagonal = 1+5+9 = 15
# Second diagonal = 3+5+9 = 17
# Absolute difference = |15-17| = 2


def diagonalDifference(arr):
    diag1 = 0
    diag2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                diag1 += arr[i][j]
            if i+j==(len(arr)-1):
                diag2 += arr[i][j]
    return abs(diag1-diag2)

arr = []
n = int(input("Enter number of rows/cols in the square matrix: "))
print("Enter elements (press enter after each element): ")
for i in range(n):
    innerArr = []
    for j in range(n):
        innerArr.append(int(input()))
    arr.append(innerArr)

print("\nAbsolute diagonal difference of matrix")
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()
print("\nis", diagonalDifference(arr))
