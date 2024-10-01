# print("working with files")
#
#
# print("reading a file")
#
# f = open("test1.txt", "r")
# # "r" is default
# print(f)
#
# text = f.read()  # if "w" is present in a  place if "r" then give error
# print(text)
# f.close()
#
#
# print("writing a file")
#
# f = open("test1.txt", "w")
# f.write("this is a first comment in test1.txt file")
#
# f.close() # write a close is important


print("readline method")

f = open("test1.txt", "r")

text1 = f.read()
print(text1)

print(type(text1))
print("by help of for loop print a value")

for i in f:
    print(i)

f.seek(0)
line = f.readline()
print(line)

f.close()

f = open("test1.txt", "r")
text3 = f.read(10) # give number of charters
print(text3)

f.seek(0)

text4 = f.readline() # \n is hide
print(text4)

f.close()

print("append method")

f = open("test1.txt", "a")

f.write("\nthis is a second comment on file name 'text.txt' ")

f = open("test1.txt", "r")
text5 = f.read()
print(text5)

f.close()

print("if file is not exist and called a open() with 'w' or 'a' then file will be created automatically")

f1 = open("test3.txt", "w")

f1.write("new file 'test3.txt'")


