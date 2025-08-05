'''
Tema: Liste, set e funzioni logiche
Obiettivo: Rafforzare l’uso di set, any, filter

Nome dell’esercizio: Presenza di elementi duplicati

Traccia:
Scrivi una funzione ha_duplicati(elementi: list) -> bool che restituisce 
True se nella lista elementi ci sono uno o più elementi ripetuti, altrimenti False.

Suggerimento:
Puoi usare set e any, oppure un approccio con filter.
'''
from typing import Any

# Alternativa 1
def ha_duplicati(elementi: list[Any]) -> bool:
    elementi_visti = set()
    return any(filter(lambda elemento: elemento in elementi_visti or elementi_visti.add(elemento), elementi))


elementi_1 = ["ciao", 1, 1, 3, "ciao", "hola", 3, 4]
elementi_2 = [1, 3, "ciao", "hola", 4]

print(ha_duplicati(elementi_1))
print(ha_duplicati(elementi_2))

# Alternativa 2
def ha_duplicati_2(elementi: list[Any]) -> bool:
    conteggio = {}

    for elemento in elementi:
        if elemento not in conteggio:
            conteggio[elemento] = 1
        else:
            return True # ritorna True, perché ha trovato più di un elemento uguale
        
    return False # se non ha trovato elementi duplicati

print(ha_duplicati_2(elementi_1))
print(ha_duplicati_2(elementi_2))