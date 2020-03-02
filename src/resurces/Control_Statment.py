a =11

#### if else statment

if a ==10:
    print('yes it is 10')
else:
    print('it is not 10')



    if (3 > 2):
        print('its true')


_name_ = 'ankita'

print(_name_)

my_iterbale = [1,2,3,4,5,6,7,8,9,10]

#####for loop
for item in my_iterbale:
    print(item)

##check for even number
for num in my_iterbale:
    if (num %2 ==0):
        print(f' even number: {num}')
    else:
        print(f'odd number : {num}')

list_sum = 0

for num in my_iterbale:
    list_sum += num
### notice indentation..it should be inline with for if have to run outside loop
print(list_sum)


my_string = 'hello world'

for letter in my_string:

    print(letter)

for _ in 'Hello World':
    print('cool')

#### tuple loop


tup =(1,2,3)

for item in tup:
    print(item)

my_list =[(1,2),(3,4),(5,6)]


for item in my_list:
    print(item)

###### tuple unpacking
for (a,b) in my_list:
    print(a)
    print(b)



d1 = {'k1':1,'k2':2,'k3':3}
for item in d1:
    print(item)

d1 = {'k1':1,'k2':2,'k3':3}
for key,value in d1.items():
    print(value)

    #####################while loop########################

    ### dictonries are unordered
 ##### array ,import is needed

x = 0

while x < 5:
    print(f'the current value is {x}')
    x = x+1
else:
    print('x is not less then 5')

######break,continue,pass keyword in python


x1 = [1,2,3,4]

for item in x1:
    pass ## do nothing

print('end of my script')


mystring = 'Sammy'

for letter in mystring:
    if (letter == 'a'):
        continue
    print(letter)


for letter in mystring:
    if (letter == 'a'):
        break
    print(letter)

x = 0

while (x < 5):
    if( x ==2):
        break
    print(x)
    x +=1


###############userful operators##################

###### range - bulit in opertor############
### range is generator

mylist =[1,2,3]

for num in range(3,10,2):
    print(num)


#######enumerate function#############

index_count = 0

word ='abcde'

for letter in word:

   print(word[index_count])
   index_count +=1

   for index,letter in enumerate(word):
       print(index)
       print(letter)

#######zipp function ..zip tohgether two list#########

myist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for item in zip(myist1,mylist2):
    print(item)  #### returning tuple

list(zip(myist1,mylist2))

print('x' in [1,2,3])  ### contain method


print('mykey' in {'mykey':34})

d= {'mykey':34}

print(34 in d.keys())


mylist4 =[1,2,3,4,5]

print(min(mylist4))

print(max(mylist4))

from random import shuffle

mylist =[1,2,3,4,5,6,7,8,9]


shuffle(mylist)

print(mylist)

from random import randint

mynum = randint(0,10)

print(mynum)

########user input##########

#result = input('enter a number here: ')

#print(result)

#result = int(input('enter a number here: '))


#######List Comprehension###########

mystring = 'hello'

mylist =[]

for letter in mystring:
    mylist.append(letter)


print(mylist)

mylist5 =[letter for letter in mystring]

mylist6 = [x for x in word]


print(mylist5)

print(mylist6)

mylist7 = [x**2 for x in range(0,11)]

print(mylist7)


mylist8 = [x for x in range (0,11) if x%2 == 0]

print(mylist8)


#######nested loop


mylist =[]

for x in [2,4,6]:
    for y in [100,200,300]:
         mylist.append(x*y)

print(mylist)

####or using list comprehenion

mylist =[x*y for x in [2,4,6] for y in [1,10,1000]]

#####create a statment tha will print put the worlds starts with s
########use if anf split

st1 = 'Sam print only the workds that starts with s in this sentence'

#st.split()


for words in st1.split():

    if(words[0].lower() =='s'.lower()):
     print(words)


#use range to print all the even number from 0 to11

print(list(range(0,11,2)))

for num in range(0,11,2):
    print(num)

#use a list comprehenion to create  lsit of umbers between1 nd 50 that r divisible by 3


list10  = [x for x in range(1,51) if x%3 ==0]

print(list10)

#.use the stirng below and rint even if length of stirng is even


st = 'print every word in thi sentence that has even number of letters'

for w in st.split():
    if len(w) %2 == 0:
        print(w +' is even')

########fizz buzz prgram

for num in range(1,10):
    if num%3 ==0 and num%5 ==0:
        print('FizzBuzz')
    elif num%3 ==0:
         print('Fizz')
    elif num%5 ==0:
         print('Buzz')
    else:
        print(num)

#use list comprehension to crate a list of first letter of every word ib low string

sr = 'create a list of first letter of eveyr word in this string'

nlist = [word[0] for word in sr.split()]

print(nlist)






