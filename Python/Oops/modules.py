# Module in Python
# a module in python is a file with come code
# will make combine these function into one by importing a module through seperating these functions into different file
# we will import through moduleimport
# def lbs_to_kg(weight):
#     return weight * 0.45


# def kg_to_lbs(weight):
#     return weight / 0.45

# import moduleimport
# print(moduleimport.kg_to_lbs(70))              # this way we use thing method through import file as modules
# print(moduleimport.lbs_to_kg(70))

# or

# directly call this function only not whole module using import
from utils import find_max
import moduleimport
# we import a specific function from our module then we just call that passing value no need to print
# press ctrl + space after import to view all functionc
from moduleimport import kg_to_lbs

kg_to_lbs(100)                                 # same as line 13


# make a function find_max() and put it in a module to import as utils
# making function
# def find_max(numbers):
#     max = number[0]
#     for number in numbers:
#         if number > max:
#             max = number
#     return max


# numbers = [10,3,6,2]
# now we will put this in seperate file named as util to import
from utils import find_max                      # this is for specific function in module util
numbers = [10, 3, 6, 2]                             # define list of numbers
# we pass this as a argument and store in max and finally print max
max = find_max(numbers)
print(max)                     # output = 10

# or 
import utils                                    # this is whole module 
numbers = [10,3,6,2]
print(utils.find_max(numbers))