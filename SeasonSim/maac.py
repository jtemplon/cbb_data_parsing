from multiseasonsim import multiseasonsim
from simutil import set_up_team_objects, find_offense_defense, find_conf_records

teamlist = ["Manhattan", "Iona", "Fairfield", "Quinnipiac", "Monmouth", "Saint Peter's", 
            "Marist", "Siena", "Rider", "Niagara", "Canisius"]

team_dict = set_up_team_objects(teamlist)
team_stats = find_offense_defense(team_dict)
team_records = find_conf_records(team_dict, "maac.csv")
for k in team_records.keys():
  print team_records[k].name, team_records[k].offense, team_records[k].defense,
  print team_records[k].starting_wins, team_records[k].starting_losses


team_stats["Iona"].home_opponents = ["Rider"]
team_stats["Fairfield"].home_opponents = ["Marist"]
team_stats["Quinnipiac"].home_opponents = ["Siena"]
team_stats["Monmouth"].home_opponents = ["Niagara"]
team_stats["Manhattan"].home_opponents = ["Iona", "Canisius"]
team_stats["Saint Peter's"].home_opponents = ["Fairfield", "Niagara"]
team_stats["Marist"].home_opponents = ["Quinnipiac"]
team_stats["Siena"].home_opponents = ["Monmouth"]
team_stats["Rider"].home_opponents = ["Canisius"]
team_stats["Niagara"].home_opponents = []
team_stats["Canisius"].home_opponents = []
team_stats["Siena"].tie_breaker = ["Rider"]

multiseasonsim(team_records, False)
