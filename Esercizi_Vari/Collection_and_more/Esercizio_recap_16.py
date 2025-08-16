'''
Tema: Liste e funzioni built-in
Obiettivo: Ripassare l’uso di all() per verificare condizioni.

Nome dell’esercizio: parole_solo_vocali

Traccia:
Scrivi una funzione che, data una lista di parole, restituisca solo quelle composte 
**esclusivamente da vocali** (a, e, i, o, u).

Esempio:
parole = ["aei", "ciao", "uo", "python", "eea"]  
→ risultato = ["aei", "uo", "eea"]

Suggerimento: Usa all(car in "aeiou" for car in parola).
'''
# Alternativa 1
def parole_solo_vocali(parole: list[str]) -> list[str]:
    return [parola for parola in parole if all(carattere in "aeiouAEIOU" for carattere in parola)]

parole = ["aei", "ciao", "uo", "python", "eea"]  
print(parole_solo_vocali(parole))

# Alternativa 2
def parole_solo_vocali(parole: list[str]) -> list[str]:
    risultato = []

    for parola in parole:
        tutti_vocali = True
        for carattere in parola:
            if carattere not in "aeiouAEIOU":
                tutti_vocali = False
                break

        if tutti_vocali:
            risultato.append(parola)

    return risultato
    
parole = ["aei", "ciao", "uo", "python", "eea"]  
print(parole_solo_vocali(parole))


