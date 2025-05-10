import pandas as pd
import itertools
import datetime

teams = pd.read_csv("../data/teams.csv")
team_names = teams['Team Name'].tolist()
matches = list(itertools.combinations(team_names, 2))

num_courts = 4
slots_per_day = 3
start_date = datetime.date.today()
days_needed = len(matches) // (num_courts * slots_per_day) + 1

schedule = []
match_idx = 0

for d in range(days_needed):
    for s in range(slots_per_day):
        for c in range(num_courts):
            if match_idx >= len(matches):
                break
            team_a, team_b = matches[match_idx]
            match_date = start_date + datetime.timedelta(days=d)
            schedule.append({
                "Date": match_date,
                "Slot": f"Slot {s+1}",
                "Court": f"Court {c+1}",
                "Team A": team_a,
                "Team B": team_b
            })
            match_idx += 1

df_schedule = pd.DataFrame(schedule)
df_schedule.to_csv("../data/match_schedule.csv", index=False)
print("✅ Match schedule generated: match_schedule.csv")
