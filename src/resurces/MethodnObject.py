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
