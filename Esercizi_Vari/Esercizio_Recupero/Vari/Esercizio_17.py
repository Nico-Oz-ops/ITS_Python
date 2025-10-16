'''
Nome dell’esercizio: filter_and_format_people

Traccia:
Scrivi una funzione chiamata filter_and_format_people che prende in input:

* people: lista di dizionari con chiavi "nome" (str) e "età" (int)
* min_age: intero

La funzione deve:

* Filtrare tutte le persone la cui età è maggiore o uguale a min_age.
* Convertire ogni persona filtrata in una stringa nel formato "nome(età)".
* Restituire una stringa unica con tutte le persone filtrate concatenate, separate da una virgola ",".
'''

def filter_and_format_people(people: list[dict[str, int]], min_age: int) -> str:

    return ', '.join(f"{persona['nome']}({persona['età']})" for persona in people if persona['età'] >= min_age)

people = [
    {"nome": "Luca", "età": 19},
    {"nome": "Anna", "età": 25},
    {"nome": "Marco", "età": 17},
    {"nome": "Giulia", "età": 30},
    {"nome": "Sara", "età": 22}
]

min_age = 20

print(filter_and_format_people(people, min_age))