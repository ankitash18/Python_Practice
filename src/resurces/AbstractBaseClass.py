from abc import ABCMeta,abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('walking')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def num_legs(self):
        return 4

class Monkey(Animal):
    def __init__(self,name):
        self.name = name

    def num_legs(self):
        return 2



#cant instantiate animal as it is absart class
d = Dog('Rolf')
print(d.name)
print(d.num_legs())
d.walk()


a = [Dog('Rolf'),Monkey('Bob')]
for animal in a:
    print(isinstance(animal,Animal))
    print(animal.num_legs())