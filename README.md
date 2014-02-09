This is a place for storage of simulation and data aggregation code that I use for Big Apple Buckets. 

FourFactorGraph.py generates graphs of the four factors (effective field goal percentage, offensive rebounding percentage, turnover percentage and free throw rate) during a game by parsing the plays from NCAA.org.

InAndOutEfficiencyHTML.py generates the team efficiency for when a player was on and off the court. This could use a little more work (and definitely some comments about how it works). Basically it parses the box score page to look if the player started. It then parses the game data to figure out when they were subbed in and out. You need to feed it individual game IDs (see bottom of the file).

SeasonSim: Everything necessary to take one of the league files (MAAC, NEC, and Ivy League examples are in the folder) and run simulations using Ken Pomeroy - or any other pythagorean expectation rating system that has offensive and defensive efficiencies. Again, needs a lot more commenting. The NEC version is complete and also does places and win totals by default. (The others will break right now.)
