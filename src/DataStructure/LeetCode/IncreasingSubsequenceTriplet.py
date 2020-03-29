"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Input: [1,2,3,4,5]
Output: true
"""


def   increasingTriplet(nums):
    firstsmall = float('inf')
    secondsmall = float('inf')

    for num in nums:
        if num <= firstsmall:
            firstsmall = num
        elif num <= secondsmall:
            secondsmall = num
        elif num >= secondsmall:
            return  True

    return False

num =  [5,4,3,2,1]

a= increasingTriplet(num)
print(a)
