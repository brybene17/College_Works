import re

class Quaterback_Stats:
    def __init__(self, player):
        self.player = player

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

    def Quarter_Back_Stats(self):
        """Feeds the parse method a line from the csv file to seperate and gets it back
        to make a list of dictionaries for the players. Then, it looks through that list of
        dictionaries to match the player name input.
        
        Args:
            Player: A name of a Quarterback.
        
        Returns:
            Dictionary of the player's stored statistics.
        """
        filename = "QB_Stats.csv"
        QB_info = []
        with open(filename, 'r') as f:
            for line in f:
                QB_info.append(self.parse_QB(line))
        for player in QB_info:
            player_info = {}
            player_info.update(player)
            if player_info.get("Player name") == self.player:
                for key, value in player_info.items():
                    print(f'{key} : {value}')