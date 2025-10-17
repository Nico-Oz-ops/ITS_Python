'''
Esercizio - Group Orders by Customer

Tema: Raggruppamento e somma di valori in una lista di dizionari

Obiettivo: Calcolare il totale speso da ciascun cliente sommando più ordini

Nome dell’esercizio: Group Orders by Customer

Traccia:
Scrivi una funzione chiamata group_orders_by_customer che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta un ordine e contiene le chiavi "cliente" e "totale".

La funzione deve restituire un dizionario in cui le chiavi sono i nomi dei clienti e i valori sono la 
somma totale dei loro ordini.

Esempio di input:

[
    {"cliente": "Anna", "totale": 20.0},
    {"cliente": "Marco", "totale": 35.5},
    {"cliente": "Anna", "totale": 15.0}
]

Esempio di output:

{"Anna": 35.0, "Marco": 35.5}
'''
def group_orders_by_customer(ordini: list[dict[str, float]]) -> dict[str, float]:
    risultato = {}
    
    for ordine in ordini:
        cliente = ordine["cliente"]
        totale = ordine["totale"]

        if cliente in risultato:
            risultato[cliente] += totale
        else:
            risultato[cliente] = totale
    
    return risultato

ordini = [
    {"cliente": "Anna", "totale": 20.0},
    {"cliente": "Marco", "totale": 35.5},
    {"cliente": "Anna", "totale": 15.0}
]

print(group_orders_by_customer(ordini))