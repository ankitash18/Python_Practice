import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input('Enter your name')
    greet =f'hello,{user_input}'
    print(greet)
    print(f'ask user {time.time()-start}')

def coplex_calc():
    start = time.time()
    print('start calcualrion')
    [x**2 for x in range(20000000)]
    print(f'coplex_calc {time.time() - start}')

start = time.time()
ask_user()
coplex_calc()
print(f'Single Thred total time {time.time() - start}')


thread1 = Thread(target=coplex_calc)
thread2 = Thread(target=ask_user)


start1 = time.time()
thread1.start()
thread2.start()

thread1.join()  #blocking operation
thread2.join()

print(f'Two Thred total time {time.time() - start1}')



