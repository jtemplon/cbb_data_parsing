from multiseasonsim import multiseasonsim

class Team():
    def __init__(self):
        self.win_distribution = {}
        self.places = {}
        self.wins = 0
        self.losses = 0
        self.season_wins = 0
        self.season_ties = 0
        self.winless_seasons = 0
        self.undefeated_seasons = 0
        self.best_season = 0
        self.worst_season = 100
        self.win_margin = 0
        self.last_places = 0
        self.total_wins = 0

rmu = Team()
rmu.name = "Robert Morris"
rmu.offense = 108.2
rmu.defense = 106.3
rmu.starting_wins = 9
rmu.starting_losses = 1

liu = Team()
liu.name = "LIU Brooklyn"
liu.offense = 103.1
liu.defense = 118.2
liu.starting_wins = 2
liu.starting_losses = 8

ccsu = Team()
ccsu.name = "Central Connecticut State"
ccsu.offense = 97.7
ccsu.defense = 111.9
ccsu.starting_wins = 3
ccsu.starting_losses = 7

sfu = Team()
sfu.name = "Saint Francis U"
sfu.offense = 95.5
sfu.defense = 108.9
sfu.starting_wins = 5
sfu.starting_losses = 5

wag = Team()
wag.name = "Wagner"
wag.offense = 97.1
wag.defense = 100.5
wag.starting_wins = 6
wag.starting_losses = 4

shu = Team()
shu.name = "Sacred Heart"
shu.offense = 100.9
shu.defense = 113.4
shu.starting_wins = 1
shu.starting_losses = 9

sfc = Team()
sfc.name = "St. Francis (NY)"
sfc.offense = 97.8
sfc.defense = 102.2
sfc.starting_wins = 6
sfc.starting_losses = 4

msm = Team()
msm.name = "Mount St. Mary's"
msm.offense = 106.3
msm.defense = 111.9
msm.starting_wins = 6
msm.starting_losses = 4

fdu = Team()
fdu.name = "Fairleigh Dickinson"
fdu.offense = 104.7
fdu.defense = 114.6
fdu.starting_wins = 4
fdu.starting_losses = 6

bryant = Team()
bryant.name = "Bryant"
bryant.offense = 108.5
bryant.defense = 107.4
bryant.starting_wins = 8
bryant.starting_losses = 2

teamlist = [rmu, liu, ccsu, sfu, wag, shu, sfc, msm, fdu, bryant]

rmu.home_opponents = [msm, liu, sfc]
liu.home_opponents = [sfc, ccsu, bryant]
ccsu.home_opponents = [shu, msm]
sfu.home_opponents = [rmu, sfc, liu]
wag.home_opponents = [bryant, shu, msm, sfu, rmu]
shu.home_opponents = [liu, ccsu]
sfc.home_opponents = [ccsu, bryant, fdu]
msm.home_opponents = [bryant, shu, sfu]
fdu.home_opponents = [wag, sfu, shu, rmu]
bryant.home_opponents = [fdu, ccsu]

multiseasonsim(teamlist, False)