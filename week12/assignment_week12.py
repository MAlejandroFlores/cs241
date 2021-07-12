import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place

players = pd.read_csv("nba_basketball_data/basketball_players.csv")
master = pd.read_csv("nba_basketball_data/basketball_master.csv")
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")


# players.columns = Index(['playerID', 'year', 'stint', 'tmID', 'lgID', 'GP', 'GS', 'minutes',
#        'points', 'oRebounds', 'dRebounds', 'rebounds', 'assists', 'steals',
#        'blocks', 'turnovers', 'PF', 'fgAttempted', 'fgMade', 'ftAttempted',
#        'ftMade', 'threeAttempted', 'threeMade', 'PostGP', 'PostGS',
#        'PostMinutes', 'PostPoints', 'PostoRebounds', 'PostdRebounds',
#        'PostRebounds', 'PostAssists', 'PostSteals', 'PostBlocks',
#        'PostTurnovers', 'PostPF', 'PostfgAttempted', 'PostfgMade',
#        'PostftAttempted', 'PostftMade', 'PostthreeAttempted', 'PostthreeMade',
#        'note'],
#       dtype='object')


min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

# print("Rebounds per season: Min: {}, Max: {}, Mean: {:.2f}, Median: {}".format(min, max, mean, median))

# print(players.sort_values("rebounds", ascending=False).head(10))

# print(players[["playerID", "year", "tmID", "rebounds"]].sort_values("rebounds", ascending=False).head(10))

# print(nba[["useFirst", "lastName", "year", "tmID", "rebounds"]].sort_values("rebounds", ascending=False).head(10))

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
nba = nba[nba.GP > 0]

print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

# nba.boxplot(column=["rebounds"])
sns.boxplot(data=nba.reboundsPerGame)
plt.show()
plt.savefig("boxplot_reboundsPerGame.png")


# sns.boxplot(data=nba[["rebounds", "oRebounds", "dRebounds"]])
# plt.show()




