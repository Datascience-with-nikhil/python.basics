l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test1():
    l1 = []
    for i in l:
        l1.append(i ** 2)
    return l1


print(test1())

print("map() function")


def sq(x):
    return x ** 2


print(sq(2))

print(map(sq, l))
list(map(sq, l))

print(list(map(sq, l)))
print(tuple(map(sq, l)))
print(set(map(sq, l)))

print(" or ")

map1 = list(map(sq, l))
print(map1)

print("map() function with lambda function")

map2 = list(map(lambda x: x ** 2, l))
print(map2)

map3 = list(map(lambda x: x * 2, "string"))
print(map3)

map4 = list(map(lambda x: x*2, "string"))
print(map4)

## map5 = list(map(lambda x: x*2, x.upper(), "string")) #error
map5 = list(map(lambda x: (x*2, x.upper()), "string"))
print(map5)

map_dict = dict(map(lambda x: (x*2, x.upper()), "string"))
print(map_dict)

map6 = list(map(lambda x: (x*2, x.upper(), x.lower()), "string"))
print(map6)

a1 = map_dict

print(a1["ss"])

map7 = list((map((lambda x: x*2 and x.upper()), "string")))
print(map7)

map8 = list((map((lambda x: x*2 or x.upper()), "string")))
print(map7)

map9 = list(map(lambda x: (x * 2 and x * 3), l))
print(map9)

map10 = list(map(lambda x: (x * 2 or x * 3), l))
print(map10)

map11 = list(map(lambda x: (x ** 2, x**3), l))
print(map11)

map12 = dict(map(lambda x: (x ** 2, x ** 3), l))
print(map12)

l1 = [0, 1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11]

map13= list(map(lambda x, y: x+y, l1, l2))
print(map13)

l3 = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
l4 = [0, 1, 2, 3, 4, 5]

map14 = list(map(lambda x, y: x + y, l3, l4))
print(map14)

def test3(x, y):
    return x + y

map15 = list(map(test3, l2, l1))
print(map15)

print("reduce() function")

print(l)

from functools import reduce

print()

red1 = reduce(lambda x, y: x+y, l)
print(red1)

red2 = reduce(lambda x, y: x % y, l)
print(red2)

red3 = reduce(lambda x, y: x*y, l)
print(red3)

print("in general under a reduce() function pass only two arguments x,y")
print(reduce(lambda x, y: x / y,[1] )) #an exceptional case

print(reduce(lambda x, y: x * y,[1],[1,2,3]))

r4 = reduce(lambda x, y: x if x>y else y, set(l))
print(r4)

print("filter() function")

fi1 = list(filter(lambda x: x % 2 == 0, l))
print(fi1)

fi2 = list(filter(lambda x: x != 0, l))
print(fi2)

l4 = [11,-2, 1, 6, -1, -10, 1, -5, 100]

p=(reduce(lambda x,y: x + y, l4))
print(p)

fi3 = list(filter(lambda x: x<0, l4))
print(fi3)

l5 = ["asian", "wide"]

fi4 = list(filter(lambda x: len(x)<5, l5))
print(fi4)