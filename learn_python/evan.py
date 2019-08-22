# Evan coding challenge

# ok i just made up a coding challenge for you
# lol
# we've got 2 dictionaries
#
# chats = {'turds odouls':set(['duncan','evan','scott']),'baseball':set(['scott','danjw','duncan']),'realnflfans':set(['scott','evan'])}
# chatnicks = {('duncan','baseball'):'yankeeboy',('duncan','turds odouls'):'poop butt',('evan','realnflfans'):'gopackgo'}
#
# chats gives a chat name and the set of members
# chatnicks gives a member,chat tuple a nickname
#
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

# 1. make set of people with nicknames
ppl_with_nicks = set()

for person in chatnicks.keys():   # loops the chat nicknames set and gets the keys
    ppl_with_nicks.add(person[0])    #  adds only the first item of the key to ppl_with_nicks

# print(ppl_with_nicks)

# 2. for each key in chats,
for chat_titles in chats.keys():
    # pick out value for key
    for names in chats.values():
        print(chat_titles, names)
        # if names in ppl_with_nicks:
        #     pass
        # else:
            # print(names)


# chatnames =  set()
# ppl_without_names =  dict()
# names_in_chat = set()
# ppl_with_nicks = set()      # creates empty set





#
# for names in chats.keys():
#     chatnames.add(names)
#     names_in_chat= set()    # creates empty set
#
# for channel_members in chats.values():  #loops chats and returns the values as channel_members
#     for name in channel_members:
#         names_in_chat.add(name)  # loops chats values and adds them to names_in_chat


# print(ppl_without_names)
