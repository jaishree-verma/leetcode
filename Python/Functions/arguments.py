# Arguments are written inside function take value or to use it as a value
# Argument is the actual balue you give to parameter
# Parameter is where you have to insert a value
def greet(first_name, last_name):   # Parameter->i/p define to a function -> first_name & last_name
    print(f"Hi {first_name} {last_name}")
    print("How are you ?")


# Arguments -> actual value assign to a parameter
# Aguments-> jaishree & verma and these are positional arguments
greet("Jaishree", "Verma")
# greet("first_name=Jaishree ", "last_name = Verma")  this is keyword arugument 

# or


def sum(a, b):  # (a,b)-> Parameter
    print(a+b)  # value pass to perform calculatioms


sum(1, 2)  # call a function , (1,2)-> argument
# basically when calling a fucntion we say arugments but when defining we say paramters
