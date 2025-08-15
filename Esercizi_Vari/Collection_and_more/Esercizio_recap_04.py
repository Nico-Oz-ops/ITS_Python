'''
Tema: Liste di dizionari - Filtraggio e aggregazione
Obiettivo: Trovare gli studenti che hanno almeno un voto sopra 
una soglia e calcolare per ciascuno la media dei loro voti.

Nome dell’esercizio: studenti_media_se_hanno_voto_alto

Traccia:
Data una lista di studenti con i loro voti, restituisci un dizionario 
dove la chiave è il nome dello studente e il valore è la sua media, 
solo se ha almeno un voto è maggiore o uguale alla soglia data.


Esempio di input:
studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [18, 16, 19]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20
'''
# Alternativa 1 - dict comprehension
def studenti_media_se_hanno_voto_alto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, float]:
    return {studente["nome"]: sum(studente["voti"]) / len(studente["voti"]) for studente in studenti
            if any(voto >= soglia for voto in studente["voti"])}

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [18, 16, 19]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20
print(studenti_media_se_hanno_voto_alto(studenti, soglia))

# Alternativa 2
def studenti_media_se_hanno_voto_alto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, float]:
    risultato = {}

    for studente in studenti:
        media_voto = sum(studente["voti"]) / len(studente["voti"])
        for voto in studente["voti"]:
            if voto >= soglia:
                risultato[studente["nome"]] = media_voto
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [10, 25, 30, 18]},
    {"nome": "Giulia", "voti": [18, 16, 19]},
    {"nome": "Elena", "voti": [24, 26]},
]
soglia = 20
print(studenti_media_se_hanno_voto_alto(studenti, soglia))


