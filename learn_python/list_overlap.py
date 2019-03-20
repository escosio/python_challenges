list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_overlap = set()

for x in list_b:
    if x in list_a:
        list_overlap.add(x)


print(list_overlap)
