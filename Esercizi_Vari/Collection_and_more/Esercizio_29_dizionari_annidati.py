'''
Tema: Dizionari annidati (accesso ai dati)
Obiettivo: Prendere confidenza con lettura e accesso a valori dentro dizionari annidatiù

Nome dell’esercizio: Estrai l’età

Traccia:
Scrivi una funzione estrai_eta(studenti: dict, nome: str) -> int che, dato un dizionario 
di studenti strutturato così:

studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"}
}

e una stringa nome, ritorni l’età corrispondente a quello studente.
Se lo studente non esiste, ritorna None.

Suggerimento: Usa dict.get() per evitare errori se il nome non c’è.
'''
# Alternativa 1
def estrai_eta(studenti: dict[str, dict[str, str | int]], nome: str) -> int | None:
    if nome in studenti:
        return studenti[nome]["eta"]
    return None


studenti = {
    "Marco": {"eta": 20, "corso": "Informatica"},
    "Luca": {"eta": 22, "corso": "Matematica"},
    "Giulia": {"eta": 21, "corso": "Fisica"}
}

print(estrai_eta(studenti, "Marco"))
print(estrai_eta(studenti, "Nico"))
print(estrai_eta(studenti, "Giulia"))

