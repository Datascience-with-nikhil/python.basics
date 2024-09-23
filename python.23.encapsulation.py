print("encapsulation")
print("")


class About_cars:

    def __init__(self, horsepower, colour, n_cap_rating, weigh):
        self.horsepower = horsepower
        self.colour = colour
        self.n_cap_rating = n_cap_rating
        self.weigh = weigh


person1_car = About_cars(300, "red", "2", 350)

print(person1_car.horsepower)
print(person1_car.colour)
print(person1_car.n_cap_rating)
print(person1_car.weigh)

print("\n changing a value \n")

person1_car.n_cap_rating = 1
person1_car.colour = "black"

print(person1_car.colour)
print(person1_car.n_cap_rating)

print("applying encapsulation ")


class car:

    def __init__(self, horsepower, colour, n_cap_rating, weigh):
        self.__horsepower = horsepower
        self.__colour = colour
        self.__n_cap_rating = n_cap_rating
        self.__weigh = weigh

    # def print_all_value(self):     # use __ not _
    #     return self.horsepower, self.colour, self.n_cap_rating, self.weigh

    def print_all_value1(self):
        return self.__horsepower, self.__colour, self.__n_cap_rating, self.__weigh

    def set_horsepower(self, horsepower):
        self.__horsepower = 0 if horsepower < 0 else horsepower

    def get_horsepower(self):
        return self.__horsepower


person1 = car(589, "white", 5, 299)
print("this is a method to modify a encamped value")
# print(person1.horsepower) # error
# print(person1._car__horsepower) #589

person1._car__n_cap_rating = 4 # change value
print(person1._car__n_cap_rating) #100

print(person1.print_all_value1())

person1.set_horsepower(782)

print(person1.print_all_value1())

print(person1.get_horsepower())