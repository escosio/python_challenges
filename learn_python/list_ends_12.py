a = [5, 10, 15, 20, 25]  # existing list
new = list()    # creates new list

list_length = len(a)  # gets length of entire list
last_item = list_length - 1  # subtracts one for last index value and returns value

first = a[0]    # gets first value in list
last = a[last_item]   # gets last value in list

new.append(first)
new.append(last)

print(new)
