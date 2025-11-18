# Files and Directories in python
# we use module pathlib which is oop path
from pathlib import Path  # Path is a class as P is capital

# now we create a path object to refernce a file on a computer
# using 2 ways
# absolute path -> root of hardisk like C:\Program Files\Microsoft ...
# relative path -> a path starting from current directory

# path object
# Path() -> current directory if no argument passed
# path = Path("ecommerce")
path = Path("C:\leetcode\Python\Oops\ecommerce")
print(path.exists())
# print false as path is not correct so u click on ecommerce folder copy its path ans paste
# now true
path = Path("email")
# print(path.exists())   # false
# print(path.mkdir())      # return none  but creates new foler as email
print(path.rmdir())      # remove directory

# to make new directory use mkdir 

