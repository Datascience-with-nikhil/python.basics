print("for loop")
print()

print("for loop with function range(start, end, step)")
for i in range(1,11):
    print(i)

for i in range(1, 21, 2):
    print(i)

l = [ 1, 2, 3, 4, 5]
for i in l:
    print(i)

for i in l:
    print(i + 10/i)
    print()

l1 = []
for i in l:
    print(i + 1)
    l1.append(i + 1)

print(l1)

l2 = ["a", "b", "c", "d", "e", "f", "i", "j", "k", "l"]
l3 = []
for i in l2:
    print(i.upper())
    l3.append(i.upper())

print(l3)