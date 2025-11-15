coordinates = (1, 2, 3)
# coordinates[0] * coordinates[1] * coordinates[2] very long
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# unpacking is to achieve same result with less code
x, y, z = coordinates  # same as line 3,4,5
# x = 1
# y = 2
# z = 3
print(x)
print(y)
print(z)
