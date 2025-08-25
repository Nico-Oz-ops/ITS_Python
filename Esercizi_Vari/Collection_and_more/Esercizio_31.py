'''
Tema: Dizionari annidati (verifica chiavi)
Obiettivo: Controllare se un certo valore esiste dentro un sotto-dizionario

Nome dell’esercizio: Studente iscritto a corso

Traccia:
Scrivi una funzione iscritto_a(studenti: dict, nome: str, corso: str) -> bool 
che ritorna True se lo studente nome è iscritto al corso dato, altrimenti False.

Se lo studente non esiste, ritorna False.

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}
'''
def iscritto_a(studenti: dict, nome: str, corso: str) -> bool:
    if nome in studenti:
        return studenti[nome]["corso"] == corso
    return False

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}
print(iscritto_a(studenti, "Giulia", "Fisica"))
print(iscritto_a(studenti, "Marco", "Matematica"))
print(iscritto_a(studenti, "Anna", "Informatica"))
print(iscritto_a(studenti, "Paolo", "Fisica"))