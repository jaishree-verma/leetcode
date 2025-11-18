# util module as find_max
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


numbers = [10,3,6,2]

# now we will import in module.py file