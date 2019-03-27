import random

num = random.randint(1,9)
print(num)

user_num = input("Pick a number from 1 to 9: ")
user_num = int(user_num)

while user_num != num:
    if user_num > num:
        user_num = int(input("Nope that's too high. Guess again."))
    elif user_num < num:
        user_num = int(input("Too low! Guess again."))

print("You got it. The number was " + str(num))
