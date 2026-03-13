class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count > self.limit:
            raise StopIteration
        value = self.a
        self.a,self.b = self.b , self.a + self.b
        self.count+=1
        return value
    
import time


fib = Fibonacci(20000)
start1 = time.time()
for nums in fib:
    print(nums)
end1 = time.time() - start1


def fibonacci_gen(start,limit):
    a, b = 0, 1

    for _ in range(start):
        a, b = b, a + b
    
    for i in range(start , limit + 1, 1):
        yield a
        a, b = b, a + b


start2 = time.time()
for i in fibonacci_gen(0 , 20000):
    print(i)
end2 = time.time() - start2
print(f"function 1 ran in {end1} seconds")
print(f"function 2 ran in {end2} seconds")