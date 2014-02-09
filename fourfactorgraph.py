import numpy as np
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import urllib2

key_team = "Marquette"
other_team = "Cal St. Fullerton"
#path = "BigAppleBuckets/LIUPBP2013/LIUMBB01.xml"
path = "http://stats.ncaa.org/game/play_by_play/2789233"
use_xml = False
#this code opens the game and finds all the play nodes
def get_plays_from_xml(p):
    f = open(p)
    xml = f.read()
    game = bs(xml, "xml")
    all_plays = game.find_all("play")
    return all_plays

def get_plays_from_html(p):
    f = urllib2.urlopen(p)
    html = f.read()
    game = bs(html)
    tables = game.find_all("table", { "class": "mytable"})
    #find the two tables that have plays for each half
    first_half = tables[1]
    second_half = tables[2]
    #get plays from those halves
    first_half_plays, first_half_times = get_plays_from_table(first_half, key_team, 1)
    second_half_plays, second_half_times = get_plays_from_table(second_half, key_team, 2)
    plays = first_half_plays + second_half_plays
    times = first_half_times + second_half_times
    print len(times)
    print len(plays)
    return plays, times

def get_plays_from_table(table, team, half):
    rows = table.find_all("tr")
    half_plays = []
    half_times = []
    header_cells = rows[0].find_all("td")
    if header_cells[1].string == team:
        index = 1
    else:
        index = 3
    for row in rows[1:-1]:
        cells = row.find_all("td")
        p = cells[index].string
        t = cells[0].string.strip()
        #print t
        if p == None:
            pass
        else:
            half_plays.append(p)
            #find how many seconds INTO the game we are, so graph looks right
            ts = t.split(":")
            if half == 1:
                seconds_in = 2400 - (int(ts[0])*60+int(ts[1]) + 1200)
            else:
                seconds_in = 2400 - (int(ts[0])*60+int(ts[1]))
                #print sec
            half_times.append(seconds_in)
    return half_plays, half_times

#these are the data points we want to grab
def parse_html_plays(plays, times):
    made_twos = 0
    made_threes = 0
    missed_twos = 0
    missed_threes = 0
    fta = 0
    ftm = 0
    play_count = []
    efg = []
    ftr = []
    pc = 0
    i = 0
    play_times = []
    for play in plays:
        if "Enters Game" in play or "Leaves Game" in play:
            pass
        else:
            pc += 1
            if "made" in play and ("Two Point Jumper" in play or "Dunk" in play or "Tip In" in play or "Layup" in play):
                made_twos += 1
            elif "missed" in play and ("Two Point Jumper" in play or "Dunk" in play or "Tip In" in play or "Layup" in play):
                missed_twos += 1
            elif "made" in play and "Three Point Jumper" in play:
                made_threes += 1
            elif "missed" in play and "Three Point Jumper" in play:
                missed_threes += 1
            elif "missed" in play and "Free Throw" in play:
                fta += 1
            elif "made" in play and "Free Throw" in play:
                fta += 1
                ftm += 1
            fga = made_twos + missed_twos + made_threes + missed_threes
            try:
                p_ftr = float(fta) / float(fga) * 100
            except ZeroDivisionError:
                p_ftr = 100
            try:
                p_efg = (float(made_twos + made_threes) + 0.5*float(made_threes)) / float(fga) * 100
            except ZeroDivisionError:
                p_efg = 0
            #print index
            efg.append(p_efg)
            ftr.append(p_ftr)
            play_count.append(pc)
            play_times.append(times[i])
        i += 1
    print fga, made_twos, missed_twos, made_threes, missed_threes, fta, ftm
    return efg, ftr, play_count, play_times

#construct data points using the time on play list
def parse_xml_plays(plays):
    made_twos = 0
    made_threes = 0
    missed_twos = 0
    missed_threes = 0
    fta = 0
    ftm = 0
    play_count = []
    efg = []
    ftr = []
    pc = 0
    for play in plays:
        #print play["action"]
        if play["team"] == key_team:
            #collect stats
            #pt = play["time"]
            pc += 1
            if play["action"] == "GOOD" and play["type"] in ["JUMPER", "LAYUP", "DUNK"]:
                made_twos += 1
            elif play["action"] == "MISS" and play["type"] in ["JUMPER", "LAYUP", "DUNK"]:
                missed_twos += 1
            elif play["action"] == "GOOD" and play["type"] == "3PTR":
                made_threes += 1
            elif play["action"] == "MISS" and play["type"] == "3PTR":
                missed_threes += 1
            elif play["action"] == "GOOD" and play["type"] == "FT":
                fta += 1
                ftm += 1
            elif play["action"] == "MISS" and play["type"] == "FT":
                fta += 1
            #calculate factors
            fga = made_twos + missed_twos + made_threes + missed_threes
            try:
                p_ftr = float(fta) / float(fga) * 100
            except ZeroDivisionError:
                p_ftr = 100
            try:
                p_efg = (float(made_twos + made_threes) + 0.5*float(made_threes)) / float(fga) * 100
            except ZeroDivisionError:
                p_efg = 0
            #time.append(pt)
            efg.append(p_efg)
            ftr.append(p_ftr)
            play_count.append(pc)
    print fga, made_twos, missed_twos, made_threes, missed_threes, fta, ftm
    return efg, ftr, play_count
# print len(time)
# print len(efg)
# print len(ftr)
# print p_efg
# print fga, made_twos, missed_twos, made_threes, missed_threes
if use_xml:
    plays = get_plays_from_xml(path)
    efg, ftr, play_count = parse_xml_plays(plays)
else:
    plays, times = get_plays_from_html(path)
    efg, ftr, play_count, play_times = parse_html_plays(plays, times)

#print len(efg)
#print len(play_times)
#print play_times
#print efg
#print ftr
x = np.fromiter(times, np.int)
y1 = np.fromiter(efg, np.float)
y2 = np.fromiter(ftr, np.float) 

plt.figure(1)
plt.subplot(211)
plt.plot(play_times, efg)
plt.axhline(y=efg[-1], color='r')
plt.title("%s eFG and FTR by Time vs. %s" %(key_team, other_team), fontsize=16, fontweight='bold')

plt.subplot(212)
plt.plot(play_times, ftr)
plt.axhline(y=ftr[-1], color='r')

plt.show()