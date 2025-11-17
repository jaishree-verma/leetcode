# Classes in python
# Think of a class like a template, and the object as the actual thing built from that template
# Objects created from a class are instances
# we use classes to use new types to model real concepts
# to define we use class + class_name and perform methods inside it
# use uppercase (P for point) called as pascal naming convention for class and rest variables or function use lowercase
class Point:
    # block -> fucntions or methods that belong to point
    def move(self):    # move is a func    # method 1
        print("move")

    def draw(self):   # draw is a func     # method 1
        print("draw")


# now we create object with thse 2 point class methods
# Object is a instance of a class
# A class defined a blueprint for creating objects
# Objects are actual instances based on that blueprint
point1 = Point()    # creates a new object like a function and we store it in a variable
# it automatically shows ur function and methods which u used and then it prints
point1.draw()
point1.move()

# apart from methods we can have attributes that are vraibles that belong to particular object
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
print(point1.y)

# another object
# type name of class and call it as object
point2 = Point()
# print(poin2.x)    # hence error cause it does not have any attribute
# each object is a different instance of a point class
point2.x = 1     # attribute so now no error simple output is 1
print(point2.x)


# summary
# -> classes are used to define new types
# -> these types can have methods that can be define inside body of class
# -> and they can have attribute anywhere

# self → refers to the current object
# Attributes → variables inside class
# Methods → functions inside class
# Class: House Blueprint
# Objects: Actual houses built from that blueprint
# Every house has
# number of rooms (attribute)
# paint color (attribute)
# open_door() (method)