'''
Tema: Liste di dizionari
Obiettivo: Estrazione e filtraggio mirato da strutture dati complesse
'''

# Esercizio 02
# Titolo: "filtra_studenti_promossi"

'''
Traccia:
Ti viene fornita una lista di dizionari, dove ogni dizionario rappresenta uno studente con le seguenti chiavi:

* "nome": nome dello studente (stringa)
* "corso": il corso frequentato (stringa)
* "voto": il voto finale ottenuto (intero)

Scrivi una funzione che:

* Prenda in input questa lista.
* Filtri solo gli studenti che hanno voto maggiore o uguale a 18.
* Ritorni una nuova lista contenente solo i nomi degli studenti promossi.
'''

def filtra_studenti_promossi(studenti: list[dict]) -> list[str]:
    return [studente["nome"] for studente in studenti if studente["voto"] >= 18]

studenti = [
    {"nome": "Luca", "corso": "Matematica", "voto": 25},
    {"nome": "Sara", "corso": "Storia", "voto": 17},
    {"nome": "Anna", "corso": "Fisica", "voto": 30},
    {"nome": "Marco", "corso": "Informatica", "voto": 16}
]

print(filtra_studenti_promossi(studenti))

# Variante
def filtra_studenti_promossi(studenti: list[dict]) -> list[str]:
    return [studente["nome"] for studente in studenti if studente["voto"] >= 18 and studente["corso"] == "Informatica"]

studenti = [
    {"nome": "Luca", "corso": "Matematica", "voto": 25},
    {"nome": "Sara", "corso": "Storia", "voto": 17},
    {"nome": "Anna", "corso": "Fisica", "voto": 30},
    {"nome": "Marco", "corso": "Informatica", "voto": 16},
    {"nome": "Nico", "corso": "Informatica", "voto": 25}
]

print(filtra_studenti_promossi(studenti))


# Opzione 2 - senza list comprehension
def filtra_studenti_promossi(studenti: list[dict]) -> list[str]:
    studenti_promossi = []

    for studente in studenti:
        if studente["voto"] >= 18:
            studenti_promossi.append(studente["nome"])
    
    return studenti_promossi

studenti_2 = [
    {"nome": "Claire", "corso": "Fisica", "voto": 28},
    {"nome": "Anna", "corso": "Fisica", "voto": 18},
    {"nome": "Marco", "corso": "Informatica", "voto": 19},
    {"nome": "Nico", "corso": "Informatica", "voto": 17}
]

print(filtra_studenti_promossi(studenti_2))
