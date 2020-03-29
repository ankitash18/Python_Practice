#implement fibonicc using recusive,iterstive,memoization(Dynamic programming)

def fib_rec(n):

    if n ==0 or n ==1:
        return n
    elif n == 2:
        return 1

    else:
        return fib_rec(n-2) + fib_rec(n-1)


a = fib_rec(10)

print(a)

#iteratvie

def fib_iter(n):
    a ,b= 0,1
    #c = a+b


    for i in range(1,n):
        c = a + b
        a = b
        b = c


    return c

s = fib_iter(10)
print(s)



#using dynamic programming
#cache informaiton

cache = [None]*(55)
def fib_memo(n):

     #base case
    if n ==0 or n == 1 :
        return n
    #chedk cache
    if cache[n]!= None:
        return cache[n]

    #keep setting cache
    cache[n] = fib_memo(n-1) + fib_memo(n-2)


    return cache[n]


s2 = fib_memo(12)

print(s2)
