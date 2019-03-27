user_a_input = input("Player one enter your move: ")

plays = ["paper","rock","scissors"]

# TODO make it into a function 
while user_a_input not in plays:
    user_a_input = input("Not a play. Enter it again ")

user_b_input = input("Now player two, enter your move: ")

while user_b_input not in plays:
    user_b_input = input("Not a play. Enter it again ")

while user_a_input != user_b_input:
        if user_a_input == "paper":
            if user_b_input == "scissors":
                print("Player two wins, scissors beats paper")
                break
            else:
                print("Player one wins! Paper beats rock")
                break
        elif user_a_input == "rock":
            if user_b_input == "paper":
                print("Player two wins, paper beats rock")
                break
            else:
                print("Player one wins! rock beats scissors")
                break
        elif user_a_input == "scissors":
            if user_b_input == "paper":
                print("Player two wins, paper beats scissors")
                break
            else:
                print("Player one wins! scissors beats rock")
                break
        else:
            print("Tie! Shoot again.")
            break

'''
# rules
rock beats scissors
scissors beats paper
paper beats rock
x ties x

get input from user_a_input
get input from user_b_input

create set of potential plays
check is inputs are in set
    if input in set
        pass
    else:
        print "not in set"
        break

check what user_a_input has
    if user_a_input has paper:
        check what b has:
            # if b same answer
            #     ties
            elif b has thing that beats paper
                paper loses
            else:
                paper wins
    if user_a_input has rock:
        check what b has:
            if b same answer
                ties
            elif b has thing that beats rock
                rock loses
            else:
                rock wins
    if user_a_input has scissors:
        check what b has :
            if b same answer
                ties
            elif b has thing that beats scissors
                scissors loses
            else:
                scissors wins



create dict with key and losing value
function user_a_input = key
        user_b_input = value

'''
