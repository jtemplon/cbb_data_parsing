from gamesim import gamesim    

def seasonsim(teamlist, balanced):
    teamlist = teamlist
    opponentlist = teamlist
    
    if balanced == True:
        for team in teamlist:
            for opponent in opponentlist:
                if team != opponent:
                    result = gamesim(team, opponent)
    else:
        for team in teamlist:
            for opponent in team.home_opponents:
                result = gamesim(team, opponent)

    teamlist = sorted(teamlist, key=lambda team: team.wins, reverse=True)

    # for team in teamlist:
    #     print "%s %s %s" %(team.name, team.wins, team.losses)

    return teamlist

def standingscounter(teamlist, seasonstats):
    bestteam = max(teamlist, key=lambda team: team.wins)
    topteams = filter(lambda team: team.wins == bestteam.wins, teamlist)
    winlessteams = filter(lambda team: team.wins == 0, teamlist)
    undefeated = filter(lambda team: team.losses == 0, teamlist)
    teamlist = sorted(teamlist, key=lambda team: team.wins, reverse=True)
    worstteam = min(teamlist, key=lambda team: team.wins)
    bottomteams = filter(lambda team: team.wins == worstteam.wins, teamlist)
    
    if len(bottomteams) == 1:
        worstteam.last_places = worstteam.last_places + 1
    
    if len(topteams) == 1:
        bestteam.season_wins = bestteam.season_wins + 1
        win_margin = bestteam.wins - teamlist[1].wins
        #print win_margin
        bestteam.win_margin = bestteam.win_margin + win_margin
    else:
        seasonstats.tied_seasons = seasonstats.tied_seasons + 1
        
        if len(topteams) == 2:
            seasonstats.two_team_tie = seasonstats.two_team_tie + 1
        elif len(topteams) == 3:
            seasonstats.three_team_tie = seasonstats.three_team_tie + 1
        else:
            seasonstats.multi_team_tie = seasonstats.multi_team_tie + 1
            print "%s teams tied" %(len(topteams))
        
        for team in topteams:
            team.season_wins = team.season_wins + 1
            team.season_ties = team.season_ties + 1
    
    if bestteam.wins in seasonstats.most_wins.keys():
        seasonstats.most_wins[bestteam.wins] += 1
    else:
        seasonstats.most_wins[bestteam.wins] = 1
    
    if len(winlessteams) > 0:
        for team in winlessteams:
            team.winless_seasons = team.winless_seasons + 1
    
    if len(undefeated) > 0:
        for team in undefeated:
            team.undefeated_seasons = team.undefeated_seasons + 1

    for team in teamlist:
        pl = teamlist.index(team) + 1
        if pl in team.places.keys():
            team.places[pl] += 1
        else:
            print "new key"
            team.places[pl] = 1
    
    for team in teamlist:
        if team.wins > team.best_season:
            team.best_season = team.wins
        if team.wins < team.worst_season:
            team.worst_season = team.wins
        team.total_wins = team.total_wins + team.wins
        tw = team.wins
        if tw in team.win_distribution.keys():
            team.win_distribution[tw] += 1
        else:
            team.win_distribution[tw] = 1

def seasonreset(teamlist):
    for team in teamlist:
        team.wins = team.starting_wins
        team.losses = team.starting_losses