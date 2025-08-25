'''
Tema: Dizionari e liste
Obiettivo: Raggruppamento in base alla lettera iniziale

Nome dell’esercizio: raggruppa_per_iniziale

Traccia:
Scrivi una funzione che, data una lista di parole (stringhe), ritorni un dizionario in cui:

Le chiavi sono le lettere iniziali maiuscole di ciascuna parola (es. "A", "B", ecc.).
I valori sono liste di parole che iniziano con quella lettera, indipendentemente dal 
fatto che siano scritte in minuscolo o maiuscolo.

Suggerimento: Ricorda di normalizzare la lettera iniziale con .upper().

Input:
parole = ["albero", "Auto", "banana", "barca", "cane", "Casa", "dado", "delfino"]
'''

def raggruppa_per_iniziale(parole: list[str]) -> dict[str, list[str]]:

    risultato = {}

    for parola in parole:
        if parola:   # questo controllo è uguale a dire << if parola != "" >> evito di provare a prendere la prima lettera da una stringa vuota ("")
            iniziale = parola[0].upper()
            if iniziale not in risultato:
                risultato[iniziale] = []

            risultato[iniziale] += [parola]
    
    return risultato

parole = ["albero", "Auto", "banana", "barca", "cane", "Casa", "dado", "delfino", ""]
print(raggruppa_per_iniziale(parole))
        