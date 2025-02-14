# Uso di IF, ELIF, ELSE

'''Imagine you're participating in a Mario Kart race with your friends. 
Each player finishes the race in a specific position.
Write a Python program that takes as input the finishing position of a player, 
given as a positive integer, and returns the
position in cardinal form (e.g., "1st", "2nd", "3rd", "4th", "5th", etc.).'''

n:int = int(input("Inserta la posizione finale del giocatore: "))

# Se il giocatore arriva per primo
if n == 1:
    print(f"Campione! Sei arrivato {n}st!")

# Se il giocatore arriva secondo
elif n == 2:
    print(f"Complimenti! Sei arrivato {n}nd!")

# Se il giocatore arriva terzo
elif n == 3:
    print(f"Uf per un pelo! Sei arrivato {n}rd!")


# Se il giocatore arriva in un posto X
else:
    print(f"Peccato! Sei arrivato {n}th :/")