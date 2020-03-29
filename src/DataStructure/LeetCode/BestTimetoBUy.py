def maxProfit(prices):

    if len(prices) == 0:
        return 0

    maxprofit = 0

    for i in range(0,len(prices)-1):
        if prices[i] < prices[i+1]:
            maxprofit += prices[i+1] - prices[i]

    return maxprofit

prices = [7,1,5,3,6,4]

a = maxProfit(prices)

print(a)