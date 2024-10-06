print("exceptions handling")

a = 1

##b = 1/0 # error

##f = open("test.txt", "r") #error

print("try and except \n")

print("in try block error")
try:
    f = open("test.txt", "r") # not give error
    f.write("this is a test file")
    f.close()
except Exception as a:
    print("this is a except block \n")


try :
    f = open("test.txt", "r")
    f.write("this is a test file")
    f.close()
except Exception as a:
    print("this is except block", a)
a = 1 + 1
print(a)

print("when try block work")

try :
    f = open("test.txt", "a")
    f.write("test.txt file")
    a = 1 + 1
    print(a)
except Exception as a:
    print("this is except block", a)
    a = 1 + 1
    print(a)

a1 = "# else block is a block that work when try block run without any error"

print("try, except and else")
try :
    f = open("test.txt", "a")
    f.write("test.txt file \n")
    f.write(a1)
    a = 1 + 1
    print(a)
except Exception as a:
    print("this is except block", a)
else:
    f.write("this is else block")
    f.close()
    print("world.wide")

try :
    f = open("test1.txt", "r")
    f.write("test.txt file")
    a = 1 + 1
    print(a)
except Exception as a:
    print("this is except block", a)
else:
    f.write("this is else block")
    f.close()
    print("world.wide")

print("try and finally")

try :
    f = open("test2.txt", "w")
    f.write("this is try opening test2.txt \n")
finally:
    print("finally will execute itself in any situation")


try :
    f = open("test3.txt", "w")
    f.write("this is try opening test2.txt \n")
finally:
    print("finally will execute itself in any situation")

f.write("write")
