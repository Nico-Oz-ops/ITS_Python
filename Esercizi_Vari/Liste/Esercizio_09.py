'''
Esercizio 4 - Inversione lista

Tema: Manipolazione lista
Obiettivo: Invertire una lista

Traccia:
Scrivi una funzione che prenda una lista e ritorni una nuova lista con gli elementi in ordine inverso.

Suggerimento: Prova con slicing [::-1].
'''
from typing import Any

# Alternativa 1 - slicing
def inverti_lista(elementi: list[Any]):
    return elementi[::-1]

elementi = ["manzana", "mela", "hola", 15, 7.5]
print(inverti_lista(elementi))

# Alternativa 2 - for
def inverti_lista(elementi: list[Any]):
    invertita = []
    
    for i in range(len(elementi) - 1, -1, -1):
        invertita.append(elementi[i])
    return invertita

print(inverti_lista(elementi))

