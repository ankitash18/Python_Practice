class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<car {self.make} {self.model}> '



class Garage:
    def __init__(self):
        self.cars=[]
    def __len__(self):
        return len(self.cars)

    def add_car(self,car):
       # print('this method is wokr in prgrss')
       if not isinstance(car,Car):
           raise TypeError(f'treid to add a class car name {car.__class__.__name__}')
       self.cars.append(car)

        #raise NotImplementedError('we cant add cars to garage gyet')


ford_garage = Garage()
car = Car('ford','fiesta')
try:
    ford_garage.add_car(car)
except TypeError:
    print('your car was not a car')
except ValueError:
    print('somthing wird happend')
finally:
    print(f'gagrage has now {len(ford_garage)} cars')

print(len(ford_garage))


def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError('Input should be a non-negative integer')
    for x in range(0, n+1):
        print(x)


class mycustomerror(TypeError):
    def __init__(self,message,code):
        super().__init__(f'Error  cdoe {code} :{message}')
        self.code  = code

raise mycustomerror('An error happend',500)


class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__('Invalid value for n, {}. n must be greater than 0.'.format(wrong_value))


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
