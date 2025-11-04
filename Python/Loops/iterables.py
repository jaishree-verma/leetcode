# Iterables mean we can iterate over it
# Example here is range function which comes under complex type
print(type(range(5)))              # complex
for x in range(5):                 # iterable range
    print("a")

for x in "Python":                 # iterable string
    print(x) 

for x in [1, 2, 3, 4, 5,"A","B"]:  # iterable list
    print(x)

for x in (1,2,3,4,5,"A","B"):      # iterable tuple
    print(x)

shopping_cart=["Apple","Oranges","Bag","Bottle"]  
for item in shopping_cart:                        
    print(item)
