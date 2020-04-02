"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
"""

def longestPalindromeSubseq(s):
    if (len(s)==0):
        return 0

    revstring = s[::-1]
    m = len(s)
    n = len(revstring)
    print(m)
    print(n)
    #dp = [[]]
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,m+1):
        print(f"here...{i}..{s[i-1]}")
        for j in range(1,n+1):
            print(f"here....j..{j}.{revstring[j - 1]}")
            if s[i-1]==revstring[j-1]:
                dp[i][j]= dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            print(dp[i][j])

    return dp[m][n]



a= longestPalindromeSubseq("bbbab")
print(a)


