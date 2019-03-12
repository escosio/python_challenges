
bkNets = {
    "teamName" : "Brooklyn Nets",
    "location" : "Brooklyn",
    "venue" : "Barclays Center",
    "conf" : "Atlantic",
    "ptleader" : "D'Angelo Russell"
}
nyKnicks = {
    "teamName" : "New York Knicks",
    "location" : "New York",
    "venue" : "Madison Square Garden",
    "conf" : "Atlantic",
    "ptleader" : "Dennis Smith Jr."
}
Lakers = {
    "teamName" : "Los Angeles Lakers",
    "location" : "Los Angeles",
    "venue" : "Staples Center",
    "conf" : "Pacific",
    "ptleader" : "Lebron James"
}


def team_info(team):
    print(team['teamName'])
    print(team['venue'] + " in " + team['location'])
    print("Conference: " + team['conf'])
    print("Leading scorer: " + team['ptleader'])

team_info(bkNets)
team_info(nyKnicks)
team_info(Lakers)
