#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line."



class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)

coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())

print(li.slope())



class Cylinder:

    def __init__(self, height=1, radius=1):

     self.height = height
     self.radius = radius

    def volume(self):
     return self.height*3.14*(self.radius)**2

    def surface_area(self):

        top = 3.14 * (self.radius) ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)

c = Cylinder(2,3)
print(c.volume())

print(c.surface_area())

##For this challenge, create a bank account class that has two attributes:
##owner\n
#balance
#and two methods:\n",
 #deposit\n",
#withdraw
##As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.



class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance+dep_amt
        print(f"added {dep_amt} to balance")

    def withdrawl(self,wd_amt):

        if(self.balance >= wd_amt):
            self.balance = self.balance - wd_amt
            print(f" withdrawl acept")
        else:
            print("sorry not enough funds")

    def __str__(self):
        return f"Onwer :{self.owner} and Balace :{self.balance}"


account  =Account("Sam",500)

print(account.owner)
print(account.balance)

account.deposit(200)
print(account)

account.withdrawl(300)

print(account)