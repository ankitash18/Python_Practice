def boxprint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("symbol needs to be a single length strength")

    if (width < 2) or (height < 2):
        raise Exception("width n height must be grater or equal to 2")
    print(symbol *  width)

    for i in range(height-2):
        print(symbol+(' ' * (width-2))+symbol)

    print(symbol * width)


boxprint('*',15,5)


def switchlights(intersection):
    for key in intersection.keys():
        if intersection[key] =='green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    assert 'red' in intersection.values(),'Neiher light is red !'+str(intersection)


market_2nd = {'ns':'green','ew':'red'}




#logging

import logging

logging.basicConfig(level = logging.DEBUG,format='%(asctime)s - %(levelname)s -%(messgae)s')


logging.debug('start of progeam')

def factorial(n):
        logging.debug('start of facorail(%s)')
        total =1
        for i in range(1,n+1):
            total *= i
            logging.debug('i is %s,tota is %s' %(i,total))
        return total

print(factorial(5))




