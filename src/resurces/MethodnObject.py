mylist =[1,2,3,4]

mylist.append(6)

print(mylist.pop())
#######function########

def nameof():
    print('hello')



nameof()

def nameofperosn(name='NAME'):
    print('hello ' + name)


nameofperosn('jose')





def add(num1,num2):
    '''
    fnciton to add two numbers
    '''
    return num1+num2


a = add(2,3)

print(a)

####find out if th word is in as  tring?

def findout(s):
     if 'dog'.lower() in s.lower():
         return True
     else:
         return  False

########or write like below

def dog_check(mystring):
    return 'dog'.lower() in mystring.lower()

print(dog_check('Dog ran away'))
print(findout('Dog ran away'))

########PIG LATIN########
#IF WORD starts with a vowel,add 'ay' to end
#if word does not start with a vowel,put first lettr at the end,then add 'ay
#word -> orday
#apple -> appleay
#

def pig_latin(word):
    first_letter = word[0]

    #check if first letter is vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
        return pig_word
    else:
        pig_word =  word[1:] + first_letter + 'ay'
        return pig_word

word1  = pig_latin('apple')

print(type(word1))

print(word1)

###########

def myfunc(*args):
    print(args)


myfunc(10,20)


def myfunc(**kwargs):  ####dictonairy
    if 'fruit' in kwargs:
        print('my choice of fruit {}'.format(kwargs['fruit']))
    else:
        print('i didt not')


myfunc(fruit = 'apple',veggie= 'lettuce')

############# LESSER OF TWO EVENS:
# #Write a function that returns the lesser of two given numbers
# *if* both numbers are even, but returns the greater if one or both numbers are odd\n",


def lesser_of_two_event(a,b):
    if a%2 ==0 and b%2 ==0:
        if a < b:
            result = a
        else:
            result = b
    else :
        if a> b:
            result= a
        else:
            result = b

    return result


print(lesser_of_two_event(2,5))


def lesser_of_two_event(a,b):
    if a%2 ==0 and b%2 ==0:
       return  min(a,b)
    else :
     return max(a,b)

    print(lesser_of_two_event(2, 5))


####### ANIMAL CRACKERS:
# #Write a function takes a two-word string and returns True if both words begin with same letter\n"

def two_word(word1,word2):
    if word1(0) == word2(0):
        return True
    else:
        return False

def two_word(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

print(two_word('Crazy cat'))


#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# *or* if one of the integers is 20. If not, return False\n",

def makes_twenty(n1,n2):
     return (n1+n2) == 20 or n1 == 20 or n2 == 20




print(makes_twenty(3,2))


########## OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def  old_mac(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'name is too short'


print(old_mac('macdonald'))


###### MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'\n",
# master_yoda('We are ready') --> 'ready are We'"


def master_yoda(text):
    wordlist = text.split()
    reversed_word_list = wordlist[::-1]
    return reversed_word_list

print(master_yoda('I am home') )

#####USING JOIN#######








