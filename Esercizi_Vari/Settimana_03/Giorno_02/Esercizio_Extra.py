'''
Tema: Mix avanzato di filter, map, reduce, lambda, any e comprehension
Obiettivo: Manipolare una lista di stringhe con più condizioni e operazioni
'''

# Esercizio Extra
# Titolo: "Analisi parole speciali"

'''
Traccia:
Scrivi una funzione analizza_parole(parole) che, data una lista di parole (stringhe), esegue i seguenti passi:

* Filtra le parole che contengono almeno una vocale (usa any + filter)
* Da queste parole filtrate, prendi solo quelle con lunghezza maggiore di 4 (usa un altro filtro o comprehension)
* Trasforma tutte queste parole in maiuscolo (usa map o comprehension)

Calcola la somma totale delle lunghezze delle parole trasformate (usa reduce)

La funzione deve restituire una tupla con:

La lista delle parole trasformate (in maiuscolo)
La somma totale delle lunghezze di queste parole

Esempio:
analizza_parole(["ciao", "strano", "xylophone", "sky", "computer", "prst"])
(['STRANO', 'XYLOPHONE', 'COMPUTER'], 22)
'''

from functools import reduce 

# Versione con filter, lambda, map e reduce
def analizza_parole(parole: list[str]) -> tuple[list[str], int]:

    vocali = "aeiouAEIOU"
    parole_con_vocale_mag_4 = filter(lambda parola: any(lettera in vocali for lettera in parola) and len(parola) > 4, parole)
    parole_maiuscolo = list(map(lambda parola: parola.upper(), parole_con_vocale_mag_4))
    somma_totale = reduce(lambda acc, parola: acc + len(parola), parole_maiuscolo, 0)

    return parole_maiuscolo, somma_totale

print(analizza_parole(["ciao", "strano", "xylophone", "sky", "computer", "prst"]))

# Versione con comprehension e filter, lambda
def analizza_parole(parole: list[str]) -> tuple[list[str], int]:

    vocali = "aeiouAEIOU"
    parole_con_vocale = filter(lambda parola: any(lettera in vocali for lettera in parola), parole)
    parole_len_mag_4 = [parola.upper() for parola in parole_con_vocale if len(parola) > 4]
    somma_parole = sum(len(parola) for parola in parole_len_mag_4)

    return parole_len_mag_4, somma_parole

print(analizza_parole(["ciao", "strano", "xylophone", "sky", "computer", "prst"]))