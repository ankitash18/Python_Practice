from typing import Union


def divide(dividend:Union[int,float],divisor:Union[int,float]):
    if divisor ==0:
        raise ValueError("divisor cannot be zero")
    return dividend/divisor


def multiply(*args:Union[int,float]):
    if len(args) ==0:
        raise ValueError("at leats one valye must be passed")
    total =1
    for arg in args:
        total *= arg

    return total