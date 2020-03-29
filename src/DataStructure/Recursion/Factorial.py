def fact(n):
    #base case
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


a = fact(4)
print(a)


#Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

def cumsum(n):
    if n ==0:
        return 0

    else:
        return n + cumsum(n-1)


b = cumsum(4)
print(b)
#Given an integer, create a function which returns the sum of all the individual digits in that integer.
import sys

#sys.setrecursionlimit(2000)


def sum_func(s):

    if  len(str(s)) == 1:
        return s

    else:
        #strip the digits
        #r = n%10
        #n = n /10
        return  s%10 + sum_func(s/10)

#c = sum_func(43)



print(len(str(43)) ==1)


#Create a function called word_split() which takes in a string **phrase** and a set **list_of_words**. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words.
# You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

def word_split(phrase,list_of_words,output=None):

    if output is None:
        output =[]

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)

    return output

#d = word_split('themanran',['the','ran','man'])


d =word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])


print(d)
