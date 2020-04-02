"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right




"""


def uniquepath(c,r):
    dp = [[0 for x in range(c)] for x in range(r)]

    for i in range(c):
        dp[0][i] = 1

    for i in range(r):
        dp[i][0] = 1

    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[r - 1][c - 1]

a= uniquepath(3,2)
print(a)