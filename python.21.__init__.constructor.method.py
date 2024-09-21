print("__init__ method, constructor")


class soft_drinks:  # creating a class

    def __init__(self, energy, sugar, sodium):  # creating a __init__ method function
        self.energy_calories = energy  # self.energy_calories is class variable
        self.sugar_gram = sugar
        self.sodium_mg = sodium

    def soft_drink_information(self):  # creating a function that return __init__ values
        return self.energy_calories, self.sugar_gram, self.sodium_mg


##coke = soft_drinks()       #  required positional arguments

cok = soft_drinks(440, 10.5, 8.5)

## cok = soft_drinks() #error required positional arguments

print(cok.soft_drink_information())
print(cok.energy_calories)
print(cok.sodium_mg)
print(cok.sugar_gram)

print()

print(type(soft_drinks))
print(type(cok))

## print(type(sodium_mg)) #error
## print(type(soft_drink_information)) #error


class soft_drink1:  # creating a class

    def __init__(self, energy, sugar, sodium):
        self.energy_calories = complex(energy) + 100j
        self.sugar_gram = sugar
        self.sodium_mg = float(sodium)

    def soft_drink_information(self):
        return self.energy_calories, self.sugar_gram, str(self.sodium_mg)

fro = soft_drink1(100,20,3)
print(fro.soft_drink_information())