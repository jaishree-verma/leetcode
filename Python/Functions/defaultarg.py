# Default Argument
def increment(number, by=1):    # Default value of by = 7
    return number+by
# print(increment(2))

# or


# now this by = 5 not 1 as it overwrites the initial default argument of by that is 1
print(increment(2, 5))

# all option parameters should come before required one


def increment(number, another_number, by=1):    # optional paaremter added beofre required one means before by 
    return ((number * another_number) + by)     # any operation


print(increment(2, 3, 1))
