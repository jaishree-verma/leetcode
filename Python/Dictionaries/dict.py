# dict are key : value pairs
customer = {
    "name": "Jaishree Verma",
    "country": "India",
}
# each key should be unquie like real english dictionary no duplicacy
print(type(customer))
print(customer["name"])     # access value
# print(customer["age"])      # error no key as age
print(customer.get("name"))
print(customer.get("age"))   # get return none not error since it means no value 
print(customer.get("age","Nov"))   # but now when you use get with a value assign then it returns that value 


# git add .
# git commit -m "Basics of Python"
# git push -u origin main

