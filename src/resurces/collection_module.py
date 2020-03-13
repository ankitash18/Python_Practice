from  collections import Counter

l = [1,1,1,1,2,2,2,2,3,4,4,5]

print(Counter(l))

s = 'adsdaaaaaadddddddsssssssttt'

print(Counter(s))


s1 = 'How many times does each word shows up in the senetence  then shows up'


word  = s1.split()

c = Counter(word)


print(type(word))

print(word)

print(c)

print(c.most_common(3))


# common pattens when using all counte object

print(sum(c.values())) # total of all values

print(list(c))  #list unique elements

print(set(c)) #conver to tset

print(dict(c))   # conver tot a regular dictonay


print(c.items()) #convert to a list of  item,count pair


#########default dict###########
from collections import  defaultdict

d = {'k1':1}

print(d['k1'])

d1 = defaultdict(object)

d1['one']


for item in d1:
    print(item)

d2 = defaultdict(lambda : 0)

print(d2['one'])

d2['two'] =2

print(d2)

#######order dict########

#retian order

d4 ={}

d4['a'] = 1

d4['b'] = 2

d4['c'] = 3

#print(d4)

for (k,v) in d4.items():
    print(k)


from collections import OrderedDict

sr = OrderedDict()

sr['a'] = 1
sr['b'] = 2
sr['c'] = 3

for (k,v) in sr.items():
    print(k)


dict1 = {}
dict1['e'] = 5
dict1['f'] = 6


dict2 ={}

dict2['e'] = 5
dict2['f'] = 6

print(dict1 == dict2)

######names tuple####

t = (1,2,3)

print(t[0])

(t1,t2,t3) = (1,2,3)

print(t1)

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

print(type(Dog))

sam = Dog(age =2,breed = 'lab',name = 'samy')

print(sam.age)


####..regualr expression

import re

patterns = ['term1','term2']

text = 'this is the string with term1 but not other term'

for pattern in patterns:
    print(f"searhcing for {pattern} ")

    if re.search(pattern,text):
        print("matc hwas found")

    else:
        print("no match found")


match = re.search(patterns[0],text)

print(match)

split_term = '@'

phrase = 'wht is your email,is it hello@gmail.com'

print(re.split(split_term,phrase))

print(re.findall('match','here is one match,here is other match'))

def multi_re_find(patterns,phrase):
    #Takes in a list of regex patterns
   # Prints a list of all matches
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))


multi_re_find(patterns,phrase)