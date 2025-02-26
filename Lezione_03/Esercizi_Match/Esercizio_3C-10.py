giorno = int(input("Inserire un giorno, espresso numericamente: "))
mese = int(input("Inserire un mese, espresso numericamente: "))

data = (giorno, mese)

match data:
    case (1, 1):
        print(f"Il {giorno}/{mese} è Capodanno!")
    case (14, 2):
        print(f"Il {giorno}/{mese} è San Valentino, cuoricino")
    case (18, 4):
        print(f"Il {giorno}/{mese} è il compleanno di Nico, tanti auguri!")
    case (2, 6):
        print(f"Il {giorno}/{mese} è la Festa della Repubblica Italiana")
    case (15, 8):
        print(f"Il {giorno}/{mese} è Ferragosto, weeeee")
    case (29, 8):
        print(f"Il {giorno}/{mese} è il compleanno della nena, tanti auguri!")
    case (31, 10):
        print(f"Il {giorno}/{mese} è Halloween, muaaahahaha")
    case (22, 11):
        print(f"Il {giorno}/{mese} è il compleanno della puzzona, tanti auguri puzzona! :)")
    case (25, 12):
        print(f"Il {giorno}/{mese} è Natale!")
    case _:
        print(f"Il {giorno}/{mese} non è una data importante, non c'è nessuna festività importante")
     
