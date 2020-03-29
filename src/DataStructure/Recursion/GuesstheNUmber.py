#guess the number game

import random

print("hello,wht's your name")
name = input()

print('well,'+name+',i am thinking a number between 1 and 20')
secretnumber = random.randint(1,20)

for gusstaken in range(1,7):
    print("take a guess")
    guess = int(input())

    if guess < secretnumber:
        print("your gues is too low")
    elif guess > secretnumber:
        print("your guess is too high")

    else:
        break #this condition is for the correct guess

if guess == secretnumber:
    print('good job,'+ name+',you guessed my number correcly in ,'+str(gusstaken)+',guesses')
else:
    print("nope,the numebe if was thinkinkg of was,"+ str(secretnumber))

