range = range(2,11)


user_input = input("Pick a number between 2 and 11: ")
int(user_input)

divisors = set()


for elem in range:
    if user_input % elem == 0:
        divisors.add(elem)
    else:
        continue

print(divisors)
