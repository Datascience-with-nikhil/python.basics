#list 

l = [1, 2, 3, 1.1, 1.2, 1.3, 1, 2, 3, True, False, 2+2j, "string.datatype",2+2j]
l2 = [1, 2, 3, 4, 5]
l3 = ["world.wide"]
l4 = [1, 2, 3, True, [100, 200, 300], [500, 600, [700, 800, 900, 100000]]]

t, f = True, False
i = 10
flo = 1.11
s = "s for string"

print(type(l))
print(type(l2))
print(type(l3))
print(type(l4))
print(type(i))
print(type(f))
print(type(s))

print("list indexing and sclicing ")

print(l[0])
print(l[2])
print(l3[0])
print(l4[4])
print(l4[5][2])
print(l4[5][1])
print(l[13])

print(l[:])
print(l[::2])
print(l[1:10])
print(l[0:2])
print(l[1:10:2])
print(l[::-1])
print(l[-1:-3:-1])
print(l2[::])
print(l3[::])
print(l4[4][0:2])
print(l4[4][::-1])
print(l4[4][-3:-1:1])
print(l4[5][0:100])
print(l4[5][2][:])
print(l4[5][2][::-1])
print(l4[5][2][-10:-1:1])
print(l4[5][2][1:100:1])