print("lambda functions")

la = lambda nu=2.0, p=3: nu ** p
print(type(la()))

print(la(2, 2))

la2 = lambda n, p: n ** p

print(la2)
print(la2(.1, 1))


## print(la2()) #error

def test1():
    lam1 = lambda n=2, p=2: n ** p
    print(lam1())
    return


test1()

lam1 = lambda x, y: x + y

print(lam1(1, 1))

print("lambda function with if and else")

lam2 = lambda x, y: (" value of x is :  ", x) if x > y else ("value of y is ", y)

print(lam2(1, 2))

print()

lam3 = lambda x, y: (" value of x is :", x, " value of y is:", y) if x > y and x >= 1 else ("value of y is ", y)

print(lam3(1, 0))

s = "Asian"
lam4 = lambda: len(s)
print(lam4())

print()

##lambda "Asian" : len("Asian")
lam5 = lambda s = "Asian": len(s)
print(lam5())