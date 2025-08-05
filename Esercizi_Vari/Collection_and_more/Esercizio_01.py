'''
Esercizio 1 - Elementi unici mantenendo l’ordine
Tema: Liste e set
Obiettivo: Rimuovere i duplicati da una lista mantenendo l’ordine originale

Nome dell’esercizio: elementi_unici_ordinati

Traccia:
Scrivi una funzione che prende una lista di elementi (possono essere numeri o stringhe) 
e restituisce una nuova lista con gli stessi elementi, ma senza duplicati e mantenendo l’ordine della prima occorrenza.

# Esempio:
elementi_unici_ordinati(["a", "b", "a", "c", "b", "d"])  

# Output atteso: ["a", "b", "c", "d"]

Suggerimento: Puoi usare un set per tenere traccia di cosa già è stato visto, ma la lista di output va costruita a parte.
'''

def elementi_unici_ordinati(elementi: list[int | float | str]) -> list[int | float | str]:
    elementi_visti = set()
    elementi_unici = []

    for elemento in elementi:
        if elemento not in elementi_visti:
            elementi_visti.add(elemento)
            elementi_unici.append(elemento)
    
    return elementi_unici

elementi = [1, "a", "b", 2, 1, "a", "g", "c", 4.52, "b", "d"]
print(elementi_unici_ordinati(elementi))