# Evan coding challenge

# ok i just made up a coding challenge for you
# lol
# we've got 2 dictionaries

# chats = {'turds odouls':set(['duncan','evan','scott']),'baseball':set(['scott','danjw','duncan']),'realnflfans':set(['scott','evan'])}
# chatnicks = {('duncan','baseball'):'yankeeboy',('duncan','turds odouls'):'poop butt',('evan','realnflfans'):'gopackgo'}

# chats gives a chat name and the set of members
# chatnicks gives a member,chat tuple a nickname

# the challenge! find everyone in chats that doesn't have a nickname. the output should be a dictionary of name to a list of channels that you don't have a nickname in
# so evan:['turds odouls'], scott:['turds odouls','baseball','realnflfans'] ...
# (a set would also make sense instead of a list)

chats = {
        'turds odouls': set(['duncan','evan','scott']),
        'baseball': set(['scott','danjw','duncan']),
        'realnflfans': set(['scott','evan'])
        }
chatnicks = {
        ('duncan','baseball'):'yankeeboy',
        ('duncan','turds odouls'):'poop butt',
        ('evan','realnflfans'):'gopackgo'
        }

'''
1. make set of people with nicknames
'''
# all_people = set()
# for sets in chats.values():
#     for names in sets:
#         all_people.add(names)
#
# people_wo_nicks = set()



'''
2. for each key in chats,
     pick out value for key
     for each item in value
       check if item is in set of people with nicknames
       if (yes) {
            do nothing
       } else {
            if (name is already a key) {
                get value
                add chatname to a value set
            }
            else {
                add name as key and chatnames as a value set
            }

       }s
       print dictionary

'''




# get all people
all_people = set()
for sets in chats.values():
    for names in sets:
        all_people.add(names)
# print("Here are all the potential names in all chats: ")
# print(all_people)

# get list of chats
all_chats = set()

for chatnames in chats:
    all_chats.add(chatnames)

# print("Here are all the chat names: ")
# print(all_chats)

# default_dic = chatnicks.fromkeys(all_chats,all_people)
# for x in all_people:
#     if x in chatnicks.keys()
#         pass
#     else:
#         add to

# check if each key is in chatnicks.fromkeys()
# if so do nothing
# if not, then add to new dict with

for x in chats.values():
    if "duncan" in x:
        print(chats.keys())

# print(test)



# remove people from tuple if they have nicknames

# create dict of all chats and all names in them
# check each tuple to
