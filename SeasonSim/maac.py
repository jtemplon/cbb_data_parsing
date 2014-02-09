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
    last_places = 0
    total_wins = 0

iona = Team()
iona.name = "Iona"
iona.offense = 116.9
iona.defense = 108.7
iona.starting_wins = 10
iona.starting_losses = 2

fairfield = Team()
fairfield.name = "Fairfield"
fairfield.offense = 92.7
fairfield.defense = 102.2
fairfield.starting_wins = 1
fairfield.starting_losses = 11

quinnipiac = Team()
quinnipiac.name = "Quinnipiac"
quinnipiac.offense = 109.5
quinnipiac.defense = 106.2
quinnipiac.starting_wins = 8
quinnipiac.starting_losses = 4

manhattan = Team()
manhattan.name = "Manhattan"
manhattan.offense = 107.0
manhattan.defense = 99.9
manhattan.starting_wins = 8
manhattan.starting_losses = 4

monmouth = Team()
monmouth.name = "Monmouth"
monmouth.offense = 98.6
monmouth.defense = 104.2
monmouth.starting_wins = 4
monmouth.starting_losses = 8

stpeters = Team()
stpeters.name = "St. Peter's"
stpeters.offense = 95.3
stpeters.defense = 103.3
stpeters.starting_wins = 3
stpeters.starting_losses = 9

marist = Team()
marist.name = "Marist"
marist.offense = 97.2
marist.defense = 102.3
marist.starting_wins = 5
marist.starting_losses = 7

siena = Team()
siena.name = "Siena"
siena.offense = 101.1
siena.defense = 103.0
siena.starting_wins = 6
siena.starting_losses = 6

rider = Team()
rider.name = "Rider"
rider.offense = 108.5
rider.defense = 110.3
rider.starting_wins = 8
rider.starting_losses = 4

niagara = Team()
niagara.name = "Niagara"
niagara.offense = 103.1
niagara.defense = 111.4
niagara.starting_wins = 3
niagara.starting_losses = 9

canisius = Team()
canisius.name = "Canisius"
canisius.offense = 112.4
canisius.defense = 106.0
canisius.starting_wins = 10
canisius.starting_losses = 2

teamlist = [iona, fairfield, quinnipiac, monmouth, manhattan, stpeters, marist, siena, rider, niagara, canisius]

iona.home_opponents = [stpeters, monmouth, rider]
fairfield.home_opponents = [monmouth, quinnipiac, rider, marist]
quinnipiac.home_opponents = [rider, marist, stpeters, siena]
monmouth.home_opponents = [marist, manhattan, stpeters, niagara]
manhattan.home_opponents = [niagara, iona, canisius]
stpeters.home_opponents = [siena, monmouth, marist, fairfield, niagara]
marist.home_opponents = [siena, iona, quinnipiac]
siena.home_opponents = [fairfield, canisius, manhattan, monmouth]
rider.home_opponents = [marist, manhattan, fairfield, iona, siena, canisius]
niagara.home_opponents = [iona, manhattan, canisius, fairfield, quinnipiac]
canisius.home_opponents = [manhattan, iona, quinnipiac, fairfield]

multiseasonsim(teamlist, False)
