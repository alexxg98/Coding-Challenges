# Solution in python for Get Money Spent problem (Algorithms > Implementation) on Hackerrank.
#
# Given the price lists for the store's keyboards and USB drives, and a budget, find and print the maximum amount of money that can be spent to purchase both items. If you don't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items. -- Spend as much as possible given the budget.
#
# Sample Input:
# b=60
# keyboards=[40,50,60]
# drives=[8,12]
# Sample Output:
# 58
# Explanation:
# Option 1. 40+8 = 48
# Option 2. 40+12 = 52
# Option 3. 50+8 = 58
# Option 4. 50+12 = 62
# Have to buy both items, so the third keyboard is not an option.
# The max price without going over the budget, 60, is option 3 for 58.



def getMoneySpent(keyboards, drives, b):
    max = -1
    for k in keyboards:
        for d in drives:
            cost = k + d
            if (cost <= b and cost > max):
                max = cost
    return max


keyboards = []
drives = []
b = int(input('Enter budget: '))
numKeyboards = int(input("Enter number of keyboard prices: "))
print("Enter costs of keyboards (press enter after each element): ")
for i in range(numKeyboards):
    num = int(input())
    keyboards.append(num)

numDrives = int(input("Enter number of drive prices: "))
print("Enter costs of drives (press enter after each element): ")
for i in range(numDrives):
    num = int(input())
    drives.append(num)

print("Maximum total price: " + str(getMoneySpent(keyboards, drives, b)))
