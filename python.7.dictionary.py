print("dictionary data type")
d = {}
print(type(d))

d1 = {"key" : "lock"}
print(d1)
print(type(d1))

d2 = {"department" : "Investigation", "phone" : 911, True : 1, "Phone" : 100, 1j : 100j}
print("calling value by key")
print()

print(d2["department"])
print(d2["phone"])
print(d2["Phone"])
print(d2[1j])
print(type(d2["phone"]))

d3 = {"coke" : [{"energy" : "44kacl"}, "total sugars", "total fat", "souium" ]}
print(type(d3["coke"]))
print(d3["coke"][0])
print(d3["coke"][0]["energy"])
print(type(d3["coke"][0]))
print(type(d3["coke"][0]["energy"]))
print(d3["coke"][0]["energy"])

d4 = {"numbers" : {1,1,5,5,9,9,4,4,9j,9j}, "assignment.no." : (1,2,3,4,5), "roll_no." : { 1 : 101, 2 : 201, 3 : 301 }}
print(d4["roll_no."][1])
print(type(str(d4["roll_no."][1])))
print(type(str(d4["roll_no."])))
print(str(d4["roll_no."])[1:100:2])
print(str(d4["roll_no."][1])[1:100:2])
print(str(d4["roll_no."][1])[1:100:2])

print("some dictionary method")
print("adding new key and value")
d2["int"] = [1, 2, 3, 4]
print(d2)
d2[float] = 1.1, 2.1, 3.1, 4.1 #float class
d2["float"] = [1.1, 2.1, 3.1, 4.1]
print(d2)
print(d2[float])
print(d2)
d2["int"][0] = 100
print(d2)
print()

print("delete method")
del d2["int"][0]
print(d2)

del d2["phone"]
print(d2)

print("key method")
print(d2.keys())
print(list(d2.keys())[0])
print(list(d2.keys()))

print("values method")
print(d2.values())
print(list(d2.values()))
print(list(d2.values())[4])
print(d2)

print("items value")
print(d2.items())
print(list(d2.items()))

print("pop method")
d2.pop("float")
print(d2)