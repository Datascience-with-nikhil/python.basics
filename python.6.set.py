print("set data type")
print("set data types are mutable, unordered, doesn't allows duplicate members and it can store only int, float, complex, string, tuples")

l1 = [2, 3, 4, 2, 3, 4, (2*9j), "string", 3.14]
l2 = [10, 11, 12, 13, 14, 15.1, ["string"]]

t1 = (2, 3, 4, 5, "string", 1.11, 10+7j, [.1, 2, True, 1+7j], (100), [(1000)])
t2 = (1.1, 2.2, 3.3, 3.3, 4.4+5.5j)

st1 = {}
st2 = {2,4,6,7,1.2,9,3,9.4,(1*9j),"string"}
st3 = {3,4.7,3.7,(1,9,"asian.paints")}

set1 = {"a", "b", "c", "d", "e", "f", "g", "h", 1, 2, 3, 4, 5, 6, 3.14}
set2 = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 2, 4, 6, 10, 100.100, 200.2}

s = "wide"

print("type() function")
print(type(st1))
print(type(st2))
print(" ")
##print(st3 + st2) #error
##print(st2 * 2)   #error

print("set() function")
set(s)
print(set(l1))
print(l1)
print(set(t2))
print(t2)
print("")

print("set data types are unordered")
##st2[0] #error
##st3[::] #error

print(list(st2)[0:10:2])
print(" ")

print("some set methods")

print("add() method")                           #aadm
print(set1)

set1.add(10+2)
print(set1)

print(set1.add(20%13))
print(set1)

##print(set1.add({11, 12, 13, 14})) #error
##print(set1.add({100})) #error
##print(set1.add(set2))  #error

print(set1.add(s))
print(set1)

print(set1.add(False))
print(set1.add(True))
print(set1)

##print(set1.add(l1)) #error
print(set1)
print("")

print("remove() method")                     #arem

set1.remove(1)
print(set1)

set1.remove(False)
print(set1)

set1.remove("wide")
print(set1)
print()

print("union() method")

##set1.union(10+10) #error
print(set1.union({10+10}))
print(set1.union({100}))
print(set1)
print("")

print(set1.union(l1)) # only simple list
print(set1.union(s))
print(set1.union(l1[7]))
print(set1.union(str(l1[7][0:2])))

