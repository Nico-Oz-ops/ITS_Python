'''
Esercizio 2

Tema: Liste e riduzione
Obiettivo: Allenarsi con reduce e operazioni matematiche

Nome dell’esercizio: Prodotto degli elementi

Traccia:
Scrivi una funzione prodotto_lista(lista) che calcoli il prodotto di tutti gli 
elementi di una lista di numeri.

Esempio:
prodotto_lista([1, 2, 3, 4])  
# Output: 24
'''
from functools import reduce

# Alternativa 1
def prodotto_lista(prodotti: list[int]):
    return reduce(lambda a, b: a * b, prodotti)

prodotti = prodotto_lista([1, 2, 3, 4])  
print(prodotti)

# Alternativa 2
def prodotto_lista(prodotti: list[int]):
    prodotto = 1

    for elemento in prodotti:
        prodotto *= elemento
    
    return prodotto

prodotti = prodotto_lista([1, 2, 3, 4])  
print(prodotti)