import re

stat = "Pass_YDS"

def parse_QB(QB):
        QB_info = {}
        QB = QB.rstrip()
        line_info = re.search('(^\S* \S[a-z]*),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', QB)
        if line_info:
            QB_info["Player name:"] = line_info[1]
            QB_info["Games Played:"] = int(line_info[2] or 0)
            QB_info["Completions:"] = int(line_info[3] or 0)
            QB_info["Attempts:"] = int(line_info[4] or 0)
            QB_info["Yards:"] = int(line_info[5] or 0)
            QB_info["TD:"] = int(line_info[6] or 0)
            QB_info["Interceptions:"] = int(line_info[7] or 0)
                
        else:
            None
        return QB_info

if stat == "Pass_YDS":
        filename = "QB_Stats.csv"
        QB_info = []
        Pass_Leaders= []
        with open(filename, 'r') as f:
            for QB in f:
                QB_info.append(parse_QB(QB))
        for player in QB_info:
            pass_info = {}
            pass_info.update(player)
            Pass_Leaders.append((pass_info.get("Yards:"), pass_info.get("Player name:")))
        sorted_list = sorted(Pass_Leaders, reverse= True, key=lambda x: x[0])
        for item in sorted_list[0:5]:
            print(f'{item[-1]} has thrown for {item[0]} yards')

