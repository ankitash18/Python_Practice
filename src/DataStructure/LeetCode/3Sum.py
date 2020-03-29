"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


def threesum(nums):
    res =[]
    nums.sort()
    length = len(nums)

    for  i in range(length-2):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i - 1]: continue
        l = i+1
        r = length-1
        while (l <r):
            total = nums[i]+nums[l]+nums[r]
            if total < 0:
                l +=1
            elif total > 0:
                r -=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l <r and nums[l] ==nums[l+1]:
                    l +=1
                while  l <r and nums[r] == nums[r-1]:
                    r -=1
                l +=1
                r -=1
    return res




nums = [-1, 0, 1, 2, -1, -4]
a = threesum(nums)
print(a)


def threeSum1(nums) :
    triplets = set()
    #triplets =[]
    nums.sort()

    print(nums)

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        #if i > 0 and nums[i] == nums[i - 1]:
        #    print(f"here1...{i}...{nums[i]}")
        #    continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            print(f"here2....{i}.{l}...{r}")
            total = nums[i] + nums[l] + nums[r]
            print(f"total...{total}")
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                triplets.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
    return [list(t) for t in triplets]




nums1 = [-1, 0, 1, 2, -1, -4]
b = threeSum1(nums1)
print(b)