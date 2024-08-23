import re

class Running_Back_Stat_Leaders:
    def __init__(self, stat):
        self.stat = stat

    def parse_RB(self, RB):
        """Takes a line of information from a csv file and uses a regular expression to seperate 
        the information and creates a dictionary.
        
        Args:
            RB: A line from a csv file with statistics from a Running Back.
        
        Returns:
            Dictionary of a player bio.
        """
        RB_info = {}
        RB = RB.rstrip()
        line_info = re.search('^(.+?),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+),([0-9]+)', RB)
        if line_info:
            RB_info["Player name"] = line_info[1]
            RB_info["Games Played"] = int(line_info[2])
            RB_info["Rush_Attempts"] = int(line_info[3])
            RB_info["Rush_YDS"] = int(line_info[4])
            RB_info["Rush_TD"] = int(line_info[5])
            RB_info["Targets"] = int(line_info[6])
            RB_info["Receptions"] = int(line_info[7])
            RB_info["Rec_YDS"] = int(line_info[8])
            RB_info["Rec_TD"] = int(line_info[9])
        
        else:
            None
        return RB_info
        
    def Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players.
        
        Args:
            Stat: Rush_YDS, TD, Rec_YDS, YDS_Per_Carry
        
        Returns:
            a list of the top 5 players numerically based on the statistic.
        """
        filename = "RB_Stats.csv"
        RB_info = []
        with open(filename, 'r') as f:
            for line in f:
                RB_info.append(self.parse_RB(line))
        if self.stat == "Rush_YDS":
            Rush_Leaders= []
            for player in RB_info:
                rush_info = {}
                rush_info.update(player)
                Rush_Leaders.append(((rush_info.get("Rush_YDS")), rush_info.get("Player name")))
            sorted_list = sorted(Rush_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has rushed for {item[0]} yards.')

        elif self.stat == "TD":
            TD_Leaders= []
            for player in RB_info:
                    TD_info = {}
                    TD_info.update(player)
                    TD = ((TD_info.get("Rush_TD") + TD_info.get("Rec_TD")))
                    TD_Leaders.append((TD, TD_info.get("Player name")))
            sorted_list = sorted(TD_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has scored {item[0]} total Touchdowns.')

        elif self.stat == "YDS_Per_Carry":
            YPC_Leaders= []
            for player in RB_info:
                Comp_info = {}
                Comp_info.update(player)
                if Comp_info.get("Rush_Attempts") == 0:
                    YPC = 0
                else:
                    YPC = float((Comp_info.get("Rush_YDS"))/(Comp_info.get("Rush_Attempts")))
                YPC_Leaders.append((YPC, Comp_info.get("Player name")))
            sorted_list = sorted(YPC_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} averages {item[0]} yards per carry.')
            
        elif self.stat == "Rec_YDS":
            Rec_Leaders = []
            for player in RB_info:
                rec_info = {}
                rec_info.update(player)
                Rec_Leaders.append(((rec_info.get("Rec_YDS")), rec_info.get("Player name")))
            sorted_list = sorted(Rec_Leaders, reverse= True, key=lambda x: x[0])
            for item in sorted_list[0:5]:
                print(f'{item[-1]} has {item[0]} receiving yards')

        else:
            print("Cannot Compute")
