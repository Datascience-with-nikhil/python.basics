print("generator function")
print()


def t1():
    return 1 + 1


print(t1())


def t2():
    a = 1
    print(a)

    return


print(t2())


def test1(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(test1(10))

for j in test1(10):
    print(j)

print()


def test2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(type(test2()))


a1 = test2()

for i in range(10):
    print(next(a1))

s = "Str"
print(type(s))

s1 = iter(s)
print(type(s1))

print(next(s1))
print(next(s1))
print(next(s1))
##print(next(s1)) #StopIteration

a2 =iter("this is iter()")
print(a2)

print(next(a2))
print(next(a2))
print(next(a2))

d = {"ocean" : 4, "continuances" : 7}

di = iter(d)

print(next(di))
print(next(di))

di_1 = iter(d.items())

print(next(di_1))
print(next(di_1))

for i in iter("string"):
    print(i)

