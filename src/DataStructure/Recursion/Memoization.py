#factorial using memozation

def fact(n):
    factorial_memo = {}

    if n < 2:
        return 1

    if not n in factorial_memo:
        factorial_memo[n] = n * fact(n-1)

    return factorial_memo[n]


a = fact(5)
print(a)

#Note how we are now using a dictionary to store previous results of the factorial function! We are now able to increase the efficiency of this function by remembering old results!\n",


#Keep this in mind when working on the Coin Change Problem and the Fibonacci Sequence Problem.

#We can also encapsulate the memoization process into a class

class memoioze:
    def __init__(self,f):
        self.f  = f
        self.memo ={}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


#Then all we would have to do is
def factorial(k):
    if k < 2:
        return k

    return k * factorial(k-1)

factorial = memoioze(factorial)



h = factorial(4)
print(h)
