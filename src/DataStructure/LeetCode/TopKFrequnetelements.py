def topk(nums,k):

    d={}
    for num in nums:
        if num in d:
            d[num] +=1
        else:
            d[num] =1

    return sorted(d,key=d.get,reverse=True)[:k]



nums = [1,1,1,2,2,3]

a = topk(nums,3)

print(a)