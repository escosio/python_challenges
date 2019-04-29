# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# test_string = "my name is Scott"
test_string = input("Send us a string: ")

test_list = test_string.split()

index = len(test_list) - 1

new_list = list()


while index >= 0:
    word = str(test_list[index])
    new_list.append(word)
    index = index - 1


str1 = ' '.join(new_list)
print(str1)


'''
get the highest value
write func to print the last value in list
    then decrease the index by 1 until index is >= 0


'''
