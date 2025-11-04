# It is used to repeat something till condition is True

# x = int(input())
# while (x % 2 == 0):            # infinite loop
#     print("Even")

# or


while True:                     #infinite loop
    command=input(">")
    print("Echo",command)
    if command.lower() == "quit":   #now no infinite with this condition
        break

# or


number = 100
while number > 0:
    print(number)
    number //= 2

# or

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


