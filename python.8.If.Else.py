print("python if.Else", "or", "Conditions and If statements")
print(" ")
print("""Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b""")
print(" ")
print("simple if")
a = 95
if a > 90:
    print("sun", a)
print()
print("if with else")
a = 911
if a == 91:
    print("police")
else :
    print("other phone number")

print()

print("elif")
a = 94
if a >= 95:
    print("sun", a)
elif a <95:
    print("moon ", a)

print()

print("elif with else")
a = 1
if a == 99:
    print("sun", a)
elif a == 100:
    print("moon", a)
else:
    print("earth", a)

print()

print("if, elif and else with and, or ")

a = 0
list1 = [0, 1, 2]
if a <= 100 and a >= 90:
    print("sun", a)
elif a <= 89 and a >=80:
    print("moon", a)
elif a == 79 or  a == 78:
    print("earth", a)
else:
    (list1.insert(0,100))
    print(list1)

print("use not")
earth = 1
moon = 0
if not earth < moon:
    print("yes")

print("Nested If")
sun = 10000
earth = 1
moon = 0.10
if sun > earth:
    print("true")
if sun > moon:
    print("true")
else:
    print("moon")

print("")

a = 110
if a>100:
    print("h1")
elif a>90:
    print("h2")

print()

a = 110
if a>100:
    print("h1")
if a>90:
    print("h2")


print()

sun = 10000
earth = 1
moon = 0.10
if moon > sun:
    print("true")
else:
     if 1 > 0:
       print("True")
     if 1 > 0:
       print("True")