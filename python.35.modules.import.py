print("modules and import statements")
import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from subject import subject_file


def student_fun():
    print("name of student, and roll number of student")


subject_file.subject_fun()


# from subject import subject_file as aa1
##subject_file.subject_fun() #error
# aa1.subject_fun()

# print("only import a specific function")
# from newfile import add #newfile in a same package
# obj1 = add(1, 2)
# print(obj1)

# from newfile import *
# x = add(1, 1)
# print(x)

# from newfile import *
# subject_fun()

# print("import same name function so how to handle this problem")
#
# import newfile as t1
# import newfile1 as t2
#
# t1.subject_fun()
# t2.subject_fun()

# print("from different package import a file")
# import subject.subject_file as aa
# aa.subject_fun()