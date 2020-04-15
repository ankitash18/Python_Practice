import  multiprocessing as mp
import time

#multiprocessing

def name_and_time(name):
    print(f'hello {name}.current time is {time.time()}')
    print('sleepinggor two mins')
    time.sleep(2)
    print('aftr sleeping..exiting funciton')


if __name__ == '__main__':
    processlist = list()
    for  i in range(10):
        process = mp.Process(target = name_and_time,args = ('Andrie',))
        processlist.append(process)
    for p in processlist:
        p.start()

    print('other instruciton of the main module')
    print('end of script')

import multiprocessing as mp


## Target function that increments a counter (multiprocessing.Value)
def increment(counter):
    counter.value += 1


## Target function that increments a counter (integer)
def my_increment(my_counter):
    my_counter += 1


if __name__ == '__main__':
    my_counter = 1  # type integer
    counter = mp.Value('i', 1)  # type multiprocessing.Value

    ## Creating, starting and joining 10 processes. They increment the counter. This is of type multiprocessing.Value
    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()

    print(f'counter of type multiprocessing.Value is {counter.value}')

    ## Creating, starting and joining 10 processes. They increment my_counter. This is of type integer
    for i in range(10):
        process = mp.Process(target=my_increment, args=(my_counter,))
        process.start()
        process.join()

    print(f'my_counter of type integer is {my_counter}')

import multiprocessing as mp
import time


## Target function. It increments a balance by 0.01  100 times
def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


## Target function. It decrements a balance by 0.01  100 times
def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 500)  ## starting balance
    print(f'Balance BEFORE running processes: {balance.value}')

    lock = mp.Lock()  # lock Object

    ## Creating, starting and joining 2 processes. They increment and decrement the shared value
    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    ## The final value of balance
    print(f'Balance AFTER running processes: {balance.value}')