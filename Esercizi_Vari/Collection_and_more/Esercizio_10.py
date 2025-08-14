'''
Tema: Liste di dizionari - Ricerca condizionata
Obiettivo: Dato un elenco di studenti con una lista di voti in ordine cronologico, 
trovare per ciascuno il primo voto inferiore a una soglia.

Nome dell’esercizio: primo_voto_sotto

Traccia:
Scrivi una funzione chiamata primo_voto_sotto che, data una lista di studenti e una soglia, 
ritorni un dizionario in cui la chiave è il nome dello studente e il valore è il primo voto 
nella lista che sia inferiore alla soglia, oppure None se non esistono voti inferiori alla soglia 
per quello studente.

Esempio di input:
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

Suggerimento: Puoi usare un ciclo for e interrompere la ricerca con break quando trovi il primo voto valido.
'''
# Alternativa 1
def primo_voto_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    risultato = {}

    for studente in studenti:
        for voto in studente["voti"]:
            if voto < soglia:
                risultato[studente["nome"]] = voto
                break
        else:
            risultato[studente["nome"]] = None
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20

print(primo_voto_sotto(studenti, soglia))

# Alternativa 2
def primo_voto_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, int]:
    # next() restituisce subito il primo elemento che rispetta la condizione, oppure None se non esiste.
    return {studente["nome"]: next((voto for voto in studente["voti"] if voto < soglia), None) for studente in studenti}

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [28, 16, 12]},
    {"nome": "Elena", "voti": [24, 26]},
    {"nome": "Javier", "voti": [20, 26, 19]}
]
soglia = 20

print(primo_voto_sotto(studenti, soglia))


