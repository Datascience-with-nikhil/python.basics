print("sum up the number till sum point")
n = int(input())
starting_point = 0
counter = 1

while counter <= n:
    starting_point = starting_point + counter
    counter = counter + 1

print(starting_point)

print("calculate factorial number")
factorial = 1
number = int(input())
while number > 0:
    factorial = factorial * number
    number = number - 1
print(factorial)

print()

number = int(input())
a, b = 0, 1
counter = 0
while counter < number:
    print(a)
    c = a + b
    a = b
    b = c
    counter = counter + 1

print("break")
i = 0
while i <= 10:
    i = i + 1
    if i == 2:
        break
    print(i)

print("continue")
i = 0
while i <= 10:
    i = i + 1
    if i == 2:
        continue
    print(i)