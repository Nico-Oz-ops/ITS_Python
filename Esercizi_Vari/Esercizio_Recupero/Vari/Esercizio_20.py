'''
calculate_weighted_sum

Scrivi una funzione chiamata

* calculate_weighted_sum(values: list[float], weights: list[float]) -> float

che calcoli la somma ponderata dei valori nella lista values, moltiplicando ogni valore per il peso 
corrispondente nella lista weights, e poi sommando tutti i risultati.

Regole:

Le due liste devono avere la stessa lunghezza.
Se una delle liste è vuota, solleva un ValueError("liste vuote").
Se le lunghezze non coincidono, solleva un ValueError("liste di lunghezza diversa").
'''

def calculate_weighted_sum(values: list[float], weights: list[float]) -> float:

    if not values or not weights:
        raise ValueError("Lista vuota")
    if len(values) != len(weights):
        raise ValueError("Liste di lunghezza diversa")

    somma_pon = 0.0
    for i in range(len(values)):
        somma_pon += values[i] * weights[i]

    return somma_pon

valori = [70, 80, 90]
pesi = [0.2, 0.3, 0.5]

print(calculate_weighted_sum(valori, pesi))

    
