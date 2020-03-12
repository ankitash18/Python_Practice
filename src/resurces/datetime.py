import datetime
import pdb #..im[ort debugger


x = [1,2,3]

y =2
z = 3

result = y+z
print(result)


#pdb.set_trace()


#..stirng funtion

s = 'ankita'
s.capitalize()

s.upper()

s.lower()
print(s.count('a'))

print(s.find('a'))

print(s.isalnum())

print(s.isalpha())

print(s.islower())

print(s.endswith('a'))

print(s[-1] == 't')

print(s.split('n'))

#########set method


s = set()

print(s.add(1))

s.add(2)

print(s)

s1 = {1,2,3}

s2= {1,2,3,4}

ss = s2.difference(s1)

se = s1.intersection(s2)

print(ss)
print(se)

sw = s.discard(1)

print(sw)


#######dictonaries method


d ={'k1':1,'k2':2}

{x:x**2 for x in range(10)}

#List#######

k = [1,2,3,4]

k.append(5)

print(k.count(5))

print(k.count(10))

x = [1,2,3]

x.extend([4,5])

print(x)

print(k.index(2))

k.insert(2,6)

print(k)

l = k.pop()

print(l)

k.pop(0)

print(k)

k.remove(6)

print(k)

k.reverse()

print(k)


k.sort()

print(k)


##hoe many times  letter w appears in word

word = 'ttseewwwtwwwy'

print(word.count('w'))