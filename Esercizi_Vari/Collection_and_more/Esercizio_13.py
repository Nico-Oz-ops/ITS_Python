'''
Tema: Liste di dizionari - Controllo universale con all()
Obiettivo: Trovare gli studenti che non hanno mai preso un voto inferiore a una certa soglia.

Nome dell’esercizio: studenti_senza_voti_sotto

Traccia:
Scrivi una funzione chiamata studenti_senza_voti_sotto che, 
data una lista di studenti e una soglia numerica, ritorni una 
lista con i nomi degli studenti per i quali tutti i voti sono maggiori o uguali alla soglia.

studenti = [
    {"nome": "Marco", "voti": [25, 30, 28]},
    {"nome": "Giulia", "voti": [18, 16, 20]},
    {"nome": "Elena", "voti": [22, 24, 26]},
    {"nome": "Luca", "voti": [19, 20, 21]},
]
soglia = 20

Suggerimento: Puoi usare all(v >= soglia for v in studente["voti"]) per verificare la condizione.
'''

# Alternativa 1
def studenti_senza_voti_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    risultato = []

    for studente in studenti:
        if all(voto >= soglia for voto in studente["voti"]):
            risultato.append(studente["nome"])
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [25, 30, 28]},
    {"nome": "Giulia", "voti": [18, 16, 20]},
    {"nome": "Elena", "voti": [22, 24, 26]},
    {"nome": "Luca", "voti": [19, 20, 21]},
]
soglia = 20
print(studenti_senza_voti_sotto(studenti, soglia))

# Alternativa 2
def studenti_senza_voti_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    return [studente["nome"] for studente in studenti if all(voto >= soglia for voto in studente["voti"])]

studenti = [
    {"nome": "Marco", "voti": [25, 30, 28]},
    {"nome": "Giulia", "voti": [18, 16, 20]},
    {"nome": "Elena", "voti": [22, 24, 26]},
    {"nome": "Luca", "voti": [19, 20, 21]},
]
soglia = 20
print(studenti_senza_voti_sotto(studenti, soglia))

# Alternativa 3
def studenti_senza_voti_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> list[str]:
    risultato = []

    for studente in studenti:
        aggiungi = True # assumo inizialmente che tutti i voti siano >= soglia
        
        for voto in studente["voti"]:
            if voto < soglia:
                aggiungi = False # trovo un voto sotto la soglia, perciò non si aggiunge
                break # visto che mi interessano tutti i voti >= soglia, e ho trovato un voto < soglia, 
                      # allora interrompo il ciclo, non serve andare a controllare gli altri voti
        
        if aggiungi: # se tutti i voti nella lista sono >= soglia, allora aggiungo il nome dello studente alla lista "risultato"
            risultato.append(studente["nome"])
    
    return risultato

studenti = [
    {"nome": "Marco", "voti": [25, 30, 28]},
    {"nome": "Giulia", "voti": [18, 16, 20]},
    {"nome": "Elena", "voti": [22, 24, 26]},
    {"nome": "Luca", "voti": [19, 20, 21]},
]
soglia = 20
print(studenti_senza_voti_sotto(studenti, soglia))






