'''
Tema: Dizionari - Conteggio di caratteri
Obiettivo: Creare un dizionario che conti quante volte compare ogni lettera in una stringa.

Nome dell’esercizio: Conteggio lettere

Traccia:
Scrivi una funzione conteggio_lettere(testo: str) -> dict[str, int] che, 
data una stringa, ritorni un dizionario in cui le chiavi sono le lettere presenti e 
i valori il numero di volte che compaiono.

Non considerare spazi o altri caratteri non alfabetici.

Input:
testo = "Python è fantastico"

Suggerimento:
Puoi scorrere ogni carattere della stringa, trasformarlo in minuscolo e aggiornare il conteggio nel dizionario.
'''
def conteggio_lettere(testo: str) -> dict[str, int]:
    risultato = {}

    for car in testo:
        if car.isalpha():
            if car.lower() not in risultato:
                risultato[car.lower()] = 0
            risultato[car.lower()] += 1

    return risultato

testo = "Python è fantastico"
print(conteggio_lettere(testo))


