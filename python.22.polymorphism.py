print("polymorphism")

print(1 + 1)
print("1" + "1")

tuple1 = ("apple", "banana", "cherry")

print(len(tuple1))

print(len("polymorphism"))
print("")

class chemistry:

    def syllabus(self):
        print("this is my syllabus for chemistry")

class geology:

    def syllabus(self):
        print("this is my syllabus for geology")

def gi(class_obj):
    for i in class_obj:
        i.syllabus()

geology1 = geology()
chemistry1 = chemistry()

class_obj = [geology1 , chemistry1]

gi(class_obj)