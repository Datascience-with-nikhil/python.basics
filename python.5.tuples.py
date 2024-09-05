print("python tuples")
t = (2, 3, 4, 5, "string", 1.11, 10+7j, [.1, 2, True, 1+7j], (100), [(1000)])
t1 = (1.1, 2.2, 3.3, 4.4+5.5j)
print(t + t1)
##print(t + 7j) #error
##print(t + (1)) #error


print("tuple type() function")
print(type(t))
print(type(t[6]))
print(type(t[7]))
print(type(t[8]))
print(type(t[9]))
print(type(t[9][0]))

print("python tuples indexing and slicing")
print(t[0])
print(t[6])
print(t[2])
print(t[9])

print(t[0:5:2])
print(t[::-1])
print(t[7][::-1])
print(t,"",t[7][::-1])

print("changing a list value in from tuple data type")
t[7][0] = 911
print(t)
t[7].pop(-1)
print(t)

print("Change Tuple Values, tuple are immutable")
x = ("a", "b", "c")
print(x)
y = list(x)
y[0] = "abc"
print(y)
x = tuple(y) # redeclaration of variable x
print(x)

print("tuple methods")

print("len()")
print(len(t))

print("index() method")
print(t.index(3))
print(t.index([1000]))

print("count() method")
print(t.count(2))