#Given a target amount **n** and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

def rec_coin(target,coin):
    #defaukt coin
    min_coins = target

    if target in coin:
        return 1

    else:
        #for eveyr coin value that is <= my target
        for i in [c for c in coin if c <= target]:
            # adda coin + recursive
            num_coins = 1+ rec_coin(target-i,coin)
            # rest  min_coins
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

coins = [1,5,10]

s = rec_coin(15,coins)

print(s)


#using memoization

def rec_coin_dynam(target,coins,known_resilts):

    #default output totarget
    min_coins = target

    #vbasecase
    if target in coins :
        known_resilts[target] =1
        return 1
    #eturn known result if it happens to be greater then 2
    elif known_resilts[target] > 0:
        return  known_resilts[target]

    else:
        #for ever ycoin valye <= target
        for i in [ c for c in coins if c <= target]:
            num_coins = 1+rec_coin_dynam(target-i,coins,known_resilts)

            if num_coins < min_coins:
                min_coins = num_coins

            #reste he knoe resut
                known_resilts[target] = min_coins
    return known_resilts[target]


target = 15
coins1 = [1,5,10]
known_result = [0]*(target+1)

s1 = rec_coin_dynam(15,coins1,known_result)

print(s1)


#using DP
def coinchange(coins,amount):
    if amount == 0:
        return 0
    if not coins :
        return -1
    maxval = 99999
    dp = [maxval for  i in range(amount+1)]
    dp[0] =0
    for v in range(1,amount+1):
        for c in coins:
            if c <= v:
                dp[v] = min(dp[v],dp[v-c]+1)

    if dp[amount] == maxval :
        return -1

    return dp[amount]


target1 = 15
coins2 = [1,5,10]


s2 = coinchange(coins2,15)
print(s2)

