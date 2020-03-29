#Given a string, write a function that uses recursion to output a list of all the possible permutations of that string
#pytonh librayr - itertools

#Python provide direct methods to find permutations and combinations of a sequence.
# These methods are present in itertools package.

from itertools import permutations


a = permutations('ABCD',2)

#print(type(a))

#for i in list(a):
#    print(i)


s2 = 'ab'

print(s2[:1] + s2[1+1:])

#without using library


def permute(s):

    out =[]
    #base case
    if len(s) == 1 :
        out = [s]

    else:
        #for every letter in string
        for i,let in enumerate(s):
            print("current letter is ",{let},{i})
            for perm in permute(s[:i] + s[i+1:]):
                print("perm letter is ", {perm})
                out += [let+perm]

    return  out



s1 = permute('abc')

print(s1)