# Esercizio 09
'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.
'''

def remove_elements(set1: set[int], list_rimuovere: list[int]) -> set:

    senza_elementi_lista = set1.difference(list_rimuovere)
    return senza_elementi_lista

print(remove_elements({5, 6, 7}, [7, 8, 9]))