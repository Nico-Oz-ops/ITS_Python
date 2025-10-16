'''
Nome dell’esercizio: filter_and_upper

Traccia:
Scrivi una funzione chiamata filter_and_upper che prende in input:

* words: lista di stringhe
* min_len: intero che rappresenta la lunghezza minima

La funzione deve:

* Filtrare tutte le stringhe nella lista la cui lunghezza è maggiore o uguale a min_len.
* Convertire tutte le stringhe filtrate in maiuscolo.
* Restituire una stringa unica con le parole filtrate concatenate, separate da uno spazio " "
'''
def filter_and_upper(words: list[str], min_len: int) -> str:
    if not words:
        raise ValueError("Lista vuota")
    
    return " ".join(parola.upper() for parola in words if len(parola) >= min_len)

parole = ["casa", "almacen", "montagna", "elicottero", "topo"]
valore = 5

print(filter_and_upper(parole, valore))
