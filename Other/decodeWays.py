# Solution in python to a coding problem found on leetcode
#
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
# To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA".
# Note that "06" cannot be mapped into 'F' since "6" is different from "06".
# Note that "0" doesn't map to a character.
#
# Given a non-empty string num containing only digits, return the number of ways to decode it.
#
# Sample Input: s = "12"
# Sample Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Sample Input: s = "226"
# Sample Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def decodeWays(s, n):
    count = 0
    if (s == "0"):
        return 0
    if (n == 1) or (n == 0):
        return 1

    # if last digit > 0
    # Note that last digit doesn't mean last digit of s, but of the partial string passed into the function (ex: s[:n-1])
    if s[n - 1] > "0":
        count = decodeWays(s, n - 1)

    # if last two digits, x, is 10 <= x < 27
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :
        count += decodeWays(s, n - 2)

    return count

s = input("Enter string: ")
n = len(s)

print(decodeWays(s, n))
