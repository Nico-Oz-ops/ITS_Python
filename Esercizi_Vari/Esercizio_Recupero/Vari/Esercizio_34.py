'''
Tema: Liste, conteggi, filter, lambda

Obiettivo: Isolare gli elementi unici in una lista (quelli che compaiono esattamente una volta)

Nome dell’esercizio: elementi_unici_assoluti

Traccia:
Scrivi una funzione che prende una lista di parole e restituisce una nuova lista 
contenente solo le parole che appaiono una sola volta, nell’ordine originale.

# Esempio:
parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]

# Output atteso:
["mondo", "codice", "logica"]

Suggerimento:
Puoi usare un dizionario per contare le occorrenze, e poi usare filter con lambda per tenere solo quelle con count == 1.
'''
# Alternativa 1
def elementi_unici_assoluti(parole: list[str]) -> list[str]:
    occorrenze = {}
    unici = []

    for parola in parole:
        if parola not in occorrenze:
            occorrenze[parola] = 0
        
        occorrenze[parola] += 1
    
    for parola in occorrenze:
        if occorrenze[parola] == 1:
            unici.append(parola)
    
    return unici

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))

# Alternativa 2
def elementi_unici_assoluti(parole: list[str]) -> list[str]:
    occorrenze = {}

    for parola in parole:
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
    
    return list(filter(lambda parola: occorrenze[parola] == 1, parole))

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))

# Alternativa 3
def elementi_unici_assoluti(parole: list[str]) -> list[str]:
    return list(filter(lambda parola: parole.count(parola) == 1, parole))

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))