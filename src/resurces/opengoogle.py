import webbrowser

#We're using webbrowser  here which is a standard library that is used to open a web browser.

#query = input("enter your searc hword")

#webbrowser.open("http://google.com/search?q=%s" %query)


#Make script that prints out the current day, and time. For example

from datetime import datetime

print(datetime.now())
print(datetime.now().year)


print(datetime.now().strftime("toda is %A,%B %d,%Y"))

age = int(input("whats your age"))

year_birth = datetime.now().year - age

print("you were born in %s" %year_birth)

#passord generator

import random

characters =  "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

chosen = random.sample(characters,6)

password = "".join(chosen)
print(password)

#Create a program asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter and at least 5 characters. If the conditions are generated, print out "Password is fine",
# otherwise keep prompting the user for a password.

while True:
    psw = input("enter new password")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw)  and len(psw) >= 5:
        print("passwprd is fine")
        break
    else:
        print("password is not fine")


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)






