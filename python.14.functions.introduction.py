print("function")
print("creating a function")

print(" ")
def test1():
    print("test1 function")

test1()

print(" ")

print(type(test1()))  #<class 'NoneType'>

## print(test1() + "string") # error because <class 'NoneType'>

print("use return")
print("by help of return can do many operations also it,s show data type")

print(" ")

def test2():
    return print("string")

test2()
print(type(test2()))

print(" ")

def test3():
    return 100

test3()
print(type(test3()))

print(test3() * 10)

print(" ")

print("pass key")

def test0():
    pass

test0() #pass key

print(" ")

print("multiple data type in single function")

def test4():
    return 1, .2, 3j, "4string", [5], {1 : 10}, 7, {9}

print(test4())

print(" ")

print("variable declaration using function that store different data type")

print(len(test4()))

a, b, c, d, e, f, g, h = test4()

print(a, b, c, d, e, f, g, h)

print(" ")

print("scaling and identifying data type")

print(test4()[0:10:2])
print(test4()[2])

print(type(str(test4()[2])))

print(" ")

print("function with logic")

def test5():
    a = int(input())
    b = int(input())
    c = a * b
    return c

print(test5())

print(" ")

print("in a name of function creating variable")

def test6(a, b, c):
    a1 = a*b*c
    return a1

print(test6(1, 2, 3))

print(" ")

l = [1,  2, 3, 4, 5, .1, .2, .3, .4, .5, "string", [11, 22, "string"], ("tuple")]

print("function with loop")
print("2 sample method 1. give value by name of text and 2. give value inside or outside function")

def test7():
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    return l1

print(test7())

print(" ")

def test8(a1):
    l1 = []
    for i in a1:
        if type(i) == list:
            for j in i:
                l1.append(j)
        else:
            if type(i) == int or type(i) == float:
                l1.append(i)
    return l1

 #in a place of a1 passing a list
print(test8(l))