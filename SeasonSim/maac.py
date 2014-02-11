from multiseasonsim import multiseasonsim
from simutil import set_up_team_objects, find_offense_defense

teamlist = ["Manhattan", "Iona", "Fairfield", "Quinnipiac", "Monmouth", "Saint Peter's", 
            "Marist", "Siena", "Rider", "Niagara", "Canisius"]

team_dict = set_up_team_objects(teamlist)
team_stats = find_offense_defense(team_dict)
for k in team_stats.keys():
  print team_stats[k].name, team_stats[k].offense, team_stats[k].defense

team_stats["Iona"].starting_wins = 12
team_stats["Iona"].starting_losses = 2
team_stats["Fairfield"].starting_wins = 1
team_stats["Fairfield"].starting_losses = 11
team_stats["Quinnipiac"].starting_wins = 8
team_stats["Quinnipiac"].starting_losses = 4
team_stats["Manhattan"].starting_wins = 8
team_stats["Manhattan"].starting_losses = 4
team_stats["Monmouth"].starting_wins = 4
team_stats["Monmouth"].starting_losses = 8
team_stats["Saint Peter's"].starting_wins = 3
team_stats["Saint Peter's"].starting_losses = 9
team_stats["Marist"].starting_wins = 5
team_stats["Marist"].starting_losses = 7
team_stats["Siena"].starting_wins = 6
team_stats["Siena"].starting_losses = 6
team_stats["Rider"].starting_wins = 8
team_stats["Rider"].starting_losses = 4
team_stats["Niagara"].starting_wins = 3
team_stats["Niagara"].starting_losses = 9
team_stats["Canisius"].starting_wins = 10
team_stats["Canisius"].starting_losses = 2

team_stats["Iona"].home_opponents = ["Saint Peter's", "Monmouth", "Rider"]
team_stats["Fairfield"].home_opponents = ["Monmouth", "Quinnipiac", "Rider", "Marist"]
team_stats["Quinnipiac"].home_opponents = ["Rider", "Marist", "Saint Peter's", "Siena"]
team_stats["Monmouth"].home_opponents = ["Marist", "Manhattan", "Saint Peter's", "Niagara"]
team_stats["Manhattan"].home_opponents = ["Niagara", "Iona", "Canisius"]
team_stats["Saint Peter's"].home_opponents = ["Siena", "Monmouth", "Marist", "Fairfield", "Niagara"]
team_stats["Marist"].home_opponents = ["Siena", "Iona", "Quinnipiac"]
team_stats["Siena"].home_opponents = ["Fairfield", "Canisius", "Manhattan", "Monmouth"]
team_stats["Rider"].home_opponents = ["Marist", "Manhattan", "Fairfield", "Iona", "Siena", "Canisius"]
team_stats["Niagara"].home_opponents = ["Iona", "Manhattan", "Canisius", "Fairfield", "Quinnipiac"]
team_stats["Canisius"].home_opponents = ["Manhattan", "Iona", "Quinnipiac", "Fairfield"]

multiseasonsim(team_dict, False)
