
"""
/*
 peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
 */
"""

#using loop - o(n)

def peakelement(nums):

    for i in range(0,len(nums)):
        if nums[i] > nums[i+1]:
            return i


    return nums[len(nums)-1]


nums =  [1,2,3,1]
a = peakelement(nums)
print(a)


#using binary search - o(logn)

def peakelement1(nums):
    lo=0
    hi = len(nums)-1

    while lo < hi:
        mid = lo + (hi-lo)//2

        if nums[mid] > nums[mid+1]:
            hi = mid
        if nums[mid] < nums[mid+1]:
            lo = mid+1

    return lo




nums1 =  [1,2,3,1]
b = peakelement1(nums1)
print(b)
