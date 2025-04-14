# Esercizio 07
'''
Filtra parole corte
Hai una lista di parole 
parole = ["cane", "gatto", "elefante", "ratto", "orso"] 
Estrai solo le parole con più di 4 lettere usando filter() e lambda.
'''
import re

parole = ["cane", "gatto", "elefante", "ratto", "orso"]

parole_piu_4_lettere = list(filter(lambda parola: len(parola) > 4, parole))
print(f"Le parole con più di 4 lettere sono: {parole_piu_4_lettere}")

print("-" * 50)

parole = ["cane", "gatto", "elefante", "ratto", "orso"]

parole_piu_4_lettere = list(filter(lambda parola: re.fullmatch(r"^[a-zA-Z]{5,}", parola), parole))
print(f"Le parole con più di 4 lettere sono: {parole_piu_4_lettere}")

print("-" * 50)

def cinque_lettere(parole:list[str]):
    parole_cinque_lettere = []
    for parola in parole:
        if len(parola) > 4:
            parole_cinque_lettere.append(parola)

    return parole_cinque_lettere

parole = ["cane", "gatto", "elefante", "ratto", "orso"]
print(cinque_lettere(parole))