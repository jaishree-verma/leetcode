# There are operators in python like and,or,not
# These boolean are short circuit evalution means if a if statement is true it reads till last condition and if a if statement got false
# then it stop right there like high_income is first to see n if it is false then condition stops right there else if true then reads till last.
# AND -> both conditions true result true
high_income = True
good_credit = True
# good_credit=False
if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")

# OR -> # OR -> If one is false and other true result is true
high_income = False
good_credit = True
if (high_income or good_credit):
    print("Eligible")
else:
    print("Not Eligible")

# Not -> inversion value of boolean as True = False and vice versa
high_income = True
good_credit = True
# student = True
student = False
if not student:
    print("Eligible")
