import re

class Wide_Receiver_Stat_Leaders:
    def __init__(self, stat):
        self.stat = stat

    def parse_WR(self, WR):
        """Takes a line of information from a csv file and uses a regular expression to seperate 
        the information and creates a dictionary.
        
        Args:
            WR: A line from a csv file with statistics from a Wide Receiver.
        
        Returns:
            Dictionary of a player bio.
        """
        WR_info = {}
        WR = WR.rstrip()
        line_info = re.search('^(.+?),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', WR)
        if line_info:
            WR_info["Player name"] = line_info[1]
            WR_info["Games Played"] = int(line_info[2] or 0)
            WR_info["Targets"] = int(line_info[3] or 0)
            WR_info["Receptions"] = int(line_info[4] or 0)
            WR_info["Rec_YDS"] = int(line_info[5] or 0)
            WR_info["TD"] = int(line_info[6] or 0)
                
        else:
            None
        return WR_info
        
    def Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players.
        
        Args:
            Stat: Rec_YDS, TD, YDS_Per_Catch
        
        Returns:
            a list of the top 5 players numerically based on the statistic.
        """
        filename = "WR_Stats.csv"
        WR_info = []
        with open(filename, 'r') as f:
            for line in f:
                WR_info.append(self.parse_WR(line))
        if self.stat == "Rec_YDS":
            Rec_Leaders= []
            for player in WR_info:
                Rec_info = {}
                Rec_info.update(player)
                Rec_Leaders.append(((Rec_info.get("Rec_YDS")), Rec_info.get("Player name")))
            sorted_list = sorted(Rec_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has {item[0]} receiving yards')

        elif self.stat == "TD":
            TD_Leaders= []
            for player in WR_info:
                    TD_info = {}
                    TD_info.update(player)
                    TD_Leaders.append(((TD_info.get("TD")), TD_info.get("Player name")))
            sorted_list = sorted(TD_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has caught {item[0]} Touchdowns')

        elif self.stat == "YDS_Per_Catch":
            YPC_Leaders= []
            for player in WR_info:
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