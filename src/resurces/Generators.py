#genrrator in python is a special fucntion -which remebers the state its in between executons.


def undread_number(): #this is called generator funtion coz of yiel;d
    i = 0
    while i <100:
        yield i
        i +=1

#print([x*2 for x in undread_number()])

g = undread_number()
print(next(g))
print(next(g))


my_rnge = range(10)
print(my_rnge)


def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime



#impletment generor class

class hundreadgenerstor:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

my_gen = hundreadgenerstor() #iterator not iterbale
print(my_gen.number)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

#for iterbale define __iter__


class firsthundrediterable:
    def __iter__(self):
        return hundreadgenerstor()


print(sum(firsthundrediterable()))


