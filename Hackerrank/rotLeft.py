# Solution in python for Rotate Left problem (Interview Preparation Kit > Arrays) on Hackerrank.
#
# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
#
# Given an array a of n integers and a number,d , perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
#
# Sample Input:
# n=5
# d=4
# a=[1 2 3 4 5]
# Sample Output:
# [5 1 2 3 4]
# Explanation:
# There are 4 rotations so:
# [1 2 3 4 5] -> [2 3 4 5 1] -> [3 4 5 1 2] -> [4 5 1 2 3] -> [5 1 2 3 4]


def rotLeft(a, d):
    return a[d:] + a[:d]

n = int(input("Enter size of array: "))
d = int(input("Enter number of left rotations: "))
a = []
print("Enter array of size " + str(n) + " (new line for each element): ")
for i in range(n):
    num = int(input())
    a.append(num)

print("New Array: " + str(rotLeft(a, d)))
