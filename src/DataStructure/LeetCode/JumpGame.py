"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


def jumpgame(nums):
    farhestpoint =0
    if(len(nums) ==1):
        return True
    for i in range(0,len(nums)):
        #//if i has overtaken farthest point or reached a farthest point when jump is 0
        if (i > farhestpoint):
            return False
        #//check if I can do better than the previous farthest point
        if (i+nums[i] > farhestpoint):
            farhestpoint = i+nums[i]

        if (farhestpoint >= len(nums)-1):
            return True

    return False


nums =[2,3,1,1,4]
a = jumpgame(nums)
print(a)

