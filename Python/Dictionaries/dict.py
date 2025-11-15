# dict are key : value pairs
customer = {
    "name": "Jaishree Verma",
    "country": "India",
}
# or add like this
customer["birthdate"] = "Nov 16"
print(customer["birthdate"])
# each key should be unquie like real english dictionary no duplicacy
print(type(customer))
print(customer["name"])     # access value
# print(customer["age"])      # error no key as age
print(customer.get("name"))
# get return none not error since it means no value
print(customer.get("age"))
# but now when you use get with a value assign then it returns that value
print(customer.get("age", "Nov"))


# git add .
# git commit -m "Basics of Python"
# git push -u origin main
