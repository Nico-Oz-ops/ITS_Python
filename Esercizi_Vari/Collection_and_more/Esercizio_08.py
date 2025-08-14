'''
Tema:
Liste di dizionari - Filtraggio e selezione valori

Obiettivo:
Dato un elenco di studenti con i loro voti, trovare per ciascuno 
il voto massimo che sia inferiore a una soglia indicata.

Nome dell’esercizio: voto_massimo_sotto

Traccia:
Scrivi una funzione chiamata voto_massimo_sotto che, 
data una lista di studenti (ognuno rappresentato da un dizionario con nome e lista di voti numerici) 
e una soglia numerica, ritorni un dizionario che associa a ogni studente il voto massimo tra quelli 
inferiori alla soglia.

Se uno studente non ha voti inferiori alla soglia, il voto massimo sarà None.

Esempio di input:
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

Suggerimento
Puoi usare max() con un generatore filtrato o un approccio con ciclo e condizionale.
'''

# Alternativa 1 - uso di classico ciclo for con list comprehension
def voto_massimo_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:

    risultato = {} # Creo un dizionario vuoto dove inserirò il massimo voto sotto la soglia per ogni studente

    for studente in studenti: # Ciclo su ciascun studente della lista 

        # Filtro solo i voti inferiori alla soglia
        voti_sotto_soglia = [voto for voto in studente ["voti"] if voto < soglia]

        # Se ci sono voti sotto la soglia, prendi il massimo; altrimenti None
        if voti_sotto_soglia:
            risultato[studente["nome"]] = max(voti_sotto_soglia)
        
        else:
            risultato[studente["nome"]] = None
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

print(voto_massimo_sotto(studenti, soglia))

# Alternativa 2 - dict comprehension
def voto_massimo_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    return {studente["nome"]: max((voto for voto in studente["voti"] if voto < soglia), default=None) for studente in studenti}

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26, 19]},
    {"nome": "Nico", "voti": [27, 25, 29]}
]
soglia = 20

print(voto_massimo_sotto(studenti, soglia))