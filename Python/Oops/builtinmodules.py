# Some Built in modules in python
# 1-> random module
# 2-> randint module
# 3-> choice module
import random
# use random.method ( to access it methods inside random module)
for i in range(3):
    # print(random.random())
    # random values between range 
    print(random.randint(10, 20))


# randomly pick items from a list
members = ['Jaishree','Mary','Bob','Alice']
# to pick any random member we use choice
print(random.choice(members))


#  roll a dice
# class dice 
# a method roll() -> call we get tuple always ( cannt add or remove items from tuples)

