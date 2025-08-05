'''
Tema: Ricorsione su tuple
Obiettivo: Contare quanti elementi negativi ci sono in una tupla di numeri.
'''

# Esercizio 03
# Titolo: "conta_negativi"

'''
Traccia:
Scrivi una funzione ricorsiva che prende una tupla di numeri e 
restituisce il numero di elementi negativi presenti.

Suggerimento:
Controlla il primo elemento, somma 1 se è negativo, e ricorri sulla tupla rimanente.
'''

def conta_negativi(num: tuple[int]) -> int:
    if len(num) == 0:
        return 0
    
    if num[0] < 0:
        return 1 + conta_negativi(num[1:])
    
    else:
        return conta_negativi(num[1:])

print(conta_negativi((3, -1, 4, -5, 0)))