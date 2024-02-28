"""
def Valide():
    global zone_1
    global zone_X
    global zone_2
    print(zone_1.get())
    print(zone_X.get())
    print(zone_2.get())
"""

def afficher():
    global result_label1
    global result_labelX
    global result_label2
    global Bet1
    global BetX
    global Bet2

    Bet1 = entry_Bet1.get()
    BetX = entry_BetX.get()
    Bet2 = entry_Bet2.get()
    # result_label.config(text=f"1: {Bet1} X: {BetX} 2: {Bet2}")
    result_label1.config(text=f"1:{Bet1}")
    result_labelX.config(text=f"X:{BetX}")
    result_label2.config(text=f"2:{Bet2}")
 