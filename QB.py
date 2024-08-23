import re

class Quarterback_Stat_Leaders:
    def __init__(self, stat):
        self.stat = stat

    def parse_QB(self, QB):
        """Takes a line of information from a csv file and uses a regular expression to seperate 
        the information and creates a dictionary.
        
        Args:
            QB: A line from a csv file with statistics from a quarterback.
        
        Returns:
            Dictionary of a player bio
        """
        QB_info = {}
        QB = QB.rstrip()
        line_info = re.search('^(.+?),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', QB)
        if line_info:
            QB_info["Player name"] = line_info[1]
            QB_info["Games Played"] = int(line_info[2] or 0)
            QB_info["Completions"] = int(line_info[3] or 0)
            QB_info["Attempts"] = int(line_info[4] or 0)
            QB_info["Yards"] = int(line_info[5] or 0)
            QB_info["TD"] = int(line_info[6] or 0)
            QB_info["Interceptions"] = int(line_info[7] or 0)
                
        else:
            None
        return QB_info
        
    def Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players.
        
        Args:
            Stat: Pass_YDS, TD, Comp_PCT
        
        Returns:
            a list of the top 5 players numerically based on the statistic.
        """
        filename = "QB_Stats.csv"
        QB_info = []
        with open(filename, 'r') as f:
            for line in f:
                QB_info.append(self.parse_QB(line))
        if self.stat == "Pass_YDS":
            Pass_Leaders= []
            for player in QB_info:
                pass_info = {}
                pass_info.update(player)
                Pass_Leaders.append(((pass_info.get("Yards")), pass_info.get("Player name")))
            sorted_list = sorted(Pass_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has thrown for {item[0]} yards')

        elif self.stat == "TD":
            TD_Leaders= []
            for player in QB_info:
                    TD_info = {}
                    TD_info.update(player)
                    TD_Leaders.append(((TD_info.get("TD")), TD_info.get("Player name")))
            sorted_list = sorted(TD_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has thrown {item[0]} Touchdowns')

        elif self.stat == "Comp_PCT":
            Comp_Leaders= []
            for player in QB_info:
                Comp_info = {}
                Comp_info.update(player)
                if int(Comp_info.get("Attempts")) == 0:
                    Comp_PCT = 0
                else:
                    Comp_PCT = float((Comp_info.get("Completions"))/(Comp_info.get("Attempts"))*100)
                Comp_Leaders.append((Comp_PCT, Comp_info.get("Player name")))
            sorted_list = sorted(Comp_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has a completion rate of {item[0]}%')
            
        else:
            print("Cannot Compute")
