"""
#pytest -v from command line below
by defalt ptest wil autmaticlly discover and run all the  test in al properly names modules from current dirdct and other dorecotry
module name - simple specify which moduke name to run onyl the tests in that module
direcoty name -run any test found in the soecified directory
-v - verbose mode endabled
-q - run in quiet mode
-s dont capture the console output
    --ignore -ignor eth pecifed path whendiscoverign test
    --maxfail -sto afte the specifed numbr if failures
    
"""

import pytest


def fizzbuzz(value):
    if ismultiple(value,3):
        if ismultiple(value,5) :
            return "FizzBuzz"
        return "Fizz"
    if ismultiple(value,5):
        return "Buzz"
    return str(value)

def ismultiple(value,mod):
    return (value%mod) == 0

def checkfizzbuzztest(value,expectedvalue):
    retval = fizzbuzz(value)
    assert retval == expectedvalue

def test_returnwith1passedin():
    checkfizzbuzztest(1,"1")

def test_returnwith2passedin():
    checkfizzbuzztest(2,"2")

def test_returnwith3passedin():
    checkfizzbuzztest(3,"Fizz")

def test_returnwith5passedin():
    checkfizzbuzztest(5,"Buzz")

def test_returnwith6passedin():
    checkfizzbuzztest(6,"Fizz")

def test_returnwith10passedin():
    checkfizzbuzztest(10,"Buzz")

def test_returnwith15passedin():
    checkfizzbuzztest(15,"FizzBuzz")