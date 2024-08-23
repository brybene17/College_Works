import re

class Tight_End:
    def __init__(self, player):
        self.player = player

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

    def Tight_End_Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players. Then, it looks through that list of
        dictionaries to match the player name input.
        
        Args:
            Player: A name of a Tight End.
        
        Returns:
            Dictionary of the player's stored statistics.
        """
        filename = "TE_Stats.csv"
        TE_info = []
        with open(filename, 'r') as f:
            for line in f:
                TE_info.append(self.parse_TE(line))
        for player in TE_info:
            player_info = {}
            player_info.update(player)
            if player_info.get("Player name") == self.player:
                for key, value in player_info.items():
                    print(f'{key} : {value}')