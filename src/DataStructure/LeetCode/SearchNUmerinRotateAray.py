"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
 */


"""


def search(nums,target):
    if (len(nums) == 0):
        return -1
    if (len(nums) ==1):
        if (nums[0] == target) :
            return 0
        else:
            return -1

    low = 0
    high = len(nums)-1
    while (low <= high):
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[high]:
            if target >= nums[mid] and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if target >= nums[low] and target <= nums[mid]:
                high = mid-1
            else:
                low = mid+1

    return -1


nums = []
a =search(nums,0)
print(a)