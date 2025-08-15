'''
Tema: Liste e set - Elementi unici e duplicati
Obiettivo: Trovare quali elementi compaiono più di una volta in una lista e restituirli senza duplicati.

Nome dell’esercizio: elementi_ripetuti

Traccia:
Data una lista di numeri (o stringhe), scrivi una funzione che restituisca un set con 
tutti gli elementi che compaiono almeno due volte nella lista.
Suggerimento: puoi usare un dizionario o un set ausiliario per contare le occorrenze.
'''
from typing import Any

# Alternativa 1
def elementi_ripetuti(elementi: list[Any]) -> set[Any]:
    occorrenze = {}

    for elemento in elementi:
        if elemento not in occorrenze:
            occorrenze[elemento] = 1
        
        else:
            occorrenze[elemento] += 1
    
    elementi_ripetuti = set()
    for elemento in occorrenze:
        if occorrenze[elemento] > 1:
            elementi_ripetuti.add(elemento)
    
    return elementi_ripetuti

lista = [4, "ciao", 7, 2, "ciao", 4, 7, "python", 2, "python", 5]
print(elementi_ripetuti(lista))

# Alternativa 2
def elementi_ripetuti(elementi: list[Any]) -> set[Any]:
    occorrenze = {}

    for elemento in elementi:
        if elemento not in occorrenze:
            occorrenze[elemento] = 1
        
        else:
            occorrenze[elemento] += 1
    
    return set(elemento for elemento in occorrenze if occorrenze[elemento] > 1)

lista = [4, "ciao", 7, 2, "ciao", 4, 7, "python", 2, "python", 5]
print(elementi_ripetuti(lista))

