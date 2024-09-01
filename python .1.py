# print function and arithmetic operations

print("basic arithmetic operations")
print(1 + 1)
print(2 * 2)
print(2 / 2)
print(2 - 1)
print(16 % 3)

# print by use of ,

print(1+1, 4*100, 12/5)

# variable declaration and some basic data types

print("variable declaration")
i = 100
flo = 100.1
s = "world wide"
s1 = 'b2 air bomber'
s2 = '''s
        400'''
s3 = """electron, proton
          and neutron """
t = True   # value of True is 1
f = False  # value of False is 0
cp = 2+7j
cp1 = 1
cp2 = 3j
cp3 = 1J+89j

print("printing variable values")
print(i)
print(flo)
print(s)
print(s1)
print(s2)
print(s3)
print(t)
print(f)
print(cp)


a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = "airbus"
print(x)
print(y)
print(z)

# type function
print(type(i))
print(type(flo))
print(type(s))
print(type(t))
print(type(f))
print(type(cp))
print(type(1*1.1))

## print(type(i,s,t) #error

# between True and False arithmatic operations
print(t+f)
print(t-f)
print(f-t)
print(f*t)
print(f/t)

print(t+100)
print(100-f)
print(f*flo)

print(t+1)
print(t*flo)
print(t+f+i*flo)

# string
print(s*i)
print(s*10)
##print(s*1.01) #error
print(s*t)
print(s*f) # give_blank

# I'DF real and imag number's from ccomplex data typs

print(cp.real)
print(cp.imag)
print(cp3.imag)
print(cp3.real)
print(cp1.imag)

# I'DF real and imag number's from int,bool,float
print(i.real)
print(i.imag)
print(t.real)
print(t.imag)
print(f.imag)
print(f.real)
print(flo.real)
print(flo.imag)

#bonus excesses

print(cp3.imag*flo*i)
print(cp2.real+100)
print(cp2.imag+100)
print(cp.imag*t)
print(cp.imag/2)
print(cp.real)