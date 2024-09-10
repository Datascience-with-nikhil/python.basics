l = [1, 2, 3, 4, 5, "string", "sun", "moon", "earth", 1.1, 2.2, 3.3, 4.4, 5.5, (1, 1.1, "new string")]
print(" ")

l1_num = []
l2_str = []
l3_other = []
for i in l:
    if type(i) == int or type(i) == float:
        l1_num.append(i)
    elif type(i) == str:
        l2_str.append(i)
    else:
        l3_other.append(i)

print(l1_num)
print(l2_str)
print(l3_other)

print(type(l1_num[0]))
print(type(l2_str[0]))
print(type(l3_other[0]))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, 6.66, 7.7, 8.8, 9.9]

for i in list1:
    print(i, type(i))

for i in l:
    print(i, type(i))

print()
print("Else in for loop")

list2 = ["string", "new string", "sun", "moon", "earth"]

for i in list2:
    print(i)
else:
    print("if for loop isable to compete itself then only else will execute")

print()

print("break, break is a keyword that used to stop a program")
print()

for i in list2:
    if i == "sun":
        break
    print(i)

print()

print("for loop with break and else")

for i in list2:
    if i == "moon":
     break
    print(i)
else:
    print("using break")

print()

print("continue")
print()

for i in list2:
    if i == "sun":
        continue
    print(i)
else:
    print("a")

print()

for i in range(0, 11):
    if i == 1:
        print("world.wide")
    else:
        print(i)
else:
    print("this else is part of for:else loop")

print()

print(str(list((range(100, 200))[0:10])[0:5]))