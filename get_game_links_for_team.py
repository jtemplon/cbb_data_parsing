from bs4 import BeautifulSoup as bs
import urllib2

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
        #print cells
        if cells[2].a != None:
            l = cells[2].a["href"]
            lid = l.split("?")[0].replace("/game/index/", "")
            try:
                o = cells[1].a.string
            except AttributeError:
                o = cells[1].string
            link_tuple = (lid, o)
            game_links.append(link_tuple)
    return game_links

print "What's the team ID at the end of the NCAA.org URL?"
team_id = input()
link = "http://stats.ncaa.org/team/index/11540?org_id=%s" %(team_id)
game_links = get_game_links(link)
for gl in game_links:
    print gl[0], gl[1]
for gl in game_links:
    print '"' + gl[0] + '"'