user_a = input("Player one enter your move: ")
user_b = input("Now player two, enter your move: ")

plays = ["paper","rock","scissors"]

if user_a in plays:
    pass
else:
    exit



while user_a != user_b:
        if user_a == "paper":
            if user_b == "scissors":
                print("Player two wins, scissors beats paper")
                break
            else:
                print("Player one wins! Paper beats rock")
                break
        elif user_a == "rock":
            if user_b == "paper":
                print("Player two wins, paper beats rock")
                break
            else:
                print("Player one wins! rock beats scissors")
                break
        elif user_a == "scissors":
            if user_b == "paper":
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

get input from user_a
get input from user_b

create set of potential plays
check is inputs are in set
    if input in set
        pass
    else:
        print "not in set"
        break

check what user_a has
    if user_a has paper:
        check what b has:
            # if b same answer
            #     ties
            elif b has thing that beats paper
                paper loses
            else:
                paper wins
    if user_a has rock:
        check what b has:
            if b same answer
                ties
            elif b has thing that beats rock
                rock loses
            else:
                rock wins
    if user_a has scissors:
        check what b has :
            if b same answer
                ties
            elif b has thing that beats scissors
                scissors loses
            else:
                scissors wins



create dict with key and losing value
function user_a = key
        user_b = value

'''
