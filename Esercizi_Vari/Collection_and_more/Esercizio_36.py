'''
Tema: Dizionari - Filtraggio
Obiettivo: Ricavare sottoinsiemi di dati da un dizionario.

Nome dell’esercizio: Studenti promossi

Traccia:
Scrivi una funzione studenti_promossi(studenti: dict[str, int], soglia: int) -> dict[str, int] che, 
dato un dizionario studenti con nome → voto e una soglia, ritorni un nuovo dizionario con solo gli 
studenti che hanno un voto maggiore o uguale alla soglia.

studenti = {
    "Marco": 28,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 22,
    "Paolo": 15
}
soglia = 20

Suggerimento:
Puoi costruire il nuovo dizionario con un ciclo e una condizione.
'''

def studenti_promossi(studenti: dict[str, int], soglia: int) -> dict[str, int]:
    return {nome: voto for nome, voto in studenti.items() if voto >= soglia}

studenti = {
    "Marco": 28,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 22,
    "Paolo": 15
}
soglia = 20

print(studenti_promossi(studenti, soglia))