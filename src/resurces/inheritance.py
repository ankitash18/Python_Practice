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



