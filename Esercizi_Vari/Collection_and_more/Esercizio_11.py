'''
Tema: Liste di dizionari - Aggregazione e filtro
Obiettivo: Restituire la lista dei nomi degli studenti che hanno la media inferiore a una soglia.

Nome dell’esercizio: studenti_con_media_sotto

Traccia:
Scrivi una funzione chiamata studenti_con_media_sotto che, 
data una lista di studenti e una soglia numerica, ritorni una 
lista con i nomi degli studenti la cui media dei voti è minore della soglia.

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Luca", "voti": [15, 18, 17]},
]
soglia = 20

Suggerimento: Puoi calcolare la media con sum(voti) / len(voti) e usare una 
list comprehension per il filtraggio.
'''
# Alternativa 1
def studenti_con_media_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    risultato = []

    for studente in studenti:
        media_voti = sum(studente["voti"]) / len(studente["voti"])
        if media_voti < soglia:
            risultato.append(studente["nome"])
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Luca", "voti": [15, 18, 17]},
]
soglia = 20

print(studenti_con_media_sotto(studenti, soglia))

# Alternativa 2
def studenti_con_media_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    return [studente["nome"] for studente in studenti if ((sum(studente["voti"]) / len(studente["voti"]) < soglia))]

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Luca", "voti": [15, 18, 17]},
    {"nome": "Gianmarco", "voti": [21, 15, 16, 25]},
]
soglia = 20
print(studenti_con_media_sotto(studenti, soglia))

