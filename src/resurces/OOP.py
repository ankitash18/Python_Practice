##########class########


class Dog():

    ######class objetc attributes and methods
#same for any instance of clas

    species = 'mammel'


    def __init__(self,mybreed,name):
         self.my_attriute = mybreed  #attributes assing it to using self.
         #or..self.mybreed = mybreed
         self.name = name

    def bark(self,number):
        print("Woof..my name is {} and number is {}".format(self.name,number))

#expect boolean for spots
#mydog = Dog(mybreed='lab',name='Sammy')

mydog = Dog('lab','Frankie')

print(type(mydog))

print(mydog.my_attriute)
print(mydog.name)



print(mydog.species)

mydog.bark(10)


class Circle():

    # class objet attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi*2  # or Circle.pi

    def get_cir(self):
         return self.radius * self.pi * 2

my_circle = Circle(30)


print(my_circle.pi)

print(my_circle.radius)

print(my_circle.area)

print(my_circle.get_cir())


##########inheritance#########


class Animal():

    def __init__(self):
        print("animal crated")

    def who_m_i(self):
        print("I am an animal")

    def eat(self):
        print("i am eating")


myanimal = Animal()

myanimal.eat()

myanimal.who_m_i()

class Dog1(Animal):#inheritance--dog is derived class

    def __init__(self):
        Animal.__init__(self)
        print("dog created")

    def who_m_i(self):
         print("i ma a dog")

    def eat(self):
        print("i m a dog and eating")

    def bark(self):
        print("woof")

mydog1 = Dog1()

mydog1.eat()

mydog1.who_m_i()

mydog1.eat()

mydog1.bark


########polymorphsim

#Real life examples of polymorphism include:\n",
 #opening different file types - different tools are needed to display Word, pdf and Excel files\n",
# adding different objects - the `+` operator performs arithmetic and concatenation"



class Dog2():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +"say woof "

class Cat():

    def __init__(self, name):
            self.name = name

    def speak(self):
            return self.name + "say meow "

niko = Dog2("niko")

felix = Cat("felix")


print(niko.speak())

print(felix.speak())


for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal:
    def __init__(self, name):    # Constructor of the class\n",
        self.name = name


    def speak(self):              # Abstract method, defined by convention only\n",
         raise NotImplementedError("Subclass must implement abstract method")



class Dog(Animal):
     def speak(self):
        return self.name+' says Woof!'


class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'



fido = Dog('Fido')

isis = Cat('Isis')

print(fido.speak())

print(isis.speak())


## Special Methods\n",
#Finally let's go over special methods. Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book1 = Book('Python Rocks','Jose Portilla',200)

print(book1)

print(len(book1))

del(book1)



