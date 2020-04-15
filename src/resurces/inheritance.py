#single inheritance

class Apple:
    manufacturer = "Apple Inc"
    coontactwedsite = "www.apple.com/contact"

    def contactdetails(self):
        print("to contact us..logon to ",self.coontactwedsite)

class MacBook(Apple):
    def __init__(self):
        self.yom = 2017

    def mnfdetails(self):
        print("thsi mac book was manufacutred n year {} by {}".format(self.yom,self.manufacturer))


macbook = MacBook()

macbook.mnfdetails()

macbook.contactdetails()


#multiple inheritance
class Operatingsystem:
    multitasking = True
    name = "MAc OS"

class Apple1:
    website = "www.apple.com"
    name = "Apple"

class Macbook1(Operatingsystem,Apple1):
    def __init__(self):
        if self.multitasking == True:
            print("this is multitasig system.Visit {} for more details".format(self.website))
            print("Name:",self.name)



macbook1 = Macbook1()

#multilevel inheritance


class MsicalInstrument:
    numberofmajorkey = 12

class StringInstrument(MsicalInstrument):
    typeofwood = "Tonewood"


class Guitar(StringInstrument):
    def __init__(self):
        self.numberofstirng = 6
        print("this gitar consist f {} stirng.it is made of {} and it can play {} keys".format(self.numberofstirng,self.typeofwood,self.numberofmajorkey))


guitar = Guitar()


#access modifiers


#public => membername
#protected => _membername
#private =>  __membername

class Car:
    numberofwheels = 1
    _color = 'black'
    __yearofmnf = 2017



class Bmw(Car):
    def __init__(self):
        print("Proeted attribute colour",self._color)




car = Car()
print("public attribute numberof wheels:",car.numberofwheels)


bmw = Bmw()

#print("private attribute yearof mnf:",car.__yearofmnf)


class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    #or add prpoerty annotation and use it likr vribale
    #def weekly_slsary(self):
    @property
    def weekly_slsary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf','MIT',15.50)
print(rolf.salary)
print(rolf.school)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
#print(rolf.weekly_slsary())
print(rolf.weekly_slsary)


#statsi method and classmethod


class FixedFloat:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}'

    #@staticmethod
    @classmethod
    #def from_sum(value1,value2):
    def from_sum(cls, value1, value2):
        #return FixedFloat(value1+value2)
        return cls(value1 + value2)

new_member = FixedFloat.from_sum(19.5,0.789)
print(new_member)


class Euro(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = 'e'

    def __repr__(self):
        return f'Euro {self.symbol} {self.amount:.2f}'

money  = Euro.from_sum(1.12,2.12)
print(money)

