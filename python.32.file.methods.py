print("files different operations")

f = open("test1.txt", "a")

f.write("this a 'test1.txt' file")

f.close()

f = open("test1.txt", "r")

print(f.read())

print("use seek to point a pointer \n")
f.seek(0)

print("by for loop can print a value \n")
for i in f:
    print(i)

f.seek(0)

for i in f:
    print(i)

print("a1 \n")
f.seek(0)
a = f.read()
print(a)

print("a2 \n")
f.seek(0)
print(f.read())

f.seek(0)

for i in f:
    print(i.upper())

f.seek(0)

print(f.read()[100:0:-1].upper())

f.close()

print("by help of os package can perform many operation")

print("create a copy")
import shutil

f1 = open("copy.txt", "a")
shutil.copy("copy.txt", "copy1.txt")

import os

print("know file size")
print(os.path.getsize("test1.txt"))

print("remove a file")
os.remove("copy1.txt")  # in this line removing file

print("change a file")
f2 = open("a1.txt", "w")
#os.rename("a1.txt", "a1.txt")  #only one time work

print("method of opening a file by with open")


with open("text001.txt", "a") as f:
    f.write("moon and mars")
