# import the data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


Shots_data = pd.read_csv('Datasets/shots_data.csv')

Shots_data.head()


#add a column with the distance from the hoop

#change X and Y values to absolute values


Shots_data['x'] = abs(Shots_data['x'])
Shots_data['y'] = abs(Shots_data['y'])

Shots_data.head()

Shots_data['Distance'] = ((((Shots_data['x'] - 0)**2) + ((Shots_data['y'] - 0)**2)))** 0.5



# classify the zones

def zones(Shots_data):
    if(Shots_data['x'] >= 22 and Shots_data['y'] <= 7.8):
        return 'C3'
    elif(Shots_data['Distance'] <= 23.75):
        return '2PT'
    elif(Shots_data['Distance'] >= 23.75):
        return 'NC3'
    
Shots_data['shot_zones'] = Shots_data.apply(zones, axis = 1)

Shots_data['shot_zones'].value_counts()


#get the shot distribution by team and zone

#make seperate tables by team

team_a = Shots_data.query("team == 'Team A'")
team_b = Shots_data.query("team == 'Team B'")

for idx, name in enumerate(team_a['shot_zones'].value_counts('percent').index.tolist()):
    print('Team A Shot zone:', team_a['shot_zones'].value_counts('percent').index.tolist()[idx])
    print('Percentage:', team_a['shot_zones'].value_counts('percent')[idx] * 100)
    
for idx, name in enumerate(team_b['shot_zones'].value_counts('percent').index.tolist()):
    print('Team B Shot zone:', team_b['shot_zones'].value_counts('percent').index.tolist()[idx])
    print('Percentage:', team_b['shot_zones'].value_counts('percent')[idx] * 100)


# get the field goal attempts and Field goal made

# Feild goal attempted data

print(team_a['shot_zones'].value_counts())


FGA_team_a = team_a['shot_zones'].value_counts()
FGA_team_b = team_b['shot_zones'].value_counts()

# feild goal made data
# create new tables with onl field goals made

table_team_a_FGM = team_a.query('fgmade == 1')
table_team_b_FGM = team_b.query('fgmade == 1')

FGM_team_a = table_team_a_FGM['shot_zones'].value_counts()
FGM_team_b = table_team_b_FGM['shot_zones'].value_counts()


#calculated effective field goal percentange

# 2 points 
EFG_team_a_2PTS = (FGM_team_a[0]+ (0.5 * (3 * 2))) / FGA_team_a[0]
EFG_team_b_2PTS = (FGM_team_b[0]+ (0.5 * (3 * 2))) / FGA_team_b[0]

# C3

EFG_team_a_C3PTS = (FGM_team_a[2]+ (0.5 * (3 * 3))) / FGA_team_a[2]
EFG_team_b_C3PTS = (FGM_team_b[2]+ (0.5 * (3 * 3))) / FGA_team_b[2]

# NC3

EFG_team_a_NC3PTS = (FGM_team_a[1]+ (0.5 * (3 * 3))) / FGA_team_a[1]
EFG_team_b_NC3PTS = (FGM_team_b[1]+ (0.5 * (3 * 3))) / FGA_team_b[1]



print(EFG_team_b_C3PTS)

print (FGA_team_a)

print(FGM_team_a)