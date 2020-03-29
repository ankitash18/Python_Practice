



def rangefun(num):
    for i in reversed(range(0,len(num)-1)):
        print(i)

num1 = [1,2,3,4,5]

rangefun(num1)


x = range(3, 20, 2)
for n in x:
  print(n)


def sum_func(s):

    if  (len(str(s))) == 1:
        return s

    else:
        #strip the digits
        #r = n%10
        #n = n /10
        return  s%10 + sum_func(s/10)

c = sum_func(4321)

print(c)