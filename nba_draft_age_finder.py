import datetime
import urllib2
from BeautifulSoup import BeautifulSoup as bs

"""A program for finding the draft age of a bunch of NBA basketball players"""

years = ["2004", "2003", "2002", "2001", "2000"]
draft_dates = {"2013":"2013-06-27", "2012":"2012-06-28", "2011":"2011-06-23", "2010": "2010-06-24", "2009": "2009-06-25",
               "2008":"2008-06-26", "2007":"2007-06-28", "2006":"2006-06-28", "2005": "2005-06-28", "2004": "2004-06-24",
               "2003":"2003-06-26", "2002":"2002-06-26", "2001":"2001-06-27", "2000": "2000-06-28"}
rows = []

def find_born_date(link):
  text = urllib2.urlopen(link).read()
  soup = bs(text)
  birth_date = soup.find(id="necro-birth")
  date = birth_date["data-birth"].strip()
  return date

def convert_to_datetime(string):
  dt = datetime.datetime.strptime(string, "%Y-%m-%d")
  return dt

for y in years:
  url = "http://www.basketball-reference.com/draft/NBA_%s.html" %(y)
  text = urllib2.urlopen(url).read()
  soup = bs(text)
  draft_date = convert_to_datetime(draft_dates[y])
  print draft_date
  draftees_table = soup.find(id="stats")
  draftees_table_rows = draftees_table.findAll("tr")
  for dtr in draftees_table_rows[2:]:
    #print dtr
    try:
      cells = dtr.findAll("td")
      pick = int(cells[0].string)
      name = cells[2]["csk"]
      if cells[2].a != None:
        player_link = "http://www.basketball-reference.com/" + cells[2].a["href"]
        birth_date = convert_to_datetime(find_born_date(player_link))
        draft_age = draft_date - birth_date
        print y, pick, name, draft_age.days
    except IndexError:
      pass