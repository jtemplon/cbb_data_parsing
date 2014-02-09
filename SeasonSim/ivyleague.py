from multiseasonsim import multiseasonsim

class Team():
    wins = 0
    losses = 0
    season_wins = 0
    season_ties = 0
    winless_seasons = 0
    undefeated_seasons = 0
    best_season = 0
    worst_season = 100
    win_margin = 0
    total_wins = 0
    last_places = 0

harvard = Team()
harvard.name = "Harvard"
harvard.offense = 108.5
harvard.defense = 97.0
harvard.starting_wins = 0
harvard.starting_losses = 0

princeton = Team()
princeton.name = "Princeton"
princeton.offense = 102.3
princeton.defense = 99.1
princeton.starting_wins = 0
princeton.starting_losses = 0

yale = Team()
yale.name = "Yale"
yale.offense = 99.6
yale.defense = 102.3
yale.starting_wins = 0
yale.starting_losses = 0

columbia = Team()
columbia.name = "Columbia"
columbia.offense = 98.0
columbia.defense = 101.8
columbia.starting_wins = 0
columbia.starting_losses = 0

penn = Team()
penn.name = "Pennsylvania"
penn.offense = 97.1
penn.defense = 102.4
penn.starting_wins = 0
penn.starting_losses = 0

cornell = Team()
cornell.name = "Cornell"
cornell.offense = 98.8
cornell.defense = 104.7
cornell.starting_wins = 0
cornell.starting_losses = 0

dartmouth = Team()
dartmouth.name = "Dartmouth"
dartmouth.offense = 96.6
dartmouth.defense = 102.9
dartmouth.starting_wins = 0
dartmouth.starting_losses = 0

brown = Team()
brown.name = "Brown"
brown.offense = 98.1
brown.defense = 101.9
brown.starting_wins = 0
brown.starting_losses = 0

teamlist = [harvard, princeton, yale, columbia, penn, cornell, dartmouth, brown]


multiseasonsim(teamlist, True)