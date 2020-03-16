#find missing lelemt in scrond array cmparing first array

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()



    for num1,num2 in zip(arr1,arr2):

        if num1 != num2:
            return num1

    return arr1[-1]

arr1 = [1,2,3,5,6,7]
arr2 =[3,7,2,1,4,6]

a = finder(arr1,arr2)

print(a)

#using hashmap -default dictoionariy

import collections

def finder1(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1

arr3 = [5,5,7,7]
arr4 =[5,5,7]

b = finder1(arr3,arr4)

print(b)


#linear time n constant space

#exclusive or

def finder3(arr1,arr2):
    result = 0

    #perfomr an XOR between the numberd of array
    for num in arr1+arr2:  #concat array
        result ^=num
        print(result)

    return result

arr5 = [5,5,7,7]
arr6=[5,5,7]

c = finder3(arr5,arr6)

print(c)