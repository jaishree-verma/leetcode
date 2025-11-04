# Keyword Arguments
# It means declare value with variable name inside argument part for parameter which is being passed
def increment(number, by):
    return number+by


# result = increment(2, 1)
# print(result)

# or -> we dont really need result variable

print(increment(2, by=1))          # keyword argument -> by = 2 (more readable)
