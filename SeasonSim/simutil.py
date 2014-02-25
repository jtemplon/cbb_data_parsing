import csv

class Team():
    def __init__(self, name):
        self.win_distribution = {}
        self.places = {}
        self.place_ties = {}
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
        self.name = name

def set_up_team_objects(teamlist):
  team_d = {}
  for x in teamlist:
      team_d[x] = Team(x)
  return team_d

def find_offense_defense(team_dict):
  csvfile = open('kenpom.csv', 'rb')
  kenpomdata = csv.reader(csvfile)
  for row in kenpomdata:
    if row[0] in team_dict.keys():
      team_key = row[0]
      team_dict[team_key].offense = float(row[7])
      team_dict[team_key].defense = float(row[11])
  return team_dict

def find_conf_records(team_dict, file_name):
  csvfile = open(file_name, 'rb')
  records = csv.reader(csvfile)
  for row in records:
    if row[1] in team_dict.keys():
      team_key = row[1]
      team_dict[team_key].starting_wins = int(row[2])
      team_dict[team_key].starting_losses = int(row[3])
  return team_dict