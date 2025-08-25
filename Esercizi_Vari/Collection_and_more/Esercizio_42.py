'''
Raggruppa tipi di elementi

Tema: Liste e dizionari
Obiettivo: Separare elementi in base al tipo

Nome: raggruppa_per_tipo

Traccia:
Scrivi una funzione raggruppa_per_tipo(lista: list[Any]) -> dict[str, list[Any]] 
che prenda una lista mista e ritorni un dizionario con chiavi: "numeri", "stringhe", "altri" 
per raggruppare gli elementi in base al tipo.

Input:
lista = [1, "ciao", 3.5, True, "Python", None, 42]
'''
from typing import Any

def raggruppa_per_tipo(lista: list[Any]) -> dict[str, list[Any]]:
    risultato = {"numeri": [], "stringhe": [], "altri": []}

    for elemento in lista:
        if isinstance(elemento, (int, bool, float)):
            risultato["numeri"].append(elemento)
        
        elif isinstance(elemento, str):
            risultato["stringhe"].append(elemento)
        
        else:
            risultato["altri"].append(elemento)
    
    return risultato

lista = [1, "ciao", 3.5, True, "Python", None, 42]
print(raggruppa_per_tipo(lista))
        