'''
Tema: Liste di dizionari - Aggregazione e valori minimi annidati
Obiettivo: Calcolare il voto più basso per ogni materia per ciascuno studente.

Nome dell’esercizio: voto_minimo_per_studente

Traccia:
Hai una lista di studenti, ciascuno rappresentato da un dizionario con:
"nome" → nome dello studente
"materie" → dizionario in cui le chiavi sono materie e i valori sono liste di voti

Scrivi una funzione che restituisca un dizionario in cui:
ogni chiave è il nome dello studente
il valore è un dizionario con il voto più basso di ogni materia

Esempio di input:

studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]

Suggerimento: usa min() per trovare il voto più basso in ogni lista di voti e 
considera una dict comprehension per creare i dizionari annidati.
'''
# Opzione 1
def voto_minimo_per_studente(studenti: list[dict[str, dict[str, list[int]]]]) -> dict[str, dict[str, int]]:
    risultato = {}
    for studente in studenti:
        minimo = {materia: min(studente["materie"][materia]) for materia in studente["materie"]}
        risultato[studente["nome"]] = minimo
    
    return risultato

studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]

print(voto_minimo_per_studente(studenti))


# Opzione 2
def voto_minimo_per_studente(studenti: list[dict[str, dict[str, list[int]]]]) -> dict[str, dict[str, int]]:
    risultato = {}
    for studente in studenti:
        minimo = {materia: min(voti) for materia, voti in studente["materie"].items()}
        risultato[studente["nome"]] = minimo
    
    return risultato

studenti = [
    {"nome": "Marco", "materie": {"matematica": [24, 18, 30], "storia": [18, 20]}},
    {"nome": "Giulia", "materie": {"matematica": [21, 22], "storia": [20, 19]}},
    {"nome": "Elena", "materie": {"matematica": [26, 25], "storia": [17, 21]}}
]

print(voto_minimo_per_studente(studenti))


