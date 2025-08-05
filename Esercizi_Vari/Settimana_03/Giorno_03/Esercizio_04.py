'''
Tema: Analisi di dati strutturati (liste e dizionari annidati) e individuazione di pattern significativi.
Obiettivo: Scrivere una funzione che individua tutte le materie in cui almeno uno studente ha avuto una media inferiore a 20.
'''

# Esercizio 04
# Titolo: "materie_con_media_bassa"

'''
Traccia:
Hai un dizionario che rappresenta gli studenti, ognuno con un sotto-dizionario 
delle materie e una lista dei voti ottenuti in ciascuna materia.

Scrivi una funzione:

def materie_con_media_bassa(studenti: dict[str, dict[str, list[int]]]) -> set[str]:

che restituisca l’insieme delle materie in cui almeno uno studente ha una media strettamente inferiore a 20.

Suggerimento:
* Ricorda che una media su una lista vuota non è definita: gestisci quel caso.
* Puoi usare any() oppure un ciclo semplice.
* Pensa a usare un set per raccogliere le materie senza ripetizioni.

studenti = {
    "Anna": {
        "matematica": [28, 30, 25],
        "storia": [30, 21, 25],
        "filosofia": [25, 26, 29]
    },
    "Luca": {
        "matematica": [18, 19, 15],
        "storia": [24, 28, 27],
        "filosofia": [27, 19, 26]
    },
    "Marta": {
        "matematica": [10, 13, 12],
        "storia": [19, 21, 0],
        "filosofia": []
    }
}
'''

def materie_con_media_bassa(studenti: dict[str, dict[str, list[int]]]) -> set[str]:

    return set(materia for studente, materie in studenti.items() # scorro ogni studente e il suo dizionario di materie -> voti
               for materia, voti in materie.items() # scorro ogni materia e lista di voti per quello studente
               if voti and (sum(voti)/ len(voti)) < 20) # evito divisioni per zero (liste vuote) e verifico se la media dei voti è sotto 20.

studenti = {
    "Anna": {
        "matematica": [28, 30, 25],
        "storia": [30, 21, 25],
        "filosofia": [25, 26, 29]
    },
    "Luca": {
        "matematica": [18, 19, 15],
        "storia": [24, 28, 27],
        "filosofia": [27, 19, 26]
    },
    "Marta": {
        "matematica": [10, 13, 12],
        "storia": [19, 21, 0],
        "filosofia": []
    }
}

print(materie_con_media_bassa(studenti))