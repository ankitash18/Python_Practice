def uni_char(s):
    return len(set(s)) == len(s)  #using set datastructure


a = uni_char("abcade")

print(a)

def uni_char2(s):
    char = set()

    for let in s:
        if let in char:
            return False
        else:
            char.add(let)

    return True


b = uni_char("abcde")

print(b)

movies = ['Star Wars', 'The Godfather', 'Harry Potter ', 'Lord of the Rings']

for m in movies:  # it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
    print(f'One of my favorites movie is {m}')
    break
else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
    print('This is the end of the list')

## for ... continue -> it prints out all letters of the string without 'o'
for letter in 'Python Go and Java Cobol':
    if letter == 'o':
        continue    #go to the beginning of the for loop and do the next iteration
    print(letter, end='')


## for ... break
sequence = [1, 5, 19, 3, 31, 100, 55, 34]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        break   #breaks out of the loop (executes the first instruction (if any) after the else block of code)
else:
    print('There is no number divisible by 17 in the sequence')

my_sum = 0
x = 10
while x:
    if x % 2 != 0:
        my_sum += x
       # print(sum)
    x -= 1

print(my_sum)