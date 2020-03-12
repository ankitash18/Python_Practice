def ask_for_input():
    try:
        result = int(input("please provie number"))
    except:
        print("whoops!thats not number")
    finally:
        print("end of block sucessfully")




#ask_for_input()

#Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks


try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("general error !watch out")

#Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

try:
    x =5
    y =0
    z = x/y
except:
    print("Can't divide by Zero ")
finally:
    print("all done")


#Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

def ask():

    wating = True
    while wating:
        try:
            n = int(input("enter a number"))
        except:
            print("please try again \n")
            continue
        else:
            wating = False
            #break

    print("number squar is")
    print(n**2)


ask()