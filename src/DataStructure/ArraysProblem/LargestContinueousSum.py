#maxiumb sum sub array or largest continuos sum

def large_sum_cont(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]: #skip first elemnt as it is alrady set
        current_sum = max(current_sum + num,num)

        max_sum = max(current_sum,max_sum)

    return max_sum

arr = [1,2,-1,3,4,10,10,-10,-1]

a = large_sum_cont(arr)
print(a)

