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


team_stats["Iona"].home_opponents = ["Saint Peter's", "Monmouth", "Rider"]
team_stats["Fairfield"].home_opponents = ["Quinnipiac", "Rider", "Marist"]
team_stats["Quinnipiac"].home_opponents = ["Saint Peter's", "Siena"]
team_stats["Monmouth"].home_opponents = ["Marist", "Manhattan", "Saint Peter's", "Niagara"]
team_stats["Manhattan"].home_opponents = ["Niagara", "Iona", "Canisius"]
team_stats["Saint Peter's"].home_opponents = ["Marist", "Fairfield", "Niagara"]
team_stats["Marist"].home_opponents = ["Siena", "Iona", "Quinnipiac"]
team_stats["Siena"].home_opponents = ["Canisius", "Manhattan", "Monmouth"]
team_stats["Rider"].home_opponents = ["Manhattan", "Fairfield", "Iona", "Siena", "Canisius"]
team_stats["Niagara"].home_opponents = ["Canisius", "Fairfield", "Quinnipiac"]
team_stats["Canisius"].home_opponents = ["Quinnipiac", "Fairfield"]

#multiseasonsim(team_records, False)
