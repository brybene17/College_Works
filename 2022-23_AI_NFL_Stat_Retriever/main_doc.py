from QB import Quarterback_Stat_Leaders
from QB_player import Quaterback_Stats
from RB import Running_Back_Stat_Leaders
from RB_player import Running_Back
from TE import Tight_End_Stat_Leaders
from TE_player import Tight_End
from WR import Wide_Receiver_Stat_Leaders
from WR_player import Wide_Receiver


def main():
    """An NFL statistics database by position or by player name. """
    while True:
        position = input("What position is your player? [QB, RB, WR, TE or Stop]: ")
        if position == "Stop":
            break
        elif position == "QB":
            player_or_stat = input("Would you like to see a player's stats or the top players by stat? [player or stat]: ")
            if player_or_stat == "stat":
                stat = input("What QB statistic would you like to see?[Pass_YDS, TD, Comp_PCT]: ")
                QB_list = Quarterback_Stat_Leaders(stat)
                QB_list.Stats()
            elif player_or_stat == "player":
                player = input("Which QB's stats do you want to see? [ex: 'Patrick Mahomes']: ")
                QB_bio = Quaterback_Stats(player)
                QB_bio.Quarter_Back_Stats()
        elif position == "RB":
            player_or_stat = input("Would you like to see a player's stats or the top players by stat? [player or stat]: ")
            if player_or_stat == "stat":
                stat = input("What RB statistic would you like to see?[Rush_YDS, TD, Rec_YDS, YDS_Per_Carry]: ")
                RB_list = Running_Back_Stat_Leaders(stat)
                RB_list.Stats()
            elif player_or_stat == "player":
                player = input("Which RB's stats do you want to see?")
                RB_bio = Running_Back(player)
                RB_bio.Running_Back_Stats()
        elif position == "WR":
            player_or_stat = input("Would you like to see a player's stats or the top players by stat? [player or stat]: ")
            if player_or_stat == "stat":
                stat = input("What WR statistic would you like to see?[Rec_YDS, TD, YDS_Per_Catch]: ")
                WR_list = Wide_Receiver_Stat_Leaders(stat)
                WR_list.Stats()
            elif player_or_stat == "player":
                player = input("Which WR's stats do you want to see?")
                WR_bio = Wide_Receiver(player)
                WR_bio.Wide_Receiver_Stats()
        elif position == "TE":
            player_or_stat = input("Would you like to see a player's stats or the top players by stat? [player or stat]: ")
            if player_or_stat == "stat":
                stat = input("What TE statistic would you like to see?[Rec_YDS, TD, YDS_Per_Catch]: ")
                TE_list = Tight_End_Stat_Leaders(stat)
                TE_list.Stats()
            elif player_or_stat == "player":
                player = input("Which TE's stats do you want to see?")
                TE_bio = Tight_End(player)
                TE_bio.Tight_End_Stats()
main()
