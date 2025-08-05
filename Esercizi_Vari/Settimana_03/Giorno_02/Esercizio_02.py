'''
Tema: filter e lambda
Obiettivo: Filtrare stringhe in base a una condizione
'''

# Esercizio 02
# Titolo: "Filtra parole con almeno una vocale"

'''
Traccia:
Scrivi una funzione filtra_con_vocale(parole) che prende una lista di stringhe e 
restituisce una nuova lista contenente solo le parole che contengono almeno una vocale, utilizzando filter() e lambda.

Considera come vocali: 'aeiouAEIOU'.
'''

def filtra_con_vocale(parole: list[str]) -> list[str]:
    vocali = "aeiouAEIOU"

    parole_con_vocale = filter(lambda parola: any(lettera in vocali for lettera in parola), parole)
    return list(parole_con_vocale)

print(filtra_con_vocale(["pinta", "mono", "assurdo", "123456"]))


list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))



