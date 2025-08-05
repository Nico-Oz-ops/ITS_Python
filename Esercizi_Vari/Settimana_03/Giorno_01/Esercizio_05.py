'''
Tema: Liste di dizionari → Calcoli aggregati
Obiettivo:  Calcolare medie raggruppate per chiave
'''

# Esercizio 05
# Titolo: "Media dei voti per corso"

'''
Traccia:
Hai una lista di dizionari, dove ogni elemento rappresenta uno studente con nome, corso e voto.
Scrivi una funzione che restituisca un dizionario in cui:

* le chiavi sono i nomi dei corsi
* i valori sono le medie aritmetiche dei voti degli studenti di ciascun corso.

studenti = [
    {"nome": "Anna", "corso": "Matematica", "voto": 28},
    {"nome": "Luca", "corso": "Fisica", "voto": 25},
    {"nome": "Marco", "corso": "Matematica", "voto": 30},
    {"nome": "Giulia", "corso": "Fisica", "voto": 22},
    {"nome": "Elena", "corso": "Chimica", "voto": 27}
]

Suggerimento:
Puoi usare due dizionari temporanei: uno per sommare i voti per ogni corso e uno per 
contare quanti studenti per corso, poi dividere alla fine.
'''

def media_voti_corsi(studenti: list[dict]) -> dict[str, float]:
    somma_voti = {}
    studenti_corso = {}

    for elemento in studenti:
        corso = elemento["corso"]
        voto = elemento["voto"]

        if corso not in somma_voti:
            somma_voti[corso] = 0
            studenti_corso[corso] = 0
        
        somma_voti[corso] += voto
        studenti_corso[corso] += 1
    
    media = {}
    for corso in somma_voti:
        media[corso] = round(somma_voti[corso] / studenti_corso[corso], 2)
    
    return media

studenti = [
    {"nome": "Anna", "corso": "Matematica", "voto": 28},
    {"nome": "Luca", "corso": "Fisica", "voto": 25},
    {"nome": "Marco", "corso": "Matematica", "voto": 30},
    {"nome": "Giulia", "corso": "Fisica", "voto": 22},
    {"nome": "Elena", "corso": "Chimica", "voto": 27}
]

print(media_voti_corsi(studenti))

    

