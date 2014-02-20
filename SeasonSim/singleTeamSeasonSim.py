from gamesim import gamesim, neutralsim
from simutil import Team
import csv

"""The purpose of this program is to sim a single team through a 
fictional schedule for a large sample of times to figure out the
percentage chance of a certain likelihood of wins and losses."""

#The team you'll be simulating games for
key_team = Team("Kansas")
with open("kenpom.csv", "rb") as csvfile:
  kenpomdata = csv.reader(csvfile)
  #find your key team and populate its offense and defense
  for d in kenpomdata:
    if d[0] == key_team.name:
      key_team.offense = float(d[7])
      key_team.defense = float(d[11])
#The games you'll be simulating, with Team Name and Site
schedule = [("Western Kentucky", "H"), ("William & Mary", "N"), ("Tennessee St.", "H"),
            ("Tulsa", "A"), ("DePaul", "N"), ("BYU", "N"),
            ("Saint Louis", "A"), ("Oral Roberts", "H"), ("Tennessee", "H"), 
            ("Alabama", "A"), ("North Carolina Central", "H"), ("Davidson", "H"),
            ("Southern Illinois", "A"), ("Northern Iowa", "H"), ("Illinois St.", "H"),
            ("Missouri St.", "A"), ("Bradley", "H"), ("Indiana St.", "H"), 
            ("Illinois St.", "A"), ("Drake", "A"), ("Loyola Chicago", "H"), 
            ("Evansville", "H"), ("Indiana St.", "A"), ("Northern Iowa", "A"), 
            ("Southern Illinois", "H"), ("Evansville", "A"), ("Loyola Chicago", "A")]

# schedule = [("Louisiana Monroe", "H"), ("Duke", "N"), ("Iona", "H"),
#             ("Towson", "H"), ("Wake Forest", "N"), ("Villanova", "N"),
#             ("UTEP", "N"), ("Colorado", "A"), ("Florida", "A"), 
#             ("Colorado", "H"), ("New Mexico", "H"), ("Georgetown", "H"),
#             ("Toledo", "H"), ("San Diego St.", "H"), ("Oklahoma", "A"),
#             ("Kansas St.", "H"), ("Iowa St.", "A"), ("Oklahoma St.", "H"), 
#             ("Baylor", "H"), ("TCU", "A"), ("Iowa St.", "H"), ("Texas", "A"),
#             ("Baylor", "A"), ("West Virginia", "H"), ("Kansas St.", "A"), 
#             ("TCU", "H"), ("Texas Tech", "A")]

def populate_schedule_with_teams(schedule):
  sched_with_teams = []
  team_dict = {}
  with open("kenpom.csv", "rb") as csvfile:
    kenpomdata = csv.reader(csvfile)
    kenpomdata.next()
    #make every team in Division I
    for d in kenpomdata:
      team_key = d[0]
      team_dict[team_key] = Team(team_key)
      team_dict[team_key].offense = float(d[7])
      team_dict[team_key].defense = float(d[11])
  print team_dict
  for game in schedule:
    opponent = team_dict[game[0]]
    location = game[1]
    g = (opponent, location)
    sched_with_teams.append(g)
  return sched_with_teams

def simulate_single_team_season(key_team, schedule):
  for game in schedule:
    if game[1] == "N":
      neutralsim(key_team, game[0])
    elif game[1] == "H":
      gamesim(key_team, game[0])
    elif game[1] == "A":
      gamesim(game[0], key_team)
  print key_team.wins, key_team.losses
  return key_team.wins, key_team.losses

def sim_key_team_seasons(key_team, schedule):
  i = 0
  wins_dict = {}
  losses_dict = {}
  popped_sched = populate_schedule_with_teams(schedule)
  while i < 10000:
    wins, losses = simulate_single_team_season(key_team, popped_sched)
    if wins in wins_dict.keys():
      wins_dict[wins] += 1
    else:
      wins_dict[wins] = 1
    if losses in losses_dict.keys():
      losses_dict[losses] += 1
    else:
      losses_dict[losses] = 1
    key_team.wins = 0
    key_team.losses = 0
    i += 1
  return wins_dict, losses_dict

w_results, l_results = sim_key_team_seasons(key_team, schedule)
print l_results
#find expectation:
total_losses = 0
total_seasons = 0
for k in l_results.keys():
  total_losses += int(k)*int(l_results[k])
  total_seasons += int(l_results[k])
print total_losses
print total_seasons
expected_losses = float(total_losses) / float(total_seasons)
print expected_losses

# Wichita St. vs. Kansas schedule: 5.59 losses expected {0: 12, 1: 60, 2: 308, 3: 869, 4: 1586, 5: 2036, 6: 2048, 7: 1557, 8: 913, 9: 404, 10: 151, 11: 45, 12: 11}
# Kansas vs. Kansas schedule: 5.55 losses expected; {0: 4, 1: 79, 2: 380, 3: 882, 4: 1604, 5: 2071, 6: 1964, 7: 1536, 8: 861, 9: 396, 10: 164, 11: 49, 12: 8, 13: 2}
# Wichita St. vs. Wichita St. schedule: 3.13 losses expected
# Kansas vs. Wichita St. schedule: 