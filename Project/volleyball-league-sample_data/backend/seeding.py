import pandas as pd
import json

df = pd.read_csv("../data/standings.csv")
df = df.sort_values(by=["Points", "Wins"], ascending=False).reset_index(drop=True)

qualified = df.head(8)['Team Name'].tolist()
bracket = [
    {"Match": "QF1", "Team A": qualified[0], "Team B": qualified[7]},
    {"Match": "QF2", "Team A": qualified[3], "Team B": qualified[4]},
    {"Match": "QF3", "Team A": qualified[1], "Team B": qualified[6]},
    {"Match": "QF4", "Team A": qualified[2], "Team B": qualified[5]},
]

with open("../data/bracket.json", "w") as f:
    json.dump(bracket, f, indent=2)

print("✅ Bracket generated: bracket.json")
