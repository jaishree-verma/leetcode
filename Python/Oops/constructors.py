# Constructors
# it a function that gets called at a time of creating objects
# we need to add special methods in the class as constructors
# we will use init as short of initialise ( function / methods gets called when we create new point object)
class Point:
    def __init__(self, x, y):    # we set extra parameters as x and y
        # initialise x and y using self that refernce to cuurent object  self.x ( x is arugment) = x ( x passed function )
        self.x = x
        self.y = y


point = Point(10, 20)
# here we created new point object so self refernce that object in memory as same refernce use here
point.x = 11
print(point.x)


# ex
class Person:                     # Person -> class or type
    def __init__(self, name):
        self.name = name          # name -> attribute

    def talk(self):               # talk() -> method
        print("talk")


jaishree = Person("Jaishree Verma")               # object
print(jaishree.name)
jaishree.talk()
