def square(num):
    return num **2

my_nums= [1,2,3,4,5]

map(square,my_nums)

for item in map(square,my_nums):
    print(item)

a = list(map(square,my_nums))

print(a)


def splicer(mystring):
    if len(mystring) %2 ==0:
        return 'EVEN'
    else:
        return mystring[0]

names =['Andy','Eve','Sally']

myname = list(map(splicer,names))

print(myname)


#########filter##########

def check_even(num):
     return num%2 == 0


my_list = [1,2,3,4,5]

print(list(filter(check_even,my_list)))

#####lamba expression#########

def sq(num):
    result = num**2
    return result


print(sq(3))

###lamba####

squa= lambda num: num**2  ###annonyms funtion

print(squa(2))

print(list(map(lambda num: num**2,my_list)))

print(list(filter(lambda num: num%2 == 0,my_list)))

print(list(map(lambda x:x[0],names)))


#reverse the namems
print(list(map(lambda x:x[:: -1],names)))

#**Write a function that computes the volume of a sphere given its radius.**












