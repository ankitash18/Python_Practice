def rotate(nums,k):
    while k > 0:
        nums.insert(0, nums.pop())
        k -=1



nums =[1,2,3,4,5,6]

rotate(nums,3)


print(nums)

num = [1,2,3,4,5,6]
#other solution
print(num[-3:] + num[:len(num)-3])

#print(num[:4])




#nums[:len(nums)-2])



#print(nums[:3])

def rotatearray(nums,k):
    #//Rotate the given array by n times toward right
    for i in range(0,k):
        last = nums[len(nums)-1]

        for j in reversed(range(1,len(nums))):
            print(j)
           # print(nums[j])
            nums[j] = nums[j-1]
        nums[0] = last



nums4 =[1,2,3,4,5,6]

rotatearray(nums4,3)

print(nums4)