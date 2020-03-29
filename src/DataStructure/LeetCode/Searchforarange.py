"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""


def searchrange(nums,target):
    if not nums:
        return [-1, -1]
    n = len(nums)
    left = -1
    right = -1
    l = 0
    r = n-1
    while l<r:
        mid = (l+r)// 2
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid

    print(nums[l])
    print(l)

    if nums[l] != target:
        return -1,-1

    left = l
    l = left
    r = n-1
    while l<r:
        mid = (l+r)//2+1
        print(mid)
        if nums[mid] == target:
            l = mid
        else:
            r = mid -1

    right = l

    return left,right

#nums = [5,7,7,8,8,10]
nums =[]
d = searchrange(nums,8)
print(d)

def searchRange( nums, target) :
        try:
            first = nums.index(target)
            nums.reverse()
            second = len(nums) - nums.index(target) - 1
            return [first,second]
        except:
            return [-1,-1]

