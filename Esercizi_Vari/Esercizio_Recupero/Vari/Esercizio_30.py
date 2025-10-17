'''
Esercizio - Filter and Summarize Sales

Tema: Filtraggio condizionale e formattazione dei risultati

Obiettivo: Mostrare solo i clienti con vendite sopra una certa soglia

Nome dell’esercizio: Filter and Summarize Sales

Traccia:
Scrivi una funzione chiamata filter_and_summarize_sales che riceve una lista di dizionari 
con le chiavi "cliente" e "totale", e un numero soglia.

La funzione deve:

* Considerare solo gli ordini con totale maggiore o uguale alla soglia.
* Restituire una stringa formattata come "cliente: €totale", separando i risultati con una virgola.

Esempio di input:

ordini = [
    {"cliente": "Anna", "totale": 25.0},
    {"cliente": "Marco", "totale": 10.0},
    {"cliente": "Luca", "totale": 40.0}
]
soglia = 20


Esempio di output:

Anna: €25.0, Luca: €40.0
'''

def filter_and_summarize_sales(ordini: list[dict[str, float]], soglia: int) -> str:

    filtro = [f"{ordine['cliente']}: €{ordine['totale']}" for ordine in ordini if ordine['totale'] >= soglia]
    return ", ".join(filtro)

ordini = [
    {"cliente": "Anna", "totale": 25.0},
    {"cliente": "Marco", "totale": 10.0},
    {"cliente": "Luca", "totale": 40.0}
]
soglia = 20

print(filter_and_summarize_sales(ordini, soglia))