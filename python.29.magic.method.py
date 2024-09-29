print("magic method or dunder method")
a = 1
print(a + 1)

print(dir(int))
print(dir(str))

print(a.__add__(1))

class Student:

    def __init__(self):

        self.id_number = 1

student_class_object = Student()

print(student_class_object.id_number)


class Student_2:

    def __add__(cls):
        print("__add__")

    def __init__(self):
        print("__init__")
        self.id_number = 1

student_2_class_object = Student_2()
print(student_2_class_object)
print(student_2_class_object.id_number)