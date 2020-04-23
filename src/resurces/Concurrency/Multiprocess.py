import time
from multiprocessing import Process

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

process = Process(target=coplex_calc)
process2 = Process(target=coplex_calc)

process.start()
process2.start()

start1 = time.time()


process.join()
process2.join()

print(f'Two Process total time {time.time() - start1}')








