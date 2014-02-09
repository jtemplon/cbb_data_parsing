from seasonsim import seasonsim, standingscounter, seasonreset

class SeasonStats():
    tied_seasons = 0
    two_team_tie = 0
    three_team_tie = 0
    multi_team_tie = 0
    most_wins = {}

def multiseasonsim(teamlist, bool):
    season_counter = 1
    balanced = bool
    seasonstats = SeasonStats()

    #while season_counter < 10001:
    while season_counter < 10001:
        seasonreset(teamlist)
        seasonsim(teamlist, balanced)
        standingscounter(teamlist, seasonstats)
        season_counter = season_counter + 1

    print "Name - Season Wins - Season Ties - Undefeated Seasons - Winless Seasons - Best Season - Worst Season - Total Win Margin"
    teamlist = sorted(teamlist, key=lambda team: team.season_wins, reverse=True)
    for team in teamlist:
        print "%s - %s - %s - %s - %s - %s - %s - %s - %s" %(team.name, team.season_wins, team.season_ties, team.undefeated_seasons, team.winless_seasons, team.best_season, team.worst_season, team.win_margin, team.total_wins)
    
    print "Tie Stats: %s ties, %s two-team, %s three-team, %s more than three" %(seasonstats.tied_seasons, seasonstats.two_team_tie, seasonstats.three_team_tie, seasonstats.multi_team_tie)
    print seasonstats.most_wins
    
    for team in teamlist:
        print team.name
        print team.places, team.win_distribution
    
    # for team in teamlist:
    #     print team.name, team.win_distributions