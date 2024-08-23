import re

class Running_Back:
    def __init__(self, player):
        self.player = player

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

    def Running_Back_Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players. Then, it looks through that list of
        dictionaries to match the player name input.
        
        Args:
            Player: A name of a Running Back.
        
        Returns:
            Dictionary of the player's stored statistics.
        """
        filename = "RB_Stats.csv"
        RB_info = []
        with open(filename, 'r') as f:
            for line in f:
                RB_info.append(self.parse_RB(line))
        for player in RB_info:
            player_info = {}
            player_info.update(player)
            if player_info.get("Player name") == self.player:
                for key, value in player_info.items():
                    print(f'{key} : {value}')