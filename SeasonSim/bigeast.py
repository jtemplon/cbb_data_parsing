from multiseasonsim import multiseasonsim
from simutil import set_up_team_objects, find_offense_defense, find_conf_records

teamlist = ["Villanova", "Creighton", "Xavier", "Marquette", "Providence", "Georgetown",
            "St. John's", "Seton Hall", "DePaul", "Butler"]

team_dict = set_up_team_objects(teamlist)
team_stats = find_offense_defense(team_dict)
team_records = find_conf_records(team_dict, "bigeaststandings.csv")
for k in team_records.keys():
  print team_records[k].name, team_records[k].offense, team_records[k].defense,
  print team_records[k].starting_wins, team_records[k].starting_losses


team_stats["Villanova"].home_opponents = ["St. John's", "Butler", "Georgetown"]
team_stats["Creighton"].home_opponents = ["Villanova", "Seton Hall", "Providence"]
team_stats["Xavier"].home_opponents = ["DePaul", "Creighton", "Villanova"]
team_stats["Marquette"].home_opponents = ["Xavier", "Creighton", "Georgetown", "St. John's"]
team_stats["Providence"].home_opponents = ["DePaul", "Villanova", "Marquette"]
team_stats["St. John's"].home_opponents = ["Georgetown", "Butler", "Xavier", "DePaul"]
team_stats["Seton Hall"].home_opponents = ["St. John's", "Georgetown", "Providence", "Xavier"]
team_stats["DePaul"].home_opponents = ["Villanova", "Marquette", "Seton Hall"]
team_stats["Butler"].home_opponents = ["Creighton", "Providence", "Seton Hall"]
team_stats["Georgetown"].home_opponents = ["Xavier", "Creighton"]

multiseasonsim(team_records, False)
