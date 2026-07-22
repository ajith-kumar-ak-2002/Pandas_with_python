# Final Project Using NumPy and Pandas (EDA -- Exploratory Data Analysis)
    ## IPL Data Analysis 

import pandas as pd
import numpy as np

ipl_dataset = pd.read_csv('matches.csv')
print(ipl_dataset.head(10))

print(ipl_dataset.shape)
print(ipl_dataset.info())
print("Before Fill Null Values :" , ipl_dataset.isnull().sum())

ipl_dataset['city'] = ipl_dataset['city'].fillna("Unknown")
ipl_dataset['player_of_match'] = ipl_dataset['player_of_match'].fillna("No Award")
ipl_dataset['winner'] = ipl_dataset['winner'].fillna('No Result')
print("After Fill Null Values: ", ipl_dataset.isnull().sum())

drop_data = ipl_dataset.drop(columns=['umpire1', 'umpire2'], errors='ignore')



### Matches for Season
matches_per_season = ipl_dataset['season'].value_counts().sort_index()
print(matches_per_season)

### Most Sucessful Teams
most_sucess_teams = ipl_dataset['winner'].value_counts()
print(most_sucess_teams)

### How Many Matches Ended with No Results 
no_result = (ipl_dataset['winner'] == "No Result").sum()
print("Matches With No Results: ", no_result)

### Toss Decision --- Does winning toss matters?
toss_match = (ipl_dataset['toss_winner'] == ipl_dataset['winner']).sum()
print("Toss And Match Winning Teams:" ,toss_match)

total_matches = ipl_dataset.shape[0]
percenage = round((toss_match / total_matches) * 100)
print("Toss and Match winning team %:",percenage)

###Player of the Match
player_of_match = ipl_dataset['player_of_match'].value_counts().head(10)
print(player_of_match)

###common toss decisions (Bat or Field)
toss_decision = ipl_dataset['toss_decision'].value_counts()
print(toss_decision)


###Which team are most successful as a particular venue? 
venue = "Wankhede Stadium"
venue_wins = ipl_dataset[ipl_dataset['venue'] == venue]['winner'].value_counts()
print(venue_wins)


###Which Mathes ended with the smallest and largest margin?
small_margin = ipl_dataset[ipl_dataset['result'] == 'runs'].sort_values(by='result_margin', ascending=False).head(1)
print(small_margin)

large_margin_wicktes = ipl_dataset[ipl_dataset['result'] == 'wickets'].sort_values(by='result_margin', ascending=False).head(1)
print(large_margin_wicktes)

large_margin = ipl_dataset[ipl_dataset['result'] == 'runs'].sort_values(by='result_margin', ascending=True).head(1)
print(large_margin)

small_margin_wicktes = ipl_dataset[ipl_dataset['result'] == 'wickets'].sort_values(by='result_margin', ascending=True).head(1)
print(small_margin_wicktes)


### How many Matches were Decided by Duckworth-Lewis (D/L)method?
d_l_method = ipl_dataset['method'].notnull().sum()
print(d_l_method)



###Which team won the most finals?
most_final_wins = ipl_dataset[ipl_dataset['match_type'] == 'Final']['winner'].value_counts()
print(most_final_wins)
