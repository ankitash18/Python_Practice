import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() #things to be printed out
counter_queue = queue.Queue()#amlunt by which to increase counter

def incrment_counter():
    global counter
    while True:
        incrment =counter_queue.get()#this waits until an item is avialble and then locks the queu
        old_counter =counter
        counter =old_counter +incrment
        job_queue.put((f'New Counter value is {counter}','------------'))
        counter_queue.task_done() #this unlocks the queue

Thread(target=incrment_counter,daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


Thread(target=printer_manager,daemon=True).start()

def incrment_mgr():
    counter_queue.put(1)

worker_thread=[Thread(target=incrment_mgr) for thread in range(10)]

for thrad in worker_thread:
    thrad.start()

for thrad in worker_thread:
    thrad.join()

counter_queue.join()
job_queue.join()