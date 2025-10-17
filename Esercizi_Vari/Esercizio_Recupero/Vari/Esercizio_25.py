'''
Tema: Manipolazione di liste di dizionari

Obiettivo: Formattare una lista di dati strutturati in una singola stringa

Nome dell’esercizio: Format Emails

Traccia:
Scrivi una funzione chiamata format_emails che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta un utente e contiene le chiavi "nome" e "email".

La funzione deve restituire una singola stringa dove ogni elemento è formattato come:
nome <email>

Gli elementi devono essere separati da una virgola.

Esempio di input:

[
    {"nome": "Anna", "email": "anna@example.com"},
    {"nome": "Marco", "email": "marco@example.com"}
]

Esempio di output:

Anna <anna@example.com>, Marco <marco@example.com>
'''

def format_emails(utenti: list[dict[str, str]]) -> str:
    formattato = [f"{utente['nome']} <{utente['email']}>" for utente in utenti]
    return ", ".join(formattato)


utenti = [
    {"nome": "Anna", "email": "anna@example.com"},
    {"nome": "Marco", "email": "marco@example.com"}
]

print(format_emails(utenti))