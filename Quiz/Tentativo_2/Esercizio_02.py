# Esercizio 02
'''
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
'''

def conto_alla_rovescia(num:int) -> int:

    if num < 0:
        print("Errore")

    elif num == 0:
        print(0)

    else:
        print(num)
        conto_alla_rovescia(num - 1)

conto_alla_rovescia(10)