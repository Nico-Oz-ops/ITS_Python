'''
Esercizio 3

Tema: Filtraggio e stringhe
Obiettivo: Usare filter e comprensioni

Nome dell’esercizio: Filtra parole lunghe

Traccia:
Scrivi una funzione filtra_parole_lunghe(lista, n) che, data una lista di 
parole e un numero n, ritorni una lista contenente solo le parole con lunghezza maggiore di n.

Esempio:

filtra_parole_lunghe(["ciao", "programmazione", "python", "code"], 4)
# Output: ["programmazione", "python"]
'''
# Alternativa 1
def filtra_parole(parole: list[str], n: int):
    return list(filter(lambda parola: len(parola) > n, parole))

parole = ["ciao", "programmazione", "python", "code"]
print(filtra_parole(parole, 4))

# Alternativa 2
def filtra_parole(parole: list[str], n: int):
    risultato = []

    for parola in parole:
        if len(parola) > n:
            risultato.append(parola)
    return risultato

parole = ["ciao", "programmazione", "python", "code"]
print(filtra_parole(parole, 4))

# Alternativa 3
def filtra_parole(parole: list[str], n: int):
    return [parola for parola in parole if len(parola) > n]

parole = ["ciao", "programmazione", "python", "code"]
print(filtra_parole(parole, 4))