x = input("x: ")
# y = x+1
# here input comes as a string so error because of type error as "1" != 1 in python
# so type conversion string to number to get output
y = int(x)+1
print(x,y)
print(f"x:{x},y:{y}")
