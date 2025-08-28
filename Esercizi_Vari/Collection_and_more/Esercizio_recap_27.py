'''
Tema: Dizionari
Obiettivo: Contare e costruire mapping.

Nome: Frequenza valori in lista

Traccia:
Scrivi una funzione conteggio_elementi(lista) che ritorni un dizionario 
in cui le chiavi sono gli elementi della lista e i valori quante volte compaiono.

lista = ["mela", "banana", "mela", "pera", "banana", "mela"]
'''
from typing import Any

# Alternativa 1
def conteggio_elementi(elementi: list[Any]) -> dict[Any, int]:
    risultato = {}

    for elemento in elementi:
        if elemento not in risultato:
            risultato[elemento] = 0
        risultato[elemento] += 1
    
    return risultato

lista = ["mela", "banana", "mela", "pera", "banana", "mela"]
print(conteggio_elementi(lista))

# Alternativa 2
def conteggio_elementi(elementi: list[Any]) -> dict[Any, int]:
    return {elemento: elementi.count(elemento) for elemento in elementi}

lista = ["mela", "banana", "mela", "pera", "banana", "mela"]
print(conteggio_elementi(lista))