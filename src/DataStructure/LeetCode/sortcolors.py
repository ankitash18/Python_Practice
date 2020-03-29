from collections import Counter

def sortcolor(nums):
    count0 =0 #count of zeros
    count1 = 0 #coount of one's
    count2 =0#coumt of 2's

    for i in range(0,len(nums)):
        if nums[i]==0:
            count0 +=1
        elif nums[i] ==1:
            count1 +=1
        elif nums[i] ==2:
            count2 +=1

    print(f"count0 are {count0}")
    print(f"count1 are {count1}")
    print(f"count2 are {count2}")

    for i in range(len(nums)):
        if i < count0:
            nums[i] = 0
        elif (i < count0+count1):
            nums[i] = 1
        else:
            nums[i]= 2


arr =  [2,2,2,1,1,0]
sortcolor(arr)

print(arr)



nums =  [2,0,0,1,1,0]

from collections import Counter

count = Counter(nums)

print(count)