#pylint
#unittest


#instal pylint
#pip install pylint

#decorator

def func():
    return 1

def hellp():
    print("hello")

hellp()

greet = hellp


greet()

def hello(name='jose'):
    print('the hello() function has crted')

    def greet():
        return '\tgreet function insde hello'

    def welcone():
        return '\t this is welcome() inside hello'

    print(" iam going to reutrn a function")

    if name == 'jose':
        return greet
    else:
        return welcone


my_new_func = hello()

print(my_new_func()) ###..function returning fucnton



def coool():

    def supercool():
        return 'i am very cool'

    return supercool()



some_func = coool()

print(some_func)


def hello1():
    return 'Hi Jose'


def other(some_def_func):
    print('other code runs here')
    print(some_def_func())  # passing function as argument


#other(hello1)


#now create a decorator

def new_decorator(original_func):

    def wrap_func():
        print('some extra code,befor eth original func')

        original_func()
        print('some extra code after original func')

    return wrap_func


def func_needs_dec():
    print("I want to be decortor")



func_needs_dec()


decorator = new_decorator(func_needs_dec)

decorator()

##or can do as below


@new_decorator
def func_needs_dec1():
    print("I want to be decortor")



func_needs_dec1()


#######generator#########

def create_cube(n):
    result= []

    for x in range(n):
        result.append(x**3)
    return result


print(create_cube(10)) ## this is keeping entrie list in memory

#using th yield


def create_cube1(n):

    for x in range(n):
        yield x**3

#fibonacci sequence#####
def fib(n):

     a =1
     b =1
     for i in range(n):
        yield a
        a,b = b,a+b


for num in fib(10):
    print(num)




def simple():
    for x in range(3):
        yield x


for num in simple():
    print(num)


g = simple()

print(g)

print(next(g))


print(next(g))

print(next(g))

#print(next(g))


#Create a generator that generates the squares of numbers up to some number N."

def square(n):

    for x in range(n):
        yield  x**2


#Create a generator that yields \"n\" random numbers between a low and high number (that are inputs).

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)




for i in rand_num(1,10,12):
    print(i)



#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.\n",
#If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator. (Multiple answers are acceptable here!)

