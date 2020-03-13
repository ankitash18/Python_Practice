import random

health=50

portioneath =random.randint(25,50)

print(portioneath)

print(len("hello"))

my_string = "hello world"

print(my_string[0])

print(my_string[-3])

print(my_string[2:])

print(my_string[0:5])

print(my_string[:3])

print(my_string[::])

print(my_string[::2]) # step size of 2

print(my_string[::-1]) # reverse string

print(my_string.capitalize())

print('p' + 'am')

print(my_string + '..am')

print(my_string.split())

print(f" mu name is {my_string}")


my_range = range(1,21)

print(list(map(str,my_range)))

#remove dulicteas
a=["1",1,"1",2]

print(list(set(a)))

#This is another solution that would preserve the original order.
# We go through all items of the original list and append them to the new list if they have not been appended before.
# The downside of this is the operation can take a lot of time if the list is large as we need to access both lists and also perform a conditional in each iteration.


a1 =["1",1,"1",2]

b =[]


for i in a1:
    if i not in b:
        b.append(i)


print(b)



dict = {"a":1,"b":2}

print(dict["b"])


d = {"a":1,"b":2,"c":3}

#easy way

print(d["a"] + d["b"] + d["c"])

#amonte rway

print(sum(d.values()))

#add a new pari of key

dict["c"]  = 3

print(dict)

#dictonary filtering

for key,value in dict.items():
    if value <= 1:
        d1 = {key:value}
        print(d1)


from pprint import pprint
d3 = {"d": list(range(1,10)),"b":list(range(11,20)),"c": list(range(21,30))}

print(d3)

pprint(d3)

print(d3["b"][2])

for key,value in d3.items():
    print(key,"has value",value)


    #make a scrpt to print letter from a to z

import string

for letter in string.ascii_lowercase:
    print(letter)


def count_words(strng):
    strng_list = strng.split()
    return len(strng_list)




#print(count_words("words2.txt"))

word = count_words("Hey there it's me!")


print(word)


def count_words(filepath):
    with open(filepath,'r') as file:
        strng = file.read
        strng_list = strng.split(" ")
        return len(strng_list)


def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)


import string

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")



a = [1,2,3]
b = (4,5,6)

for i ,j  in zip(a,b):
    print(i+j)



 #Create a script that generates a file where all letters of English alphabet are
# listed two in each line. The inside of the text file would look like:
# ab
#cd
#rs


import string

with open("letters.txt",'w') as file:
    for letter1,letter2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        file.write(letter1+letter2 + "\n")

#Create a script that iterates through text files and checks if strings p, y, t, h, o, or n are found in the content of the text file.
# If any of those strings is found, append that string to a list.


import glob

letters = []
file_list = glob.iglob("letters/*.txt")
check = "python"

for filename in file_list:
    with open(filename, "r") as file:
        letter = file.read().strip("\n")
    if letter in check:
        letters.append(letter)





