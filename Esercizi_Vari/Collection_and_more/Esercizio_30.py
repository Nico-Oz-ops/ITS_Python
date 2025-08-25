'''
Tema: Dizionari annidati (accesso ai valori)
Obiettivo: Leggere un campo specifico da un dizionario annidato

Nome dell’esercizio: Estrai il corso

Traccia:
Scrivi una funzione estrai_corso(studenti: dict, nome: str) -> str | None che, 
dato il dizionario di studenti e un nome, ritorni il corso frequentato da quello studente.

Se lo studente non esiste, ritorna None.

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}
'''
def estrai_corso(studenti: dict, nome: str) -> str | None:
    if nome in studenti:
        return studenti[nome]["corso"]
    return None

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"},
    "Anna": {"eta": 23, "corso": "Informatica"}
}
print(estrai_corso(studenti, "Marco"))
print(estrai_corso(studenti, "Luca"))
print(estrai_corso(studenti, "Nico"))


