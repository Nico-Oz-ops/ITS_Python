'''
Esercizio 6 - Intersezione di liste

Tema: Operazioni tra liste
Obiettivo: Trovare elementi comuni

Traccia:
Scrivi una funzione che, date due liste, ritorni una lista con gli elementi comuni ad entrambe.
'''
from typing import Any

# Alternativa 1

def intersezione(lista1: list[Any], lista2: list[Any]):
    return [elemento for elemento in lista1 if elemento in lista2]

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

print(intersezione(l1, l2))

# Alternativa 2
def intersezione(lista1: list[Any], lista2: list[Any]):
    comuni = []

    for elemento in lista1:
        if elemento in lista2:
            comuni.append(elemento)
    
    return comuni

print(intersezione(l1, l2))