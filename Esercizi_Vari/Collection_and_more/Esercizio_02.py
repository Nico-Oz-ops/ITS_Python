'''
Esercizio 2 - Filtra solo le parole che compaiono una sola volta
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

# Opzione 1
def elementi_unici_assoluti(parole: list[str]) -> list[str]:

    conteggio = {}
    for parola in parole:
        if parola not in conteggio:
            conteggio[parola] = 1
        
        else:
            conteggio[parola] += 1
    
    risultato = []
    for parola in conteggio:
        if conteggio[parola] == 1:
            risultato.append(parola)
    
    return risultato

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))

# Opzione 2
def elementi_unici_assoluti(parole: list[str]) -> list[str]:
    conteggio = {}
    for parola in parole:
        if parola not in conteggio:
            conteggio[parola] = 1
        
        else:
            conteggio[parola] += 1
    
    # Uso filter con una lambda che prende una parola e restituisce True solo se la parola è apparsa una volta nel conteggio
    # e alla fine, si converte il filtro in lista per ottenere il risultato
    return list(filter(lambda parola: conteggio[parola] == 1, parole))

parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
print(elementi_unici_assoluti(parole))


