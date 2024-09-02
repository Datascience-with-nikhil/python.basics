print("python Slice Strings")

s = "Pacific Ocean, Atlantic Ocean, Indian Ocean, Arctic Ocean and the Southern Ocean"
print(type(s))

print("python index")
print(s[0])
print(s[1])
## print(s[100]) # error because string index out of range
print(s[20])
print(s[0])
print(s[0]*10)

print(s[0:100])
print(s[00:100])
print(s[0:])
print(s[:])
print(s[:100])
print(s[1:20])
print(s[1:20]*3)
print(s[10:1]) #give_blank

print(s[::])
print(s[0::])
print(s[00::])
print(s[0:100:])
print(s[0::1])
print(s[::1])
print(s[1:10:])
print(s[1:10:2])
print(s[1:100:2])
print(s[1:100:2]*10)
print(s[10:100:3])
## print(s[10:100:0]) #give_error
print(s[::2])
print(s[::2]*10)
print(s[10:1:2]) #give_blank

print("python Negative Slice Strings")

print(s[::-1])
print(s[::-1]*2)
print(s[100:0:-1])
print(s[00:0:-1]) #give_blank
print(s[0:100:-3]) #give_blank
print(s[100::1]) #give_blank
print(s[:100:-1]) #give_blank
print(s[10:0:-5])
print(s[10:0:-5]*2)
print(s[-1:-100:1]) #give_blank
print(s[-1:-100:-1])
print(s[:50:-1])
print(s[-1:5:-1])
print(s[-1:5:1]) #give_blank
print(s[100:-1:-1]) #give_blank

print("some string function")

print(len(s))
print(s.upper())
print(s.title())
print(s.lower())
print(s.capitalize())
print(s.find("i"))
print(s.find("in")) #not in a string
print(s.find("In"))
print(s.count("i"))
print(s.count("I"))

#bonus excesses

cp = 2 + 4j
t = True
i = 3

print(cp.real*len(s))
print(cp.imag*len(s))
print(s.upper()+" world.wide")
print(s.title()*i)
print(s.lower()*4)
print(s.capitalize()*len(s))
print(s.find("i")+len(s))
print(s.find("in")) #not in a string
print(s.find("In")/len(s))

print(s[0:10-2:1])
print(s[0:10+2:1])
print(s[2*2:10-2:1])
##print(s[0:10/2:1]) #error
print(s[-1:0:-1+(-1)])
print(s[-1:0:-1+-1])
print(s[-1:0:-1])
print(str(True)[1:3])