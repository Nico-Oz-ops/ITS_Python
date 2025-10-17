'''
Tema: Filtraggio di dati in liste di dizionari

Obiettivo: Estrarre elementi che soddisfano una condizione logica

Nome dell’esercizio: Get Adults Names

Traccia:
Scrivi una funzione chiamata get_adults_names che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta una persona e contiene le chiavi "nome" e "eta".

La funzione deve restituire una lista contenente solo i nomi delle persone la cui età è maggiore o uguale a 18.

Esempio di input:

[
    {"nome": "Luca", "eta": 20},
    {"nome": "Sara", "eta": 17},
    {"nome": "Marta", "eta": 25}
]

Esempio di output:

["Luca", "Marta"]
'''

def get_adults_names(persone: list[dict[str, int]]) -> str:
    return [persona["nome"] for persona in persone if persona["eta"] >= 18]

persone = [
    {"nome": "Luca", "eta": 20},
    {"nome": "Sara", "eta": 17},
    {"nome": "Marta", "eta": 25}
]

print(get_adults_names(persone))