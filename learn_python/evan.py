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

# create list of chatnames
# loop through chats names,
#     for name in set
#         if in chat nicknames
#             do nothing
#         elif in chat nicknames
#             add to dictionary


chatnames =  set()
ppl_without_names =  dict()

for names in chats.keys():
    chatnames.add(names)

def check_for_nicks(x):
    for x in chats.values():
        if x in chatnicks.keys():
            print("nothing")
        else:
            ppl_without_names[x] = "chats.values()"

for x in chatnames:
    check_for_nicks(x)

print(ppl_without_names)
