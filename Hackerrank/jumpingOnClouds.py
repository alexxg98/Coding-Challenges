# Solution in python for Jumping on Clouds problem (Interview Preparation Kit > Warm-up Challenges) on Hackerrank.
#
# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. She must avoid the thunderheads, denoted in an array of clouds numbered 0 if they are safe or 1 if they must be avoided. The number on each cloud is its index in the list so she must avoid the clouds at those indexes where the value is 1.
#
# Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.
#
# Sample Input:
# 6
# 0 0 0 0 1 0
# Sample Output:
# 3
# Explanation:
# Given:
# Index: 0 1 2 3 4 5
# Value: 0 0 0 0 1 0
# Start: |
# Jump:      |
# Jump:        |
# Jump:            |
# == 3 jumps (0 -> 2 -> 3 -> 5)


def jumpingOnClouds(c):
    cloud = 0
    jumps = 0

    # First and last cloud is always 0 (safe)
    if len(c) == 2:
        jumps = 1
    while cloud < len(c)-2: #second to last cloud
        if c[cloud+2] == 0:
            cloud += 2
            jumps += 1
        else:
            cloud += 1
            jumps += 1

        #last jump
        if cloud == len(c)-2:
            jumps += 1
            break
    return jumps

c = []
n = int(input('Enter array size: '))
print("Enter array of elements (0 or 1) (press enter after each element): ")
for i in range(n):
    num = int(input())
    c.append(num)

print("Minumum number of jumps to win: " + str(jumpingOnClouds(c)))
