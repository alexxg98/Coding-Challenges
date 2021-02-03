coins = [25, 10, 5]
coins2 = [9, 6, 5, 1]
v = 30
v2 = 11

def minCoins(coins, value):
    """ Given a list of coins and a value, return the minimum number of coins needed to get to the value. This solution assumes the list of coins is sorted with no repeats. """

    count = 0

    if (len(coins) == 0 or value == 0):
        return 0

    for coin in coins:
        while value >= coin:
            value -= coin
            count += 1
    return count


# print("Enter list of coins (enter for next coin, enter twice to end list): ")
# try:
#     list_coins = []
#
#     while True:
#         list_coins.append(int(input()))
#
# # if the input is not-integer, just print the list
# except:
#     pass
#
# value = int(input("Enter a value: "))
#
# print(minCoins(list_coins, value))

print(minCoinsDP(coins, v))
print(minCoinsDP(coins2, v2))
