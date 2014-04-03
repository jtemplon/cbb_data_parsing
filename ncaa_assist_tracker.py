from bs4 import BeautifulSoup as bs
import urllib2
"""The purpose of this program is to take a player and a school and find all
of the assists that player had and the players he gave those assists to, plus
the type of play they were for"""

#This function just takes a file name and turns into into
#BeautifulSoup objects so that we can do parsing easily
def read_and_soup_html(string):
    #print string
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
                    times = cells[0].string.split(":")
                    time = int(times[0]*60) + int(times[1])
                play = {"team": tstring, "opponent": ostring, "time": time}
                plays.append(play)
    return plays

def find_types_and_players(plays, key_player):
    shooters = []
    shot_types = []
    shooter = None
    shot_type = None
    found_player = False
    for p in plays:
        if p["team"] != "":
            player = p["team"].split()[0]
            #print player
            if "made" in p["team"]:
                shooter = player
                if ("Layup" in p["team"]) or ("Dunk" in p["team"]) or ("Tip In" in p["team"]):
                    shot_type = "rim"
                elif "Two Point Jumper" in p["team"]:
                    shot_type = "two-point jumper"
                elif "Three Point Jumper" in p["team"]:
                    shot_type = "three-point jumper"
                else:
                    shot_type = None
            elif "Assist" in p["team"] and player == key_player:
                found_player = True
                if shot_type != None and shooter != None:
                    shot_types.append(shot_type)
                    shooters.append(shooter)
                else:
                    print "Got assist with no shot type or shooter"
            else:
                shooter = None
                shot_type = None
    if not found_player:
        print "Didn't find %s in this game" %(key_player)
    return shooters, shot_types

def get_game_links(team_page):
    f = urllib2.urlopen(team_page)
    html = f.read()
    text = bs(html)
    tables = text.find_all("table", { "class": "mytable" })
    game_table = tables[0]
    gt_rows = game_table.find_all("tr")
    game_links = []
    for r in gt_rows[2:]:
        cells = r.find_all("td")
        #covers weird case for tournament names pre 2012-13
        try:
            if cells[2].a != None:
                game_links.append(cells[2].a["href"])
        except IndexError:
            pass
    return game_links

def get_play_by_play_urls(game_links):
    play_by_plays = []
    for gl in game_links:
        game_url = "http://stats.ncaa.org/" + gl
        f = urllib2.urlopen(game_url)
        html = f.read()
        text = bs(html)
        root_list = text.find_all("ul", { "id": "root" })
        items = root_list[0].find_all("li")
        for i in items:
            if i.a != None and i.a.string == "Play by Play":
                p_b_p = i.a["href"]
                play_by_plays.append(p_b_p)
    return play_by_plays

key_player = "BRICKMAN,JASON"
team = "LIU Brooklyn"
team_page = "http://stats.ncaa.org/team/index/11540?org_id=361&sport_year_ctl_id=11540"
game_links = get_game_links(team_page)
play_by_plays = get_play_by_play_urls(game_links)
master_shooters = []
master_types = []
for pbp in play_by_plays:
    path = "http://stats.ncaa.org/" + pbp
    print path
    try:
        s = read_and_soup_html(path)
        plays = find_plays_in_html(s)
        players, shot_types = find_types_and_players(plays, key_player)
        if len(players) != len(shot_types):
            print "Missing something!"
        for p in players:
            master_shooters.append(p)
        for st in shot_types:
            master_types.append(st)
    except:
        print "Failed somewhere in the process on %s" %(path)
print master_shooters
print master_types