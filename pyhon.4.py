i = 5
flo = 3.14
t = True
f = False
cp = 9+3j
s = "original.string"
l = [2, 4.4, True, "this.is.string", 4+7j, ["list", 10, True], [2.14, ["call", 911]]]
l1 = [2, 4.4, True, "this.is.string", 4+7j, ["list", 10, True], [2.14, ["call", 911]],"!!!"]
l2 = ["asian.paints"]

print(type(l))
print(l * i)
print(l * f)
print(l * t)

print("but")

##print(l * flo) #error
##print(l + 7)   #error
##print(l + s)   #error

print("so")

print(l + [i])
print(type([i]))
h = [i]            # because int are immutable
print(type(h))

print(l + [s])
print(type([s]))
hs = [s]            # because string are immutable
print(type(hs))
print([s])
print(hs)

print(l + l2)
print(l)
print(l2)

##print(l + s) #error
print(l + [s])
print(l)

print(list(s))  # using list function
print(str(l))  # using string(str) function

## print(list(i)) #error
## print(list(t)) #error
## print(list(cp)) #error
## print(list(flo)) #error

print("in list can change any index data because list are mutable data type")
l[0] = 100
print(l) # because list are mutable data type

print("print 'this' from variable l")
print(l[3][0:4])

print("print 'tr' from l")
print(l[3][0:2])

print("print 'tu' from variable l")
print(str(l[2])[0:2])

print("some list methods")

print("len() method")
print(len(l))
print(len(l2))

print("append()")
print(l.append(100))
print(l.append("100"))
print(l)

print("extend() method")
l.extend("aws")
print(l)
print(l.extend(s))
print(l)
print(l.extend(l))
print(l)
print(len(l))

print("insert() method")
l.insert(0,1.123)
print(l)
l.insert(-1,"@@")
print(l)
l.insert(-0,"##")
print(l)
l.insert(0,100/5)
print(l)

print("pop() method")
print(l1)
l1.pop()
print(l1)

l1.pop(-1)
print(l1)

l1.pop(1)
print(l1)

l1.pop(0+1)
print(l1)

l1[3].pop(1)
print(l1)

print("remove() method")
print(l)
l.remove("a")
print(l)
print(l.remove("a"))
print(l[8].remove(10))
print(l)

print("reverse() method")
l.reverse()
print(l)
l.reverse()
print(l)

l1[3].reverse()
print(l1)

print("sort() method")
l3 = [1,2,3,0,1.2,.2,.832,.2,.2,1,10,True,False]
print(l3)

print(l3.sort())
print(l3)

print("index() method")
print(l.index("##"))
print(l)
print(l.index("w"))
print(l[8].index("list"))
print(l.index(100,5,100))

print("count() method")
print(l.count(100))
print(l[8].count("list"))