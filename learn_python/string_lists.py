user_word=input("Give me a word and I'll tell you if it's a palindrome or not: ")

word = list()

for letter in user_word:
    word.append(letter)

# get number of letters in list
length_of_word = len(user_word)

 # subtract -1 from list to get value of the last item
 # save that value as index_b
index_b = length_of_word - 1
# set index_a to zero
index_a = 0

letter_a = word[index_a]
letter_b = word[index_b]


while index_a < index_b:
    if letter_a == letter_b:
        index_a = index_a + 1
        index_b = index_b - 1
        letter_a = word[index_a]
        letter_b = word[index_b]
        if index_a + 1 == index_b:
            print("This is a palindrome")
            break
    else:
        print("This is not a palindrome")
        break


'''

'''
