from seasonsim import seasonsim, standingscounter, seasonreset

class SeasonStats():
    tied_seasons = 0
    two_team_tie = 0
    three_team_tie = 0
    multi_team_tie = 0
    most_wins = {}

def multiseasonsim(team_dict, bool):
    season_counter = 1
    balanced = bool
    seasonstats = SeasonStats()

    #while season_counter < 10001:
    while season_counter < 10001:
        seasonreset(team_dict)
        seasonsim(team_dict, balanced)
        standingscounter(team_dict, seasonstats)
        season_counter = season_counter + 1

    print "Name - Season Wins - Season Ties - Undefeated Seasons - Winless Seasons - Best Season - Worst Season - Total Win Margin"
    for k in team_dict.keys():
        print "%s - %s - %s - %s - %s - %s - %s - %s - %s" %(team_dict[k].name, team_dict[k].season_wins, team_dict[k].season_ties, team_dict[k].undefeated_seasons, team_dict[k].winless_seasons, team_dict[k].best_season, team_dict[k].worst_season, team_dict[k].win_margin, team_dict[k].total_wins)
    
    print "Tie Stats: %s ties, %s two-team, %s three-team, %s more than three" %(seasonstats.tied_seasons, seasonstats.two_team_tie, seasonstats.three_team_tie, seasonstats.multi_team_tie)
    print seasonstats.most_wins
    
    for k in team_dict.keys():
        print team_dict[k].name
        print team_dict[k].places
        print team_dict[k].place_ties
        print team_dict[k].win_distribution
