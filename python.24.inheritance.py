print("inheritance")
print("parent class and child class \n")


class Parent_class:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_parent_class_init_value(self):
        return self.id, self.name


person1 = Parent_class(1, "name of person 1")
print(person1.print_parent_class_init_value())  # calling a method

print("creating a child class \n")


class Child_class(Parent_class):

    def child_class_method(self):
        pass


person2 = Child_class(2, "name of person 2")  # using init from Parent_class
print(person2.print_parent_class_init_value())  # printing value by Parent_class in print_parent_class_init_value method


class Super_class(Parent_class):
    def __init__(self, id, name, rating):
        super().__init__(id, name)
        self.rating = rating

    def printing_all_info(self):
        return self.rating  # self.id, self.name give error


person3 = Super_class(3, "name of person 3", 5)

print(person3.printing_all_info())
print(person3.print_parent_class_init_value())

print("another example of inheritance")


class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


dog = Dog()
print(dog.sound())  # Bark

print(dir(dog))


class test:

    def test_math(self):
        return "this is from test class and method is test_math"


class child_test(test):
    pass


child_test_obj = test()

print(child_test_obj.test_math())

print("Multiple leval inheritance color")


class Class1:

    def class1_method(self):
        return "this is a Class1:  class1_method"


class Class2(Class1):
    def class2_method(self):
        return "this is a Class2:  class2_method"


class Class3(Class2):
    def class3_method(self):
        pass


obj_Class3 = Class3()

print()

print(obj_Class3.class1_method())
print(obj_Class3.class2_method())
print(obj_Class3.class3_method())

print()

print("multiple inheritance \n")


class Class01:
    def class01_method(self):
        return "this is Class01"


class Class02:
    def Class02_method(self):
        return "this id Class02"


class Class03(Class01, Class02):
    pass


obj_Class03 = Class03()
print(obj_Class03.class01_method())

print(obj_Class03.Class02_method() )