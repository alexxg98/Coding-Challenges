# Solution in python for Sock Merchant problem (Interview Preparation Kit > Warm-up Challenges) on Hackerrank.
#
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# Sample Input:
# n = 7
# ar = [1,2,1,2,1,3,2]
# Sample Output:
# 2
# Explanation:
# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.


def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    i = 0
    while i < n-1:
        if (ar[i] == ar[i+1]):
            pairs = pairs + 1
            i += 2
        else:
            i += 1

    return pairs

ar = []
n = int(input('Enter array size: '))
print('Enter ' + str(n) + ' elements (press enter after each element): ')
for i in range(n):
    num = int(input())
    ar.append(num)

print("Number of matching pairs: " + str(sockMerchant(n, ar)))
