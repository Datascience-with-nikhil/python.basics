print("decorators")


def create_adder(x):
    def adder(y):
        return x + y

    return adder

add = create_adder(15)

print(add(1))

print()


def deco(func):
    def inner_dec():
        print("this is a start of my function")
        func()
        print("this is the end of myfunction")
    return inner_dec


@deco
def test1():
    print(1 + 1)

test1()

import time

def timer_test(func):
    def timer_test_inner ():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timer_test_inner

@timer_test
def test2():
    print(1 + 1)


test2()