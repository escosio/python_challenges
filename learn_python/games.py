# this is list practice

games = ['Call of Duty', 'NBA 2K', 'MLB the Show','Red Dead Redemption']

print(games) #prints them all with games
print("Currently playing " + games[2])  # prints the 3rd item in the list

# loops through games and prints them all once
for x in games:
    print(x)

# checks if list contains value
if "NBA 2K" in games:
    print("This is a list of ps4 games.")

# prints number of games
numOfGames = len(games)  # gets number of games
print(f"This is a list of {numOfGames} games") # prints string and formats in var

# Accepts new game and adds it to the list
newgame = input("Enter a new game to the list:")
games.append(newgame)
print(games)

#then remove it
games.remove(newgame)
print(games)
