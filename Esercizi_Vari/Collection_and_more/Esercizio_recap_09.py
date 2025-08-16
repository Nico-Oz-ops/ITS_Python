'''
Tema: Dizionari e filtri
Obiettivo: Ripassare l’uso di all() e any().

Nome dell’esercizio: studenti_senza_voti_sotto

Traccia:
Scrivi una funzione che riceve una lista di dizionari con la struttura:

studenti = [
    {"nome": "Marco", "voti": [28, 30, 25]},
    {"nome": "Lucia", "voti": [18, 20, 22]},
    {"nome": "Anna", "voti": [30, 29, 30]}
]

La funzione deve restituire una lista di nomi degli studenti che non hanno 
nessun voto sotto una certa soglia (parametro della funzione).

Esempio: con soglia 24 → risultato: ["Marco", "Anna"].

Suggerimento: Usa all() per verificare la condizione sui voti.
'''
# Alternativa 1
def studenti_senza_voti_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    return [studente["nome"] for studente in studenti if all(voto > soglia for voto in studente["voti"])]

studenti = [
    {"nome": "Marco", "voti": [28, 30, 25]},
    {"nome": "Lucia", "voti": [18, 20, 22]},
    {"nome": "Anna", "voti": [30, 29, 30]}
]

print(studenti_senza_voti_sotto(studenti, 24))

# Alternativa 2
def studenti_senza_voti_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    studenti_sopra_soglia = []

    for studente in studenti:
        if all(voto > soglia for voto in studente["voti"]):
            studenti_sopra_soglia.append(studente["nome"])
    
    return studenti_sopra_soglia

studenti = [
    {"nome": "Marco", "voti": [28, 30, 25]},
    {"nome": "Lucia", "voti": [18, 20, 22]},
    {"nome": "Anna", "voti": [30, 29, 30]}
]

print(studenti_senza_voti_sotto(studenti, 24))