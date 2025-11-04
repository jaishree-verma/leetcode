for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# or

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successfull")
        break

# or

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successfull")
        break
else:
    print("Attempted 3 times and failed")