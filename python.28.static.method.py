print("static method")

class Student_class:

    def student_details(self, name, mail_id, id_number):
        print(name, mail_id, id_number)


Student_class_object = Student_class()

Student_class_object.student_details("mark", "mark@mail.com", 1)


class student_class:

    def student_details(self, name, mail_id, number):
        return name, mail_id, number

    def student_subject_names(list_of_subject_names):
        print(list_of_subject_names)

student_class.student_subject_names(["history", "chemistry"]) # without creating an object can use class method

print("class under static")
print("static under static")
class student_class3:

    def student_details(self, name, mail_id, number):
        return name, mail_id, number

    @staticmethod
    def student_subject_code(list_of_subject_code):
        print(list_of_subject_code)

    @staticmethod
    def student_subject_names(list_of_subject_names):
        student_class3.student_subject_code(["hir01", "che02"])
        print(list_of_subject_names)

    @classmethod
    def student_class_method(cls):
        cls.student_subject_names([['history', 'chemistry']])

student_class3.student_class_method()

student_class3.student_subject_code(['history', 'chemistry'])
print("object orientated  ")