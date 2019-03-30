a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c = [item for item in a if item in a if item in b]
#
# print(c)
c = list()

for item in a:
    if item in a:
        c.append(item)

for item in b:
    if item in b:
        c.append(item)

print(c)
