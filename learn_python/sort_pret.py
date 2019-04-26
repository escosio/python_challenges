a = [1, 2, 1, 4, 6, 7]


# print(a.sort())


# OR

count = 0
item_a = a[count]
item_b = b[count+

def sort_nums():
    if item_a <= item_b:
        pass
    elif item_a > item_b:
        a[count] = item_b
        a[count+1] = item_a
        count = count +1

for num in a:
    sort_nums()

'''
func that compares two items
    if a <= b:
        pass
    elif a > b:
        list[]


'''
