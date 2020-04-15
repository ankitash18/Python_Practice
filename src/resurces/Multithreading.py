import  threading
import time

#multiprocessing

def name_and_time(name):
    print(f'hello {name}.current time is {time.time()}')
    print('sleepinggor two mins')
    time.sleep(2)
    print('aftr sleeping..exiting funciton')


if __name__ == '__main__':
    thread_list = list()
    for  i in range(10):
        thread = threading.Thread(target = name_and_time,args = ('Andrie',))
        thread_list.append(thread)
    for p in thread_list:
        p.start()

    for p in thread_list:
        p.join()

    print('other instruciton of the main module')
    print('end of script')