# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.

list_1 = [1,1,2,2,3,3,4,4,5]
set_1 = set()

'''
def remove_dupe(list):
    for x in list:
        set_1.add(x)


remove_dupe(list_1)
print(set_1)
'''

s = set(list_1)
print(s)
