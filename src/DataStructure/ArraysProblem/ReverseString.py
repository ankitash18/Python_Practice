#given string of words,reverse all the words
#this is the best
#best the is this

s="this is the best"
print(s.split())
print(reversed(s.split()))
#print(" ".join(reversed(s.split())))

def rev_words(s):
    word = []
    length = len(s)
    space =[' ']

    i = 0
    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i +=1

            word.append(s[word_start:i])

        i +=1

    return " ".join(reversed(word))


s1="this is the best"

s2 = rev_words(s1)
print(s2)
