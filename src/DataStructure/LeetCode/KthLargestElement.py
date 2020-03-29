#Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#nums.sort()
		#nums.reverse()

	#	return nums[k-1]

#or sorted(nums)[-k]
#lst = [3,2,1,5,6,4]

lst =[3,2,3,1,2,4,5,5,6]

a  = sorted(lst,reverse=True)

print(a)

print(a[4-1])

import heapq

lst = [3,2,1,5,6,4]

newlist = heapq.nlargest(2,lst)

print(newlist[2-1])