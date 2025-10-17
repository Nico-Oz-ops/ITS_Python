'''
Tema: Aggregazione e formattazione di dati in dizionari

Obiettivo: Riassumere informazioni numeriche e restituirle in formato testuale

Nome dell’esercizio: Summarize Orders

Traccia:
Scrivi una funzione chiamata summarize_orders che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta un ordine e contiene le chiavi "cliente" e "totale".

La funzione deve restituire una stringa in cui, per ogni cliente, compare il totale speso formattato come:
nome_cliente: €totale

Gli elementi devono essere separati da una virgola.

Esempio di input:

[
    {"cliente": "Anna", "totale": 35.5},
    {"cliente": "Marco", "totale": 42.0},
    {"cliente": "Luca", "totale": 15.75}
]

Esempio di output:

Anna: €35.5, Marco: €42.0, Luca: €15.75
'''

def summarize_orders(ordini: list[dict[str, float]]) -> str:
    filtro = [f"{ordine['cliente']}: €{ordine['totale']}" for ordine in ordini]
    return ", ".join(filtro)

ordini = [
    {"cliente": "Anna", "totale": 35.5},
    {"cliente": "Marco", "totale": 42.0},
    {"cliente": "Luca", "totale": 15.75}
]

print(summarize_orders(ordini))