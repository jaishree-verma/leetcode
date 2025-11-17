# how to return a function
# by default all function python returns none
def square(number):
    return number * number        # this will return sqaure of that number


# square(5)
# square(5)  or we can store this value in a variable and print that variable contaning the value which is final ans
result = square(5)
print(result)
print(square(6))   # this way also we can print 

# if we dont use return then, 
def cube(numbers):
    print(numbers * numbers * numbers)

# cube(3)
# or
print(cube(3))      # this gives none too as control moves to sqaure function and by default all function returns value none so to avoid it we use return