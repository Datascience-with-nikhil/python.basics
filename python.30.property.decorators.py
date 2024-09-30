print("property decorators getter, setters and deletes")


class Student:

    def __init__(self, student_id, student_name):
        self.__student_id = student_id
        self.student_name = student_name

    def print_student_information(self):
        return self.__student_id, self.student_name

    @property
    def student_id_access(self):
        return self.__student_id

    @student_id_access.setter
    def student_id_set(self, id_number):
        if id_number == 1:
            pass
        else:
            self.__student_id = id_number

    @student_id_access.deleter
    def delete_student_id(self):
        del self.__student_id


student_class_object = Student(1, "student 1")

print(student_class_object.print_student_information())

student_class_object.__student_id = 2 #not give error but wrong
print(student_class_object.print_student_information())
##print(student_class_object.__student_id) #error

print("by help of property decorator can access a privet variable")

print(student_class_object.student_id_access)
print("or but wrong method")
##print(student_class_object._Student__student_id) #wrong method

print("set")

student_class_object.student_id_set = 2
print(student_class_object.student_id_access)

print("delattr")

print(student_class_object.student_id_access)

del student_class_object.delete_student_id

##print(student_class_object.student_id_access) #'Student' object has no attribute '_Student__student_id'