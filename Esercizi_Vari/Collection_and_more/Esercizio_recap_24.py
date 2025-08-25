'''
Tema: Dizionari e liste
Obiettivo: Raggruppamento in base alla lunghezza delle stringhe

Nome dell’esercizio: raggruppa_per_lunghezza

Traccia:
Scrivi una funzione che, data una lista di stringhe, ritorni un dizionario in cui:

Le chiavi sono le lunghezze delle stringhe.
I valori sono liste di stringhe che hanno quella lunghezza.

Suggerimento: Usa len() per calcolare la lunghezza di ciascuna stringa.

Input: 
stringhe = ["sole", "luna", "cielo", "mare", "terra", "fuoco", "aria", "ghiaccio"]
'''

def raggruppa_per_lunghezza(stringhe: list[str]) -> dict[int, list[str]]:
    risultato = {}

    for stringa in stringhe:
        lunghezza = len(stringa)
        if lunghezza not in risultato:
            risultato[lunghezza] = []
        risultato[lunghezza] += [stringa]
    
    return risultato

stringhe = ["sole", "luna", "cielo", "mare", "terra", "fuoco", "aria", "ghiaccio", ""]
print(raggruppa_per_lunghezza(stringhe))