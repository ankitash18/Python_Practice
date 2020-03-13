#by definito - characteristic of an entiry to be able to present in more then onfr form
#plus method

class Employee:
    def setnumberofwh(self):
        self.numberofworkinghrs = 40

    def display(self):
        print(self.numberofworkinghrs)

class Trainee(Employee):
    def setnumberofwh(self):
        self.numberofworkinghrs =45

    def resetnumberofhrs(self):
        super().setnumberofwh()

emp = Employee()
emp.setnumberofwh()
print("number of working hours")
emp.display()

trainee = Trainee()
trainee.setnumberofwh()
print("number of wkring hours for trainee")

trainee.display()

trainee.resetnumberofhrs()

trainee.display()


#operator overloading

class Square():
    def __init__(self,side):
        self.side = side

    def __add__(square1,square2):
        return ((4*squareone.side)+(4*squaretwo.side))

squareone = Square(5) #5*4
squaretwo = Square(10) #5 *10

print(squareone+squaretwo)



