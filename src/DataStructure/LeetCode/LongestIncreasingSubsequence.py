"""

A subsequence of an array is a subset of the array that maintains temporal order.

It does not have to be contiguous but it might turn out to be contiguous by chance.

 /**
    Explanation for dummies

    initialize
    i = 0 and j = 1 and max = 1
    result array of each element filled as 1 ( Arrays, fill(result, 1)
    //Result array is used to store the count of lojgnest subsequence till the index for each index.
    //Means, result[5] = 3 means, the 5th index has a max LIS of length 3.

    For each j :
        iterate from i to j - 1
        check if arr[i] < arr[j]
        if yes, result[j] = Math.max(result[i] + 1, result[j])
        ^ why you may ask. Cuz, now j contributes to an extra 1 on top of result[i]. If result[j already isnt larger, result[j] = result[i] + 1]
        Morever, keep track of the maximum of result[i] so far.

    Return max
"""


def LIS(nums):
        if (len(nums)==0 or len(nums)==1):
            return len(nums)

        Max = 1
        dp = [1 for i in range(len(nums))]

        for j in range(1,len(nums)):
            for i in range(0,j):
                if nums[j] > nums[i]:
                    dp[j]= max(dp[i]+1,dp[j])
                    Max = max(Max,dp[j])
        return Max


nums = [10,9,2,5,3,7,101,18]
a = LIS(nums)
print(a)