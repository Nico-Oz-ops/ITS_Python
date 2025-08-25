'''
Conta elementi unici

Tema: Dizionari e set
Obiettivo: Contare quante volte compare ogni elemento

Nome: conteggio_elementi

Traccia:
Scrivi una funzione conteggio_elementi(lista: list[Any]) -> dict[Any, int] 
che ritorni un dizionario con gli elementi della lista come chiavi e il numero di occorrenze come valori.

Input:
elementi = ["apple", "banana", "apple", "orange", "banana", "apple"]
'''
from typing import Any

def conteggio_elementi(elementi: list[Any]) -> dict[Any, int]:
    risultato = {}

    for elemento in elementi:
        if elemento not in risultato:
            risultato[elemento] = 0
        
        risultato[elemento] += 1
    
    return risultato

elementi = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(conteggio_elementi(elementi))

# Alternativa pro
from collections import Counter

def conteggio_elementi(elementi: list[Any]) -> dict[Any, int]:
    conteggio = dict(Counter(elementi))
    return conteggio

elementi = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(conteggio_elementi(elementi))
