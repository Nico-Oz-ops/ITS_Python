# Esercizio 03
'''
Frequenza di Parole Uniche con Normalizzazione

Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.

Requisiti:

● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:

1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).

● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.

● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.

Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}
'''

import string # contiene tutti i simboli di punteggiatura

def count_unique_words(text: str) -> dict:

    tokens = text.split() # si divide il testo in parole (token) sugli spazi, cosi ottengo i token 

    cont_parole = {} # creo un dizionario vuoto in cui si conteranno il numero di volte che si ripete un token o parola

    for token in tokens:

        parola = token.lower().strip(string.punctuation) # si normalizza ogni tokrn rimuovendo punteggiatura e convertendo a minuscolo

        if parola == "":
            continue # si ignora qualsiasi token che diventa una stringa vuota

        # si contano le parole

        if parola in cont_parole:
            cont_parole[parola] += 1
        
        else:
            cont_parole[parola] = 1
    
    return cont_parole

text = "Hello, world! Hello... PYTHON? world."
print(count_unique_words(text))





