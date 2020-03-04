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

mylist=['a','b','c']

'--'.join(mylist)


#####USING JOIN#######
def master_yoda1(text):
    wordlist = text.split()
    reversed_word_list = wordlist[::-1]
    return ' '.join(reversed_word_list)

print(master_yoda1('I am home') )

#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200\n"

def almost_there(n):
   return  ((abs(100-n) <= 10) or (abs(200-n) <= 10))


print(almost_there(104))


######level 3 questions..
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True\n",
   # "    has_33([1, 3, 1, 3])→ False
 #   "    has_33([3, 1, 3]) → False"


def has_33(nums):

    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True

        return False

print(has_33([1,3,1,3]))

def has_331(nums):  ##use slicing

    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True

        return False

print(has_331([1,3,3,3]))


#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(n):
    result = ''

    for char in n:
        result += char*3

    return  result

print(paper_doll('Hello'))

#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum([a,b,c]) <=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return 'BUST'


print(blackjack(9,9,9))


#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


#  summer_69([1, 3, 5]) --> 9\n",
#summer_69([4, 5, 6, 7, 8, 9]) --> 9\n",
# summer_69([2, 1, 6, 9, 11]) --> 14"


def summer_69(arr):

    total =0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break

    return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))


#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order\n",


def spy_code(nums):
    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works\n"


    return len(code) == 1

print(spy_code([1,2,4,0,0,7,5]))

#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number\n",


def count_primes(num):

    if num < 2:
        return 0
    ## 2 or greater

    primes = [2]
    x =3

    while x <= num:
        for y in primes:
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return  len(primes)


print(count_primes(100))

#### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter\n


def print_big(letter):
       patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
       alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}

       for pattern in alphabet[letter.upper()]:

             print(patterns[pattern])

print(print_big('a'))

#**Write a function that computes the volume of a sphere given its radius.**

def vol(rad):
    result =  (4/3)*(3.14)*(rad**3)

    return result


print(vol(2.0))

#**Write a function that checks whether a number is in a given range (inclusive of high and low)**


def ran_check(num,low,high):
    if num in range(low,high):
        print(f' {num} is in the range')
    else:
        print(f' {num} is not  in the range')


ran_check(3,1,10)

#**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

def up_low(s):
    d = {"upper":0,"lower":0}

    for c in s:
        if c.isupper():
            d["upper"] +=1
        elif c.islower():
            d["lower"] +=1
        else:
            pass
    print(f'originla string {s}')
    print(f'No. of Upper case characters {d["upper"]}')
    print(f'No. of lower case characters {d["lower"]}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday')



#**Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(l):
    x =[]
    for a in l:
        if a not in x:
            x.append(a)

    return x


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



#**Write a Python function to multiply all the numbers in a list.**

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x

    return total

print(multiply([1,2,3,-4]))


#**Write a Python function that checks whether a passed string is palindrome or not.**

def palindrome(s):
    s = s.replace(' ', '')
    return  s == s[:: -1]


print(palindrome('helleh'))


#Write a Python function to check whether a string is pangram or not


#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.\n",
 #For example : \"The quick brown fox jumps over the lazy dog\"\n",

import string

def ispangram(str1,alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The quick brown fox jumps over the lazy dog"))