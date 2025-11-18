# Inheritance in python
# child class or sub class inherits the property from its parent or super class
# class Dog:
#     def walk(self):
#         print("walk")

class Mammal:                      # parent class
    def walk(self):
        print("walk")


# a class in python cannot be empty
class Dog(Mammal):                       # child class to inherit from parent class -> mammal
    # pass                               # pass means nothing just pass this
    def bark(self):
        print("bark")
# i define another function inside dog
# or we can take any method
# dog class inheriting the walk method from mamal


class Cat(Mammal):
    pass

    def meow(self):
        print("meow")


# now create object
dog1 = Dog()    # object
dog1.walk()     # parent
dog1.bark()     # child
cat1 = Cat()    # object
cat1.walk()     # parent
cat1.meow()     # child
# here we call another method bark
# both cat and dog class is inheriting the method(walk) defined in parent class (mammal)
# we create object to call that class using dog or cat
