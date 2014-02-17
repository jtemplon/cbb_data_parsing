from multiseasonsim import multiseasonsim
from simutil import set_up_team_objects, find_offense_defense, find_conf_records

teamlist = ["Robert Morris", "Bryant", "Wagner", "St. Francis NY", "Mount St. Mary's", 
            "St. Francis PA", "Fairleigh Dickinson", "Central Connecticut", 
            "LIU Brooklyn", "Sacred Heart"]

team_dict = set_up_team_objects(teamlist)
team_stats = find_offense_defense(team_dict)
team_records = find_conf_records(team_dict, "nec.csv")
for k in team_records.keys():
  print team_records[k].name, team_records[k].offense, team_records[k].defense,
  print team_records[k].starting_wins, team_records[k].starting_losses

team_stats["Robert Morris"].home_opponents = ["LIU Brooklyn", "St. Francis NY"]
team_stats["LIU Brooklyn"].home_opponents = ["Central Connecticut", "Bryant"]
team_stats["Central Connecticut"].home_opponents = ["Mount St. Mary's"]
team_stats["St. Francis PA"].home_opponents = ["St. Francis NY", "LIU Brooklyn"]
team_stats["Wagner"].home_opponents = ["Sacred Heart", "Mount St. Mary's", "St. Francis PA", "Robert Morris"]
team_stats["Sacred Heart"].home_opponents = ["LIU Brooklyn", "Central Connecticut"]
team_stats["St. Francis NY"].home_opponents = ["Central Connecticut", "Bryant", "Fairleigh Dickinson"]
team_stats["Mount St. Mary's"].home_opponents = ["Sacred Heart", "St. Francis PA"]
team_stats["Fairleigh Dickinson"].home_opponents = ["Wagner", "Sacred Heart", "Robert Morris"]
team_stats["Bryant"].home_opponents = ["Fairleigh Dickinson", "Central Connecticut"]

multiseasonsim(team_records, False)