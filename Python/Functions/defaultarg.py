# Default Argument
def increment(number, by=1):    # Default value of by = 7
    return number+by
# print(increment(2))

# or


# now this by = 5 not 1 as it overwrites the initial default argument of by that is 1
print(increment(2, 5))

# all option parameters should come before required one


# optional paaremter added beofre required one means before by
def increment(number, another_number, by=1):
    return ((number * another_number) + by)     # any operation


print(increment(2, 3, 1))

# or


def square(numbers):
    return numbers*numbers


print(square(5))

# or


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# they are tuples which are iterable & used in loops
print(multiply(2, 3, 4, 5))     # product of these numbers is 120
