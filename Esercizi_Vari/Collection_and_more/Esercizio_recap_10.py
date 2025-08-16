'''
Tema: Liste e funzioni built-in
Obiettivo: Ripassare uso di any() e condizioni su liste.

Nome dell’esercizio: parole_con_lettera

Traccia:
Scrivi una funzione che, data una lista di parole e una lettera, 
restituisce solo le parole che contengono quella lettera almeno una volta.

Esempio:
parole = ["cane", "gatto", "topo", "mucca"]
lettera = "a"
→ risultato = ["cane", "gatto"]

Suggerimento: Puoi risolverlo con un semplice if lettera in parola, 
oppure provare a usare any() con una condizione sui caratteri.
'''

def parole_con_lettera(parole: list[str], lettera: str) -> list[str]:
    risultato = []

    for parola in parole:
        if lettera in parola:
            risultato.append(parola)
    
    return risultato

parole = ["cane", "gatto", "topo", "mucca"]
lettera = "a"
print(parole_con_lettera(parole, lettera))


def parole_con_lettera(parole: list[str], lettera: str) -> list[str]:
    return [parola for parola in parole if any(carattere == lettera for carattere in parola)]

parole = ["cane", "gatto", "topo", "mucca"]
lettera = "a"
print(parole_con_lettera(parole, lettera))