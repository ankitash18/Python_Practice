def removeduplicates(nums):
    n = len(nums)
    j = 1

    if n ==0:
        return 0

    if n ==1:
        return 1

    for i in range(1,n):
        if nums[i-1] != nums[i]:
            nums[j] = nums[i]
            j +=1

    return  j

nums =[1,1,2]

a = removeduplicates(nums)
print(a)