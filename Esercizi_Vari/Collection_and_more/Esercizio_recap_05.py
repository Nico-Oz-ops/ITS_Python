'''
Tema: Liste di dizionari - Ricerca condizionale e dati annidati
Obiettivo: Per ogni materia, trovare lo studente che ha preso il voto più basso in quella materia.

Nome dell’esercizio: peggior_voto_per_materia

Traccia:
Hai un elenco di studenti con un dizionario di materie e relativi voti.
Restituisci un nuovo dizionario dove ogni materia è una chiave e il valore 
è una tupla (nome_studente, voto) corrispondente al voto più basso per quella materia.

Input:
studenti = [
    {"nome": "Marco", "materie": {"matematica": 24, "storia": 18}},
    {"nome": "Giulia", "materie": {"matematica": 21, "storia": 20}},
    {"nome": "Elena", "materie": {"matematica": 26, "storia": 17}}
]

Esempio output atteso: un dizionario del tipo {"matematica": ("Marco", 18).
'''

def peggior_voto_per_materia(studenti: list[dict[str, dict[str, int]]]) -> dict[str, tuple[str, int]]:
    risultato = {}

    for studente in studenti: # scorro uno per uno i dizionari degli studenti.
        for materia, voto in studente["materie"].items(): #per ogni studente, scorro tutte le materie e voti usando .items() sul dizionario "materie".
            # se la materia non è ancora presente in risultato, la aggiungo.
            # altrimenti se la materia c’è già ma il voto attuale è più basso di quello salvato 
            # allora aggiorno con il nuovo peggiore voto.
            if materia not in risultato or voto < risultato[materia][1]:
                risultato[materia] = (studente["nome"], voto)

    return risultato

studenti = [
    {"nome": "Marco", "materie": {"matematica": 24, "storia": 18}},
    {"nome": "Giulia", "materie": {"matematica": 21, "storia": 20}},
    {"nome": "Elena", "materie": {"matematica": 26, "storia": 17}}
]

print(peggior_voto_per_materia(studenti))
