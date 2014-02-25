from bs4 import BeautifulSoup as bs
import urllib2
"""My future expectations for this program are to be able to
   calculate the offensive and defensive splits for when a
   player is on and off the court. Using the name supplied."""

#This function just takes a file name and turns into into
#BeautifulSoup objects so that we can do parsing easily
def read_and_soup_html(string):
    print string
    f = urllib2.urlopen(string, "r")
    html = f.read()
    soup = bs(html)
    return soup

#Takes souped up play-by-play and finds all the plays for a team
def find_plays_in_html(soup):
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

#This function identifies if the player passed to the function
#in string started the game by seeing if he is one of first 5 on box score
def find_if_started(player, boxscore):
    #soup the box score page
    soup = read_and_soup_html(boxscore)
    #find the roster tables
    tables = soup.find_all("table", {"class" : "mytable"})
    player_started = False
    for t in tables:
        players = []
        rows = t.find_all("tr")
        for r in rows:
            #ignore the rows that are fluff
            try:
                cl = r["class"]
            except KeyError:
                cl = None
            if cl not in ["heading", "grey_heading"]:
                #take first cell in non-fluff rows and find name
                try:
                    p = r.td.a.string
                except:
                    p = None
                #print p
                #actually figure out if they started or not
                if p == player._name and len(players) < 5:
                    player_started = True
                elif p != None:
                    #print p
                    players.append(p)
    return player_started

def find_if_started_second_half(player, plays, started_game):
    started = False
    starters = []
    subbed_in = []
    for p in plays:
        if p["team"] != "":
            if "Enters Game" in p["team"]:
                name = p["team"].split()[0]
                if name not in subbed_in:
                    subbed_in.append(name)
            if "Leaves Game" in p["team"]:
                name = p["team"].split()[0]
                if name not in subbed_in:
                    starters.append(name)
    #print starters
    #if he's in the starters then he obviously started
    if player in starters:
        print "Looks like he started 2nd half"
        started = True
    #if he started the 1st and played the whole thing then
    #maybe the list is short a player
    elif len(starters) < 5 and started_game:
        print "Fewer than five starters and he started"
        started = True
    return started

#Takes a play and a name and figures out if that player is in
#or out of the game. It assumes it's getting a play.
def in_or_out(p, string, in_game):
    if "Enters Game" in p and string in p:
        in_game = True
    elif "Leaves Game" in p and string in p:
        in_game = False
    else:
        pass
    return in_game

#This funtion takes all the plays in the game and generates four
#dictionaries of statistics that represent Offense and Defense
#when the player was in and out of the game
def find_game_splits(player, team, soup, started):
    #this is so dumb, but have to uppercase name for PBP
    #the replace on the end of the string is for first names like E.J.
    name_pieces = player._name.split()
    if len(name_pieces) == 2:
        last = name_pieces[0].upper()
        first = name_pieces[1].upper().replace(".", "")
    elif len(name_pieces) == 3:
        last = name_pieces[0].upper() + " " + name_pieces[1].upper()
        first = name_pieces[2].upper().replace(".", "")
    print last
    if last.endswith("JR,"):
        print "Ends with JR"
        last = last.replace("JR", "JR.")
    pbp_name = last + first
    print pbp_name
    plays = find_plays_in_html(soup)
    in_game = started
    last_time = 1200
    halftimes = 0
    for p in plays:
        #This is an additional check for when there's a change to the lineup at halftime
        #I've also added a check because overtime causes issues
        if p["time"] > last_time and halftimes == 0:
            halftime_index = plays.index(p)
            second_half_plays = plays[halftime_index:]
            in_game = find_if_started_second_half(pbp_name, second_half_plays, started)
            halftimes += 1
        if p["team"] != "":
            if "Enters Game" in p["team"] or "Leaves Game" in p["team"]:
                in_game = in_or_out(p["team"], pbp_name, in_game)
            elif "Turnover" in p["team"]:
                if in_game:
                    player._team_stats_in.to += 1
                else:
                    player._team_stats_out.to += 1
            elif "Offensive Rebound" in p["team"]:
                if in_game:
                    player._team_stats_in.oreb += 1
                else:
                    player._team_stats_out.oreb += 1
            elif "Defensive Rebound" in p["team"]:
                if in_game:
                    player._team_stats_in.dreb += 1
                else:
                    player._team_stats_out.dreb += 1                
            elif "missed" in p["team"]:
                if ("Layup" in p["team"]) or ("Dunk" in p["team"]) or ("Tip In" in p["team"]):
                    if in_game:
                        player._team_stats_in.two_pt_a += 1
                    else:
                        player._team_stats_out.two_pt_a += 1
                elif "Two Point Jumper" in p["team"]:
                    if in_game:
                        player._team_stats_in.two_pt_a += 1
                    else:
                        player._team_stats_out.two_pt_a += 1
                elif "Three Point Jumper" in p["team"]:
                    if in_game:
                        player._team_stats_in.three_pt_a += 1
                    else:
                        player._team_stats_out.three_pt_a += 1
                elif "Free Throw" in p["team"]:
                    if in_game:
                        player._team_stats_in.fta += 1
                    else:
                        player._team_stats_out.fta += 1
            elif "made" in p["team"]:
                if ("Layup" in p["team"]) or ("Dunk" in p["team"]) or ("Tip In" in p["team"]):
                    if in_game:
                        player._team_stats_in.two_pt_a += 1
                        player._team_stats_in.two_pt_m += 1
                    else:
                        player._team_stats_out.two_pt_a += 1
                        player._team_stats_out.two_pt_m += 1
                elif "Two Point Jumper" in p["team"]:
                    if in_game:
                        player._team_stats_in.two_pt_a += 1
                        player._team_stats_in.two_pt_m += 1
                    else:
                        player._team_stats_out.two_pt_a += 1
                        player._team_stats_out.two_pt_m += 1
                elif "Three Point Jumper" in p["team"]:
                    if in_game:
                        player._team_stats_in.three_pt_a += 1
                        player._team_stats_in.three_pt_m += 1
                    else:
                        player._team_stats_out.three_pt_a += 1
                        player._team_stats_out.three_pt_m += 1
                elif "Free Throw" in p["team"]:
                    if in_game:
                        player._team_stats_in.fta += 1
                        player._team_stats_in.ftm += 1
                    else:
                        player._team_stats_out.fta += 1
                        player._team_stats_out.ftm += 1
        if p["opponent"] != "":
            if "Turnover" in p["opponent"]:
                if in_game:
                    player._oppo_stats_in.to += 1
                else:
                    player._oppo_stats_out.to += 1
            elif "Offensive Rebound" in p["opponent"]:
                if in_game:
                    player._oppo_stats_in.oreb += 1
                else:
                    player._oppo_stats_out.oreb += 1
            elif "Defensive Rebound" in p["opponent"]:
                if in_game:
                    player._oppo_stats_in.dreb += 1
                else:
                    player._oppo_stats_out.dreb += 1                
            elif "missed" in p["opponent"]:
                if ("Layup" in p["opponent"]) or ("Dunk" in p["opponent"]) or ("Tip In" in p["opponent"]):
                    if in_game:
                        player._oppo_stats_in.two_pt_a += 1
                    else:
                        player._oppo_stats_out.two_pt_a += 1
                elif "Two Point Jumper" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.two_pt_a += 1
                    else:
                        player._oppo_stats_out.two_pt_a += 1
                elif "Three Point Jumper" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.three_pt_a += 1
                    else:
                        player._oppo_stats_out.three_pt_a += 1
                elif "Free Throw" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.fta += 1
                    else:
                        player._oppo_stats_out.fta += 1
            elif "made" in p["opponent"]:
                if ("Layup" in p["opponent"]) or ("Dunk" in p["opponent"]) or ("Tip In" in p["opponent"]):
                    if in_game:
                        player._oppo_stats_in.two_pt_a += 1
                        player._oppo_stats_in.two_pt_m += 1
                    else:
                        player._oppo_stats_out.two_pt_a += 1
                        player._oppo_stats_out.two_pt_m += 1
                elif "Two Point Jumper" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.two_pt_a += 1
                        player._oppo_stats_in.two_pt_m += 1
                    else:
                        player._oppo_stats_out.two_pt_a += 1
                        player._oppo_stats_out.two_pt_m += 1
                elif "Three Point Jumper" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.three_pt_a += 1
                        player._oppo_stats_in.three_pt_m += 1
                    else:
                        player._oppo_stats_out.three_pt_a += 1
                        player._oppo_stats_out.three_pt_m += 1
                elif "Free Throw" in p["opponent"]:
                    if in_game:
                        player._oppo_stats_in.fta += 1
                        player._oppo_stats_in.ftm += 1
                    else:
                        player._oppo_stats_out.fta += 1
                        player._oppo_stats_out.ftm += 1
        last_time = p["time"]
    return player

class StatsDict(object):
    def __init__(self):
        self.to = 0
        self.two_pt_a = 0
        self.two_pt_m = 0
        self.fta = 0
        self.ftm = 0
        self.three_pt_m = 0
        self.three_pt_a = 0
        self.oreb = 0
        self.dreb = 0
        
    def estimate_possessions(self):
        poss = round(self.fta * 0.475) + self.to - self.oreb + (self.two_pt_a + self.three_pt_a)
        return poss
        
    def calculate_points(self):
        points = self.two_pt_m * 2 + self.three_pt_m * 3 + self.ftm
        return points
    
    def calculate_eff(self):
        try:
            eff = (float(self.calculate_points()) / float(self.estimate_possessions())) * 100
        except ZeroDivisionError:
            eff = 0
        return eff

class Player(object):
    def __init__(self, name):
        self._name = name
        self._team_stats_in = StatsDict()
        self._team_stats_out = StatsDict()
        self._oppo_stats_in = StatsDict()
        self._oppo_stats_out = StatsDict()

game_list = ["2858904",
        "2865173",
        "2890353",
        "2909453",
        "2912020",
        "2920427",
        "2950733",
        "2942194",
        "2967733",
        "2973901",
        "3023114"]
key_player = Player("Sanders Jr, Sidney")
team = "Fairleigh Dickinson"
for g in game_list:
    box_score_link = "http://stats.ncaa.org/game/index/%s" %(g)
    play_by_play_link = "http://stats.ncaa.org/game/play_by_play/%s" %(g)
    s = read_and_soup_html(play_by_play_link)
    started = find_if_started(key_player, box_score_link)
    print "Started:", started
    key_player = find_game_splits(key_player, team, s, started)

print key_player._name, key_player._team_stats_in.calculate_eff(),
print key_player._team_stats_out.calculate_eff(), key_player._oppo_stats_in.calculate_eff(),
print key_player._oppo_stats_out.calculate_eff(), key_player._team_stats_in.estimate_possessions(),
print key_player._team_stats_out.estimate_possessions()
print key_player._oppo_stats_in.__dict__
print key_player._team_stats_out.__dict__
    
    