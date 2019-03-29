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

user_num = int(input("Pick a number and i'll tell you if it's prime"))

potential_divisors = range(2,user_num)

def check_prime(x):
    for x in potential_divisors:
        if user_num / x <= 0:
            pass
        elif user_num / x > 0:
            print(str(x) + " number is not prime")

check_prime(user_num)
