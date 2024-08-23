import re

class Tight_End_Stat_Leaders:
    def __init__(self, stat):
        self.stat = stat

    def parse_TE(self, TE):
        """Takes a line of information from a csv file and uses a regular expression to seperate 
        the information and creates a dictionary.
        
        Args:
            TE: A line from a csv file with statistics from a Tight End.
        
        Returns:
            Dictionary of a player bio.
        """
        TE_info = {}
        TE = TE.rstrip()
        line_info = re.search('^(.+?),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', TE)
        if line_info:
            TE_info["Player name"] = line_info[1]
            TE_info["Games Played"] = int(line_info[2] or 0)
            TE_info["Targets"] = int(line_info[3] or 0)
            TE_info["Receptions"] = int(line_info[4] or 0)
            TE_info["Rec_YDS"] = int(line_info[5] or 0)
            TE_info["TD"] = int(line_info[6] or 0)
                
        else:
            None
        return TE_info
        
    def Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players.
        
        Args:
            Stat: Rec_YDS, TD, YDS_Per_Catch
        
        Returns:
            a list of the top 5 players numerically based on the statistic.
        """
        filename = "TE_Stats.csv"
        TE_info = []
        with open(filename, 'r') as f:
            for line in f:
                TE_info.append(self.parse_TE(line))
        if self.stat == "Rec_YDS":
            Rec_Leaders= []
            for player in TE_info:
                Rec_info = {}
                Rec_info.update(player)
                Rec_Leaders.append(((Rec_info.get("Rec_YDS")), Rec_info.get("Player name")))
            sorted_list = sorted(Rec_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has {item[0]} receiving yards')

        elif self.stat == "TD":
            TD_Leaders= []
            for player in TE_info:
                    TD_info = {}
                    TD_info.update(player)
                    TD_Leaders.append(((TD_info.get("TD")), TD_info.get("Player name")))
            sorted_list = sorted(TD_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has caught {item[0]} Touchdowns')

        elif self.stat == "YDS_Per_Catch":
            YPC_Leaders= []
            for player in TE_info:
                Comp_info = {}
                Comp_info.update(player)
                if Comp_info.get("Receptions") == 0:
                    YPC = 0
                else:
                    YPC = float((Comp_info.get("Rec_YDS"))/(Comp_info.get("Receptions")))
                YPC_Leaders.append((YPC, Comp_info.get("Player name")))
            sorted_list = sorted(YPC_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} averages {item[0]} yards per catch.')
            
        else:
            print("Cannot Compute")