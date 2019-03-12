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


names_in_chat = chats.values()

for channel_members in chats.values():
    for name in channel_members:
        # schannel_members = {'name' in channel_members}
        set("channel_members")
        print(channel_members)

# print("these are all the people: ")
# print(names_in_chat)
# ppl_with_nicks = (chatnicks.keys())
# print("these are the people with nicknames :")
# print(ppl_with_nicks)
#
# for x in names_in_chat:
#     for x in ppl_with_nicks:
#         continue
#     else:
#         print(x)
