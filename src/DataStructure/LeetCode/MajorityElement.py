"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

using sortig
"""


def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]


nums = [3,2,3]
a= majorityElement(nums)
print(a)


#using hashmap

def majorityElement1(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums) // 2:
            return num
        else:
            dic[num] += 1 