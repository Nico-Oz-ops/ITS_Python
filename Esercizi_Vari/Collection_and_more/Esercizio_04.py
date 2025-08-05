'''
Tema: Liste, dizionari, filter e lambda
Obiettivo: Riconoscere gli elementi che appaiono più di una volta e la loro posizione

Nome dell’esercizio: Indici degli elementi duplicati

Traccia:
Scrivi una funzione che, data una lista di elementi, restituisce un dizionario in cui 
le chiavi sono gli elementi duplicati, e i valori sono le liste degli indici in cui compaiono nella lista originaria.

indici_duplicati(["a", "b", "c", "a", "b", "a"])
{'a': [0, 3, 5], 'b': [1, 4]}

Suggerimento: Usa un dizionario per raccogliere tutti gli indici degli elementi mentre scorri la lista, 
poi filtra solo quelli che hanno più di una posizione.
'''
from typing import Any

def indici_duplicati(elementi: list[int|float|str]) -> dict[Any, list[int]]:
    raccolta = {}
    indice = 0

    for elemento in elementi:
        if elemento not in raccolta:
            raccolta[elemento] = []

        raccolta[elemento].append(indice)
        indice += 1
    
    return {elemento: indici for elemento, indici in raccolta.items() if len(indici) > 1}

elementi = ["a", "b", "c", "a", "b", "a"]
print(indici_duplicati(elementi))


