def timer(func):
    import time    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{func.__name__} ran in {t2} seconds")
        return result
    return wrapper
    
import time 
@timer
def add(a, b):
    time.sleep(1)
    return a + b

# print(add(9,10))

def retry (attempts , time_delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                    time.delay(time_delay)

                except Exception as e:
                    print(f"attempt no {attempt} failed : {e} ")

                if attempt == attempts-1:
                    raise
        return wrapper
    return decorator
    

import random 
@retry(5,2)
def unstable():
    num = random.random()
    if num < 0.2:
        return "Success!!!"
    raise Exception("Failure")

# print(unstable())


def cache(func):
    memo = {}
    def wrapper(n):
        if n in memo:
            return memo[n]
        memo[n] = func(n)
        return func(n)
    return wrapper

@cache
def fibonacci(n):
    if n <= 1 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(35))


def validate_type(**type_hints):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name , expected_type in type_hints.items():
                if name in kwargs and not isinstance(kwargs[name] , expected_type):
                    raise TypeError(f"{name} must be of {expected_type} type!!!")
            return func(*args, **kwargs)
        return wrapper
    return decorator
    

@validate_type(a = int , b = int)
def add(a, c):
    return a+c

print(add(a = 12 , c = 15.1))



                  