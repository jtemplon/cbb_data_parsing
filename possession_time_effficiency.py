from bs4 import BeautifulSoup as bs
import urllib2

#This function just takes a file name and turns into into
#BeautifulSoup objects so that we can do parsing easily
class Possession():
    plays = []
    points = 0
    start_time = 1200
    end_time = 0
    team = None

def read_and_soup_html(string):
    print string
    f = urllib2.urlopen(string, "r")
    html = f.read()
    soup = bs(html)
    return soup

#Takes souped up play-by-play and finds all the plays for a team
def find_plays_in_html(soup, team):
    plays = []
    tables = soup.find_all("table", {"class" : "mytable"})[1:]
    #print len(tables)
    for t in tables:
        rows = t.find_all("tr")
        first_row_cells = rows[0].find_all("td")
        if first_row_cells[1].string == team:
            ti = 1
            oi = 3
        elif first_row_cells[3].string == team:
            ti = 3
            oi = 1
        else:
            print "No team index found!"
        for r in rows[1:]:
            cells = r.find_all("td")
            #print cells
            if len(cells) > ti:
                if cells[ti].string == None:
                    tstring = ""
                else:
                    tstring = cells[ti].string
                if cells[oi].string == None:
                    ostring = ""
                else:
                    ostring = cells[oi].string
                if cells[0].string == None:
                    time = 0
                else:
                    #print cells[0].string
                    times = cells[0].string.split(":")
                    #print times
                    time = int(times[0])*60 + int(times[1])
                play = {"team": tstring, "opponent": ostring, "time": time}
                plays.append(play)
    return plays

def remove_plays(plays):
    key_plays = []
    for p in plays:
        if "Turnover" in p["team"] or "Turnover" in p["opponent"]:
            key_plays.append(p)
        elif "Rebound" in p["team"] or "Rebound" in p["opponent"]:
            key_plays.append(p)
        elif "made" in p["team"] or "made" in p["opponent"]:
            key_plays.append(p)
        elif "missed" in p["team"] or "missed" in p["opponent"]:
            key_plays.append(p)
        else:
            pass
        #print p["time"]
    return key_plays

def check_possession_end(p1, p2):
    #a made shot from the field or a turnover ends a possession easy peasy
    if "Turnover" in p1["team"]:
        poss_end = True
        team = "Team"
    elif "Turnover" in p1["opponent"]:
        poss_end = True
        team = "Opponent"
    elif "Defensive Rebound" in p1["team"]:
        poss_end = True
        team = "Opponent"
    elif "miss" in p1["team"] and "Deadball Rebound" in p2["opponent"]:
        poss_end = True
        team = "Team"
    elif "miss" in p1["opponent"] and "Deadball Rebound" in p2["team"]:
        poss_end = True
        team = "Opponent"
    elif "Defensive Rebound" in p1["opponent"]:
        poss_end = True
        team = "Team"
    elif "Deadball Rebound" in p1["team"] and p2["opponent"] != "":
        poss_end = True
        team = "Team"
    elif "Deadball Rebound" in p1["opponent"] and p2["team"] != "":
        poss_end = True
        team = "Opponent"
    elif "made" in p1["team"] and ("Free Throw" not in p2["team"]):
        poss_end = True
        team = "Team"
    elif "made" in p1["opponent"] and ("Free Throw" not in p2["opponent"]):
        poss_end = True
        team = "Opponent"
    #this covers the end of halves scenarios
    elif p1["time"] < p2["time"]:
        poss_end = True
        if p1["team"] != "":
            team = "Team"
        else:
            team = "Opponent"
    else:
        poss_end = False
        team = None
    return poss_end, team

def split_into_possessions(plays):
    total_play_count = len(plays)
    i = 0
    total_possessions = 0
    possessions = []
    possession = Possession()
    possession.plays = []
    possession.points = 0
    #takes the key_plays and puts them into possessions!
    while i < total_play_count:
        #this is a stupid try/except block to get the last possession
        try:
            p1 = plays[i]
            p2 = plays[i+1]
            possession_end, possession.team = check_possession_end(p1, p2)
        except IndexError:
            p1 = plays[i]
            possession_end = True
            if p1["team"] != "":
                possession.team = "Team"
            else:
                possession.team = "Opponent"
        if possession_end:
            total_possessions += 1
            possession.plays.append(p1)
            possession.end_time = p1["time"]
            if possession.end_time > possession.start_time:
                print "Possession End Less Than Possession Start"
                possession.start_time = 1200
            possession.points = find_points_in_possession(possession.plays)
            possessions.append(possession)
            possession = Possession()
            possession.start_time = p1["time"]
            possession.plays = []
            possession.points = 0
        else:
            possession.plays.append(p1)
        i += 1
    return possessions

def find_points_in_possession(plays):
    points = 0
    for p in plays:
        if "made" in p["team"]:
            if "Free Throw" in p["team"]:
                points += 1
            elif "Three Point Jumper" in p["team"]:
                points += 3
            else:
                #print p["team"]
                points += 2
        elif "made" in p["opponent"]:
            if "Free Throw" in p["opponent"]:
                points += 1
            elif "Three Point Jumper" in p["opponent"]:
                points += 3
            else:
                #print p["opponent"]
                points += 2
        else:
            pass
    return points

game_list = ["2688213",
    "2709017",
    "2718555",
    "2768134",
    "2786279",
    "2803558",
    "2811008",
    "2816273",
    "2820657",
    "2832980",
    "2836513",
    "2838133",
    "2841315",
    "2857413",
    "2869063",
    "2885953",
    "2898133",
    "2908096",
    "2924294",
    "2932473",
    "2943553",
    "2978913",
    "3003137",
    "3026165",
    "3084716",
    "3114241",
    "3117283",
    "3147363",
    "3161295",
    "3194923",
    "3199747"]
team = "Fordham"
time_buckets = {"0-7": {"points": 0, "possessions": 0},
                "8-14": {"points": 0, "possessions": 0},
                "15-21": {"points": 0, "possessions": 0},
                "22-28": {"points": 0, "possessions": 0},
                "29-35": {"points": 0, "possessions": 0},
                "35+": {"points": 0, "possessions": 0}}
opp_points = 0
for g in game_list:
    team_game_points = 0
    opp_game_points = 0
    play_by_play_link = "http://stats.ncaa.org/game/play_by_play/%s" %(g)
    s = read_and_soup_html(play_by_play_link)
    plays = find_plays_in_html(s, team)
    key_plays = remove_plays(plays)
    possessions = split_into_possessions(key_plays)
    for poss in possessions:
        if poss.team == "Team":
            #print poss.plays
            total_time = poss.start_time - poss.end_time
            if total_time <= 7:
                time_buckets["0-7"]["points"] += poss.points
                time_buckets["0-7"]["possessions"] += 1
            elif 8 <= total_time <= 14:
                time_buckets["8-14"]["points"] += poss.points
                time_buckets["8-14"]["possessions"] += 1
            elif 15 <= total_time <= 21:
                time_buckets["15-21"]["points"] += poss.points
                time_buckets["15-21"]["possessions"] += 1
            elif 22 <= total_time <= 28:
                time_buckets["22-28"]["points"] += poss.points
                time_buckets["22-28"]["possessions"] += 1
            elif 29 <= total_time <= 35:
                time_buckets["29-35"]["points"] += poss.points
                time_buckets["29-35"]["possessions"] += 1
            else:
                time_buckets["35+"]["points"] += poss.points
                time_buckets["35+"]["possessions"] += 1    
            team_game_points += poss.points
        else:
            #print poss.plays
            opp_points += poss.points
            opp_game_points += poss.points
    print team_game_points, opp_game_points
print time_buckets
total_points = 0
for tb in time_buckets.keys():
    total_points += time_buckets[tb]["points"]
print total_points
print opp_points