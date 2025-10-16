'''
Tema: Analisi di una lista di dizionari

Obiettivo:
Data in input una lista di dizionari contenenti informazioni su persone ({"nome": str, "età": int}), 
la funzione deve restituire un dizionario con i dati di età più giovane, più vecchia e media.

Nome dell’esercizio: analyze_people

Traccia:
Scrivi una funzione con il seguente header:

* def analyze_people(people: list[dict[str, int]]) -> dict[str, any]:

La funzione deve restituire un dizionario con queste chiavi:

* "youngest" → il nome della persona più giovane
* "oldest" → il nome della persona più vecchia
* "average_age" → l’età media delle persone

Vincoli:

Non usare funzioni built-in come min(), max(), sorted() o simili.
Non usare librerie esterne.

Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
'''
from typing import Any

def analyze_people(people: list[dict[str, int]]) -> dict[str, Any]:
    if not people:
        raise ValueError("Lista vuota")
    
    youngest_name = people[0]["nome"]
    oldest_name = people[0]["nome"]
    youngest_age = people[0]["età"]
    oldest_age = people[0]["età"]
    somma_eta = 0
    dict_persone = {}

    for persona in people:
        eta = persona["età"]

        if eta < youngest_age:
            youngest_age = eta
            youngest_name = persona["nome"]
        
        if eta > oldest_age:
            oldest_age = eta
            oldest_name = persona["nome"]
        
        somma_eta += eta

    media_eta = somma_eta / len(people)
    
    dict_persone["youngest"] = youngest_name
    dict_persone["oldest"] = oldest_name
    dict_persone["average age"] = float(media_eta)

    return dict_persone

persone = [
    {"nome": "Luca", "età": 19},
    {"nome": "Anna", "età": 25},
    {"nome": "Marco", "età": 30},
    {"nome": "Giulia", "età": 22}
]

print(analyze_people(persone))
    
