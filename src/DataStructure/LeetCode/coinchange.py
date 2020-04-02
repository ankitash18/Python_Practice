"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

def coinchange(coins,amount):
    #create dp aaray wirh defaulg value
    dp = [amount+1 for i in range(amount+1)]
    dp[0]=0

    for i in range(len(dp)):
        for coin in coins:
            if(i-coin >=0):
                dp[i]= min(1+dp[i-coin],dp[i])

    return dp[amount] if dp[amount] <= amount else -1


coins = [1, 2, 5]
a= coinchange(coins,11)
print(a)
