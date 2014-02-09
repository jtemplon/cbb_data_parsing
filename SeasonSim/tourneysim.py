def round_one(standings):
    if len(standings) > 8:
        if standings%2 == 0:
            teams_needed = (len(standings) - 8) * 2 - 1
        else:
            teams_needed = (len(standings) - 8) * 2
        first_round_teams = []
        reversed_standings = reversed(standings)
        for i <= teams_needed:
            print "Adding %s to first round" %(reversed_standings[0].name)
            first_round_teams.append(reversed_standings[0])
            reversed_standings.pop(reversed_standings[0])
            i = i + 1
    