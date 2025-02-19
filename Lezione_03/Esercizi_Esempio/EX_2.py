# Uso di MATCH

'''Imagine you're participating in a Mario Kart race with your friends. 
Each player finishes the race in a specific position.
Write a Python program that takes as input the finishing position of a player, 
given as a positive integer, and returns the
position in cardinal form (e.g., "1st", "2nd", "3rd", "4th", "5th", etc.).'''

n:int = int(input("Inserta la posizione finale del giocatore: "))

match n:
    case 1:
        print(f"Campione! Sei arrivato {n}st!")
    case 2:
        print(f"Complimenti! Sei arrivato {n}nd!")
    case 3:
        print(f"Uf, per un pelo! Sei arrivato {n}rd!")
    case _:
        print(f"Peccato, non ce l'hai fatta! Se arrivato {n}th :/")

# In this example, the match statement is used to match the value of the variable n.
# The match statement is followed by a series of case statements, each of which specifies a possible value of n.
