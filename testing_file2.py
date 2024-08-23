from QB import Quarterback_Stat_Leaders
from QB_player import Quaterback_Stats
from RB import Running_Back_Stat_Leaders
from RB_player import Running_Back
from TE import Tight_End_Stat_Leaders
from TE_player import Tight_End
from WR import Wide_Receiver_Stat_Leaders
from WR_player import Wide_Receiver

QB_list = Quarterback_Stat_Leaders("Comp_PCT")
QB_list.Stats()

QB_bio = Quaterback_Stats("Tom Brady")
QB_bio.Quarter_Back_Stats()

RB_bio = Running_Back("Austin Ekeler")
RB_bio.Running_Back_Stats()

RB_list = Running_Back_Stat_Leaders("TD")
RB_list.Stats()

Te_bio = Tight_End("Travis Kelce")
Te_bio.Tight_End_Stats()

RB_list = Tight_End_Stat_Leaders("TD")
RB_list.Stats()

WR_bio = Wide_Receiver("Stefon Diggs")
WR_bio.Wide_Receiver_Stats()

WR_list = Wide_Receiver_Stat_Leaders("YDS_Per_Catch")
WR_list.Stats()