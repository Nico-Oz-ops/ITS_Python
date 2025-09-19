'''
Esercizio 5 - Elementi unici

Tema: Set e liste
Obiettivo: Ottenere gli elementi senza duplicati

Traccia:
Scrivi una funzione che ritorni una lista contenente solo gli elementi unici di una 
lista iniziale (cioè senza ripetizioni).

Suggerimento: Puoi usare un set o controllare manualmente.
'''
from typing import Any

def elementi_unici(elementi: list[Any]):
    unici = []

    for elemento in elementi:
        if elemento not in unici:
            unici.append(elemento)
    
    return unici

elementi = [1, 2, 2, 3, 4, 1]
print(elementi_unici(elementi))

# Alternativa 2
def elementi_unici(elementi: list[Any]):
    return list({elemento for elemento in elementi})

print(elementi_unici(elementi))

# Alternativa 3
def elementi_unici(elementi: list[Any]):
    unici = []

    [unici.append(elemento) for elemento in elementi if elemento not in unici]

    return unici

print(elementi_unici(elementi))