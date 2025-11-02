# What are strings?
# It is a datatype & sequence of characters in " "
# It is immuatble (cannot change)
course = "Python Programming"
print(course)
# What is a function
# A function is reuseable piece of code that carries out a task.
# There are builtin function like len(),endswith(),count(),capitalise(),startswith(),upper(),lower(),title(),find(),replace()
print(len(course))
# In Python to access string functions or better to say methods we use dot(.) operator
# course.methodname -> course = object , . = to access , methodname = desired methods required to perform certain question
print(course.endswith("g"))
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.endswith("y"))
print(course.count("P"))
print(course.count("s"))
print(course.capitalize())
print(course.startswith("P"))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find("g"))
print(course.replace("P", "j"))
print(course[0])
# Slicing-> gives the desired part of string by using index starting from 0 (starting first) or -1 (starts with end)
# course[1:3] chr of last index number that is 3 not included hence it goes from (1) to (course-1)
print(course[1:3])
print(course[-1])
print(course[0:5])
print(course[0:18])
print("Pro" in course)
print("pro" in course)
print("java" not in course)
print("Pro" not in course)
