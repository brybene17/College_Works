from argparse import ArgumentParser
import re


filename = "QB_Stats.csv"
QB_list =[]
with open(filename, 'r') as f:
    for QB in f:
        QB_info = {}
        QB = QB.rstrip()
        line_info = re.search('(^\S* \S[a-z]*),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', QB)
        if line_info:
            QB_info["Player name:"] = line_info[1]
            QB_info["Games Played:"] = line_info[2]
            QB_info["Completions:"] = line_info[3]
            QB_info["Attempts:"] = line_info[4]
            QB_info["Yards:"] = line_info[5]
            QB_info["TD:"] = line_info[6]
            QB_info["Interceptions:"] = line_info[7]
            QB_list.append(QB_info)
        else:
            None
        
Comp_Leaders = []
for player in QB_list:
    Comp_info = {}
    Comp_info.update(player)
    if int(Comp_info.get("Attempts:")) == 0:
        Comp_PCT = 0
    else:
        Comp_PCT = float(int(Comp_info.get("Completions:"))/int(Comp_info.get("Attempts:"))*100)
    Comp_Leaders.append((Comp_PCT, Comp_info.get("Player name:")))
sorted_list = sorted(Comp_Leaders, reverse= True, key=lambda x: x[0])
for item in sorted_list[0:5]:
    print(f'{item[-1]} has a completion rate of {item[0]}%')




    