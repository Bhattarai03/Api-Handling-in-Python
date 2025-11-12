import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import textwrap


data=pd.read_csv("IPL.csv")
print(data)
print(data.info())
print(data.shape)
print(data.isnull().sum())
# For knowing the highest match winning team in the ipl 2022
match_winner=data["match_winner"].value_counts()
print(match_winner)
sns.barplot(y=match_winner.index,x=match_winner.values,palette="viridis")
plt.title("Most Matches Won By Team")
plt.show()

# Toss Decision
sns.countplot(x=data["toss_decision"],palette=("viridis"))
plt.title("Toss Decision Trends")
plt.show()

# Toss Winner and Match Winner
toss_match_winner=data[data["match_winner"]==data["toss_winner"]]["match_id"].count()
toss_match_losser=data[data["match_winner"]!=data["toss_winner"]]["match_id"].count()
print(toss_match_winner)
print(toss_match_losser)
plt.pie(x=[toss_match_winner,toss_match_losser],labels=["toss_winner_match_winner","toss_winner_match_losser"],explode=(0.05,0),autopct="%1.1f%%")
plt.title("Toss and Match Analysis")
plt.show()

# Maximum team won by run or wickets
Won_by=data["won_by"].value_counts()
print(Won_by)
sns.countplot(x=data["won_by"],palette=("viridis"))
plt.show()


# Most Player  of the match
motm=data["player_of_the_match"].value_counts().head(10)
print(motm)
plt.figure(figsize=(10,8))
sns.barplot(y=motm.index,x=motm.values,palette="mako")
plt.title("Top 10 Player With Most MOTM Awards")
plt.show()

# Top 5 Most Run Scorer in the match
top_scorer=data.groupby('top_scorer')["highscore"].sum().sort_values(ascending=False).head(5)

print(top_scorer)
plt.figure(figsize=(13,8))
sns.barplot(x=top_scorer.values,y=top_scorer.index,palette="viridis")

plt.title("Top 5 Most Run scorer in the match")
plt.show()

# Top 10 Bowling figure
data['highwick']=data["best_bowling_figure"].apply(lambda x : x.split("--")[0])
data["highwick"]=data["highwick"].astype(int)
plt.figure(figsize=(10,10))
top_bowl=data.groupby("best_bowling")["highwick"].max().sort_values(ascending=False).head(10)
sns.barplot(y=top_bowl.index,x=top_bowl.values,palette="mako")
plt.title("Top 10 Best Bowling Analysis")
plt.show()


# Most matches played by venue
venue_count=data["venue"].value_counts()
print(venue_count)
plt.figure(figsize=(10,6))
wrapped_text=[textwrap.fill(label,12) for label in venue_count.index]
sns.barplot(x=venue_count.values,y=wrapped_text,palette="rainbow")
plt.yticks(fontsize=10)
plt.tight_layout
plt.title("Most matches played by venue")
plt.show()

# Highest Margin by Runs
highmar=data[data["won_by"]=="Runs"].sort_values(by="margin",ascending=False,ignore_index=True).head(5)[["match_winner","margin"]]

print(highmar)
sns.barplot(x="match_winner",y="margin",data=highmar,palette="viridis")
plt.title("Highest Margin by Runs")
plt.show()

# Highest individual score
highind=data.groupby("top_scorer")["highscore"].max().sort_values(ascending=False).head(5)
print(highind)
plt.figure(figsize=(9,4))
wrappedtext1=[textwrap.fill(label,7) for label in highind.index]
sns.barplot(x=highind.values,y=wrappedtext1,palette="mako")
plt.xlabel("Individual Runs")
plt.ylabel("Batmens")
plt.title("Highest individual score")
plt.show()

# Highest wicket taker in the match
best_bowler=data.groupby("best_bowling")["highwick"].max().sort_values(ascending=False).head(5)
plt.figure(figsize=(9,4))
wrappedtext2=[textwrap.fill(label,10) for label in  best_bowler.index]
sns.barplot(x=best_bowler.values,y=wrappedtext2,palette="viridis")
plt.title("Highest wicket taker in the match ")
plt.xlabel("wickets")
plt.ylabel("Bowler")
plt.show()
