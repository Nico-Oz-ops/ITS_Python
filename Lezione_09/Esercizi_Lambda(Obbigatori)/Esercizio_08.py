# Esercizio 08
'''
Doppio ordinamento
Hai una lista di dizionari:

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]
Ordina la lista in ordine decrescente di media usando una funzione lambda.
'''

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

media_decrescente = sorted(studenti, key=lambda studente: studente["media"], reverse=True)
print(media_decrescente)

print("-" * 50)

def media_studenti(studente):
    return studente["media"]

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

studenti_ordinati = sorted(studenti, key=media_studenti, reverse=True)
print(studenti_ordinati)