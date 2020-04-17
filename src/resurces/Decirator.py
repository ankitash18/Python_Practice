from functools import wraps


# defining a decorator
#decorator as HOF which takes a funtion and return a funtion
def timer(fn):
    from time import time

    @wraps(fn)
    def wrapper_timer(*args, **kwargs):  # this is a generic decorator
        start_time = time()  # retrieving the current timestamp
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{fn.__name__} execution time:{end_time - start_time}')
        return result

    return wrapper_timer


# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)


s = sum_of_powers(1000000, 2)
print(s)

s = sum_of_powers(1000000, 3)
print(s)

s = sum_of_powers(1000000, 5)
print(s)


import functools
user={'username':'jose123','accesslevel':'admin'}

def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args,**kwargs):
        """
        secure_fun running
        """
        if user.get('accesslevel') == 'admin':
            return func(*args,**kwargs)
    return secure_func

@user_has_permission
def my_function(panel):
    """
    my_fucntion
    """
    return f'password for {panel} panel is 1234'

@user_has_permission
def another():
    print('hello')



print(my_function('movies'))
print(my_function.__name__)

another()