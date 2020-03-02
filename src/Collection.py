my_list = [1,2,3,4,5]

my_list[0]

new_list = my_list + [6,7]

print(new_list)

new_list[0] = 8

print(new_list) #list is mutable

new_list.append(10)

print(new_list)

sort_lsit = sorted(new_list)

print(sort_lsit)


print(sort_lsit.pop())

print(sort_lsit)

print(sort_lsit.reverse())


list1 = [4,7,1,2,8,9]

list1.sort()

list2 = list1

print(list2)


lst =['a','b','c']
print(lst[1:])

##########dictoriniers

dict = {'key1':'value1','key2':'value2'}

print(dict['key2'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}

print(d['k1'])

print(d['k2'])

print(d['k3'])

print(d['k3']['insidekey'])

print(d.keys())
print(d.values())

print(d.items())
########tuples

t =(1,2,3)

mylist = [1,2,3]

print(type(t))

print(type(mylist))

t1 = ('a','b','a')

print(t1.count('a'))

print(t1.count('b'))

print(t1.index('b'))

###########sets

myset =set()
myset.add(4)

print(myset)

print(myset)

set1 = set('parallel')

print(set1)

###########boolean

yes = True

print(yes)

print(type(yes))

print(1 > 2)


###############fie

myfile = open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\societie_general_interview.txt')

#print(myfile.read())

with open('NEWFILE.txt',mode = 'w') as new_file:
   new_file.write('Hi...')
    #print(contents)

#myfile.close()