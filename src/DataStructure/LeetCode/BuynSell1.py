"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Input: [7,1,5,3,6,4]
Output: 5
"""

def maxProfit(prices):
    minprice = float('inf')
    maxProfit = 0
    for price in prices:
        currentprofit = price - minprice
        minprice = min(price,minprice)
        maxProfit = max(currentprofit,maxProfit)

    return maxProfit


prices = [7,1,5,3,6,4]
a = maxProfit(prices)
print(a)
