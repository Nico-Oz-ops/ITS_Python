'''
Tema: Liste di dizionari - Filtraggio e selezione valori
Obiettivo: Dato un elenco di studenti con i loro voti, trovare per ciascuno il voto minimo 
che sia maggiore di una soglia indicata.

Nome dell’esercizio: voto_minimo_sopra

Traccia:
Scrivi una funzione chiamata voto_minimo_sopra che, data una 
lista di studenti (ognuno rappresentato da un dizionario con nome e 
lista di voti numerici) e una soglia numerica, ritorni un dizionario che associa 
a ogni studente il voto minimo tra quelli maggiori della soglia.

Se uno studente non ha voti sopra la soglia, il voto minimo sarà None.

Esempio di input:
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

Suggerimento: Puoi usare min() con un generatore filtrato o un ciclo con condizionale.
'''

# Alternativa 1
def voto_minimo_sopra(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    return {studente["nome"]: min((voto for voto in studente["voti"] if voto > soglia), default=None) for studente in studenti}

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Juan", "voti": [18, 19, 18]}
]
soglia = 20

print(voto_minimo_sopra(studenti, soglia))

# Alternativa 2
def voto_minimo_sopra(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    risultato = {}

    for studente in studenti:
        voto_sopra_soglia = [voto for voto in studente["voti"] if voto > soglia]

        if voto_sopra_soglia:
            risultato[studente["nome"]] = min(voto_sopra_soglia)
        
        else:
            risultato[studente["nome"]] = None
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Juan", "voti": [18, 19, 18]}
]
soglia = 20

print(voto_minimo_sopra(studenti, soglia))