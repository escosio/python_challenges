import random
import string

get_int = str(random.randrange(10))
get_lower = random.choice(string.ascii_letters).lower()
get_upper = random.choice(string.ascii_letters)
options = [get_int,get_lower,get_upper]
x = ""

def choose_char(x):
    new_char = random.choice(options)
    x = x + new_char

choose_char(x)
print(x)

# def generate_pass():



'''
write func to choose randomly from variables that will choose either a random number or a random letter
run that function 16 times
random int
random lowercase
random uppercase
random unique character
then shuffle

'''
