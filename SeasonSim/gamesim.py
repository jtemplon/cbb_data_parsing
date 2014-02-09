from random import randint

class Game():
    winner = None
    loser = None

def gamesim(team1, team2):
    game = Game()
    
    game.home = team1
    game.away = team2
    home = game.home
    away = game.away
    
    home.adjusted_pomeroy = pow(home.offense*1.014,11)/(pow(home.offense*1.014,11)+pow(home.defense*0.986,11))
    away.adjusted_pomeroy = pow(away.offense*0.986,11)/(pow(away.offense*0.986,11)+pow(away.defense*1.014,11))

    home.win_percentage = 100 * (home.adjusted_pomeroy - home.adjusted_pomeroy * away.adjusted_pomeroy) / (home.adjusted_pomeroy + away.adjusted_pomeroy - 2 * home.adjusted_pomeroy * away.adjusted_pomeroy)
    away.win_percentage = 100 * (away.adjusted_pomeroy - away.adjusted_pomeroy * home.adjusted_pomeroy) / (away.adjusted_pomeroy + home.adjusted_pomeroy - 2 * away.adjusted_pomeroy * home.adjusted_pomeroy)

    #print home.win_percentage
    #print away.win_percentage
    
    test_val = randint(1, 100)
    
    if test_val <= round(home.win_percentage):
        home.wins = home.wins + 1
        away.losses = away.losses + 1
        game.winner = game.home
        game.loser = game.away
    else:
        home.losses = home.losses + 1
        away.wins = away.wins + 1
        game.winner = game.away
        game.loser = game.home
    
    return game

def neutralsim(team1, team2):
    game = Game()
    
    team1.pomeroy = pow(team1.offense,11)/(pow(team1.offense,11)+pow(team1.defense,11))
    team2.pomeroy = pow(team2.offense,11)/(pow(team2.offense,11)+pow(team2.defense,11))
    
    team1.win_percentage = 100 * (team1.pomeroy - team1.pomeroy * team2.pomeroy) / (team1.pomeroy + team2.pomeroy - 2 * team1.pomeroy * team2.pomeroy)
    team2.win_percentage = 100 * (team2.pomeroy - team2.pomeroy * team1.pomeroy) / (team2.pomeroy + team1.pomeroy - 2 * team2.pomeroy * team1.pomeroy)

    test_val = randint(1, 100)
    
    if test_val <= round(team1.win_percentage):
        game.winner = team1
        game.loser = team2
    else:
        game.winner = team2
        game.loser = team1
    
    return game
