'''
Tema: Dizionari annidati (aggiunta di valori)
Obiettivo: Aggiornare un sotto-dizionario

Nome dell’esercizio: Aggiorna età

Traccia:
Scrivi una funzione aggiorna_eta(studenti: dict, nome: str, nuova_eta: int) -> bool che:

* Se lo studente esiste, aggiorna la sua età con nuova_eta e ritorna True.
* Se lo studente non esiste, ritorna False.

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}

Esempio:
aggiorna_eta(studenti, "Marco", 25)  # aggiorna Marco a 25 anni → True
aggiorna_eta(studenti, "Paolo", 30)  # non esiste → False
'''

def aggiorna_eta(studenti: dict, nome: str, nuova_eta: int) -> bool:
    if nome in studenti:
        studenti[nome]["eta"] = nuova_eta
        return True
    return False

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}

print(aggiorna_eta(studenti, "Marco", 25))
print(aggiorna_eta(studenti, "Paolo", 30))