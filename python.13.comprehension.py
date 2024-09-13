print("Comprehensions in Python")
print(""" 4 types of comprehension:
          • List Comprehensions
          • Dictionary Comprehensions 
          • Set Comprehensions
          • Generator Comprehensions """)

list1 = [1, 2, 3, 4, 5, 1.1, 2.2, 3.3, 4.4, 5.5]
l1 = []

for i in list1:
    l1.append(i**2)

print(l1)

print("list comprehension")

l_c1 = [ i ** 2 for i in list1]
print(l_c1)
print()

l_c2 = [i ** 3 for i in list1 if i % 2 == 0]
print(l_c2)

l2_int = []
l2_float = []
l_c3 = [l2_int.append(i) if type(i) == int else l2_float.append(i) for i in list1]
print(l2_int)
print(l2_float)
print(l_c3)

print()

print("using for and if")

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l_com = [i for i in list2 if i % 2 == 0]
print(l_com)
l_com1 = [i for i in list2 if i % 2 == 1]
print(l_com1)

print("using for, if and else")

l_com2 = [ i**3 if i<= 5 else i**2 for i in list2]
print(l_com2)

print("if and else")

l_com3 = ["yes 1>0" if 1>0 else 100]
print(l_com3)

print("dictionary comprehension")

d = {"ocean" : 4, "continuances" : 7}
d_com = {k:v * 2 for k, v in d.items()}
print(d_com)

d_com1 = {v * 2 for v in d.values()}
print(d_com1)

print("dictionary comprehension with if")

d_com2 = {k:v for k, v in d.items() if v >= 7}
print(d_com2)