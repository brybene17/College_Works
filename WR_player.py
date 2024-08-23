import re

class Wide_Receiver:
    def __init__(self, player):
        self.player = player

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

    def Wide_Receiver_Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players. Then, it looks through that list of
        dictionaries to match the player name input.
        
        Args:
            Player: A name of a Wide Receiver.
        
        Returns:
            Dictionary of the player's stored statistics.
        """
        filename = "WR_Stats.csv"
        WR_info = []
        with open(filename, 'r') as f:
            for line in f:
                WR_info.append(self.parse_WR(line))
        for player in WR_info:
            player_info = {}
            player_info.update(player)
            if player_info.get("Player name") == self.player:
                for key, value in player_info.items():
                    print(f'{key} : {value}')