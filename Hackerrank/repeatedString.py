# Solution in python for Repeated Strings problem (Interview Preparation Kit > Warm-up Challenges) on Hackerrank.
#
# Given a string, s, of lowercase English letters that is repeated infinitely many times and an integer, n, find and print the number of letter a's in the first n letters of the infinite string.
#
# Sample Input:
# aba
# 10
# Sample Output:
# 7
# Explanation:
# Given the input, we are finding number of a in: abaabaabaa (10 characters created by repeating aba).
# There are 7 occurances in the above.


import math
import re

def repeatedString(s, n):
    find = 'a'
    numOfA = 0

    #corner case where the string is either composed of all a or none
    if len(s) == 1:
        if s == find:
            numOfA = n
        else:
            numOfA = 0

    # Find number of a in the inputed string
    numInS = len(re.findall(find, s))
    length = len(s)

    #Find how many times the string can be fully repeated
    repeat = math.floor(n/length)

    #Left over amount of characters (amount of characters left to fill in n length string)
    remainder = n%length

    # Find number of a in the substring
    sLeft = len(re.findall(find, s[:remainder]))

    # (number of a in string s * number of times s can be fully repeated) + number of a in the left over substring
    numOfA = (numInS*repeat) + sLeft

    return numOfA


s = input("Enter string: ")
n = int(input("Enter length (total characters where s is repeated): "))
print("Number of character a: " + str(repeatedString(s, n)))
