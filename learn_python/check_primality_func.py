'''
get number from user
get range of numbers less than number

check_prime(x):

check_prime(x):
    for x in potential_divisors:
        if num % x =< 0:
            pass
        elif num % x > 0:
            print(str(x) + "number is not prime")

'''

import sys

user_num = int(input("Pick a number and i'll tell you if it's prime: "))

potential_divisors = range(2,user_num)

def check_prime(x):
    if user_num % x > 0:
        pass
    elif user_num % x == 0:
        sys.exit(str(user_num)+ " is prime.")


for num_in_range in potential_divisors:   # looping through all possible divisors
    check_prime(num_in_range)

print(str(user_num) + " is not a prime number.")
