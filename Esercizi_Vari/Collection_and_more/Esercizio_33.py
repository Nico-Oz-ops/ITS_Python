'''
Tema: Dizionari annidati (verifica più campi)
Obiettivo: Controllare due condizioni nello stesso sotto-dizionario

Nome dell’esercizio: Studente adulto e iscritto

Traccia:
Scrivi una funzione adulto_iscritto_a(studenti: dict, nome: str, corso: str) -> bool che ritorni True solo se:

* Lo studente esiste
* È iscritto al corso indicato
* Ha almeno 21 anni
* Altrimenti ritorna False.

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}
'''
def adulto_iscritto_a(studenti: dict, nome: str, corso: str) -> bool:
    if nome in studenti:
        return studenti[nome]["corso"] == corso and studenti[nome]["eta"] >= 21 
    return False

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}

print(adulto_iscritto_a(studenti, "Marco", "Informatica"))
print(adulto_iscritto_a(studenti, "Luca", "Matematica"))
print(adulto_iscritto_a(studenti, "Giulia", "Fisica"))
print(adulto_iscritto_a(studenti, "Anna", "Informatica"))