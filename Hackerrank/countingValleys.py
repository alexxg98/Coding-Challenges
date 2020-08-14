# Solution in python for Counting Valleys problem (Interview Preparation Kit > Warm-up Challenges) on Hackerrank.
#
# For every step he took, he noted if it was an uphill, U, or a downhill, D step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:
#
# * A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# * A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
#
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
#
# Sample Input:
# n = 8
# s = UDDDUDUU
# Sample Output
# 1
# Explanation:
# Path represented as:
# _/\      _
#    \    /
#     \/\/
# He enters and leaves one valley.


def countingValleys(n, s):
    height = 0
    valleys = 0
    for step in range(n):
        if s[step] == 'D':
            height -= 1
        if s[step] == 'U':
            height += 1
        if height > 0:
            continue
        if (height == 0 and s[step] == 'U' and step != 0):
            valleys += 1
    return valleys

n = int(input("Enter number of steps: "))
s = input("Enter string of " + str(n) + " steps (D or U) with no spaces: ")

print("Number of Valleys: " + str(countingValleys(n, s)))
