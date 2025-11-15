numbers = [5, 2, 1, 7, 4]
numbers.append(10)     # append in last
numbers.insert(0, 10)  # insert (index , object)
print(numbers)
# clear()-> remove all item
# pop() -> remove last item
# remove(value)-> remove element
numbers = [2,2,4,6,3,4,6,1]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
# duplicated are removed