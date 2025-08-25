'''
Tema: Dizionari - Conteggio
Obiettivo: Calcolare frequenze di elementi in una lista.

Nome dell’esercizio: Conteggio delle vocali

Traccia:
Scrivi una funzione conteggia_vocali(parole: list[str]) -> dict[str, int] che, 
data una lista di parole, ritorni un dizionario in cui le chiavi sono le vocali 
(a, e, i, o, u) e i valori sono il numero di volte che ciascuna vocale compare in tutte le parole della lista.

Se una vocale non compare mai, non deve comparire nel dizionario.

Suggerimento:
Puoi scorrere ogni parola, e per ciascun carattere verificare se è una vocale.
'''
def conteggia_vocali(parole: list[str]) -> dict[str, int]:
    risultato = {}

    for parola in parole:
        for car in parola:
            if car.lower() in "aeiou":
                if car.lower() not in risultato:
                    risultato[car.lower()] = 0
                risultato[car.lower()] += 1
    return risultato

parole = ["cane", "gAtto", "sole", "luna", "amico", "io", "tu", "computer", "i"]
print(conteggia_vocali(parole))



