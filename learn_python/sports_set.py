#sets
# unordered and unindexed

sports = {"baseball","basketball", "football"}
print(sports)

for x in sports:
    print(x)

# Adds to the set
sports.add("soccer")
print(sports)

numOfSports = len(sports)
print(f"There are {numOfSports} that I care about.")

# sports.remove("soccer")
sports.discard("soccer") # removes it
numOfSports = len(sports) # needed this step to update
print(f"Actually there are just {numOfSports}.")


del sports
