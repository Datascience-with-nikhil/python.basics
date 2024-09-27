print("class method")

class Parent_class:

    def __init__(self, id, mail):
        self.id = id
        self.mail = mail

    def parent_class_method_student_info(self):
        return self.id, self.mail

parent_class_obj = Parent_class(1, "1id@mail.com")

print(parent_class_obj.mail)
print(parent_class_obj.id)
parent_class_obj.parent_class_method_student_info()
print(type(parent_class_obj.parent_class_method_student_info()))

print("")

class Parent_class1:

    def __init__(self, id, mail):
        self.id = id
        self.mail = mail

    # @classmethod  # decorators
    # def stu_details(cls, name): #missing one argument
    #     return cls(name)

    @classmethod
    def stu_details(cls, name, news):
        return cls(name, news)

    def parent_class_method_student_information(self):
        return self.id, self.mail


print()

##Parent_class1.stu_details() #error missing 2 required positional arguments: 'name' and 'news'
##Parent_class1.parent_class_method_student_info()

Parent_class1.stu_details("mark", "yes")  # without creating object pass a value

##class_method_obj = stu_details("mark", "yes") #error
class_method_obj = Parent_class1.stu_details("mark", "yes")

print(class_method_obj.parent_class_method_student_information())
print(class_method_obj.mail)
print(class_method_obj.id)

print("class variable")


class Parent_class2:
    class_variable = 2648549376

    def __init__(self, id, mail):
        self.id = id
        self.mail = mail

    # @classmethod  # decorators
    # def stu_details(cls, name): #missing one argument
    #     return cls(name)

    @classmethod
    def change_mobile_number(cls, mobile):
        Parent_class2.mob_no = mobile

    @classmethod
    def stu_details(cls, name, news):
        return cls(name, news)

    def parent_class_method_student_information(self):
        return self.id, self.mail, Parent_class2.class_variable


#class_variable_obj = Parent_class2() #error

print(Parent_class2.class_variable)

print(Parent_class2.change_mobile_number(3438934285))

print(Parent_class2.class_variable)

print("print class_variable")

obj1 = Parent_class2(1, 2)
print(obj1.parent_class_method_student_information())

obj2 = Parent_class2.stu_details(1, 1) # creating a class method(@classmethod) object and printing class_variable
print(obj2.parent_class_method_student_information())

print("add a variable in a class")

class Parent_class3:

    def __init__(self, id, mail):
        self.id = id
        self.mail = mail

    # @classmethod  # decorators
    # def stu_details(cls, name): #missing one argument
    #     return cls(name)


    @classmethod
    def stu_details(cls, name, news):
        return cls(name, news)

    def parent_class_method_student_information(self):
        return self.id, self.mail

def loca(self, location):
    self.location = location
    return location

Parent_class3.loca = classmethod(loca)

# print(Parent_class3.loca(1000))

print("deactivate any method")

del Parent_class1.stu_details

delattr(Parent_class2, "change_mobile_number")