# Conditioal Statements -> to write conditions in a code.
# if,elif,else
# temperature = 15
temperature = 15
if temperature > 30:
    print("Its warm")
    print("Drink water")
elif temperature > 20:
    print("Its nice")
else:
    print("Its cold")
print("Done")

# if a person in university valid to vote or note
# condition if a student > 18 -> eligible else not

age = 20
if (age > 18):
    print("You can vote")
else:
    print("You cannot vote")

# or

age = 20
if (age > 18):
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# or

age = 30
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
