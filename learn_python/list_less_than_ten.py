a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than_5 = list()

# for number in a:
#     if number < 5:
#         # print(number)
#         less_than_5.append(number)
#     else:
#         continue
user_number = input("Enter a number from 1 to 100: ")
int(user_number)

for number in a:
    if number < user_number:
        less_than_5.append(number)
    else:
        continue

print(less_than_5)
