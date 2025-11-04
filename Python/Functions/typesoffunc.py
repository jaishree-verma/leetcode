# Types of Fucntion
# 1-> Perform a task (print something on terminal)
# 2-> Calculate & Return a value

print(round(1.9))     # 1 type -> to print something on terminal

# or


def greet(name):
    # 1 type -> we have to write soemthing to get a value so that part is type 2
    print(f"Hi {name}")


print(greet("Jaishree"))    # by default all funtion in python returns null


# or


def get_greeting(name):
    return f"Hi {name}"   # 2 type -> return value


message = get_greeting("Jaishree")
print(message)                      # return value
