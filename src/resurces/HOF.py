def sum(number,fn):
    result = 0
    for i in range(1,number+1):
        result += fn(i)
    return result

def square(x):
    return x**2


result = sum(3,square)

print(result)


import math

result1 = sum(10,math.sqrt)

print(result1)


#funtion that return anothe funtion

def compute(msg):
    if msg == "square":
        return square
    else :
        return math.sqrt


func = compute("square")
result2 = func(10)

print(result2)