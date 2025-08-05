'''
Tema: reduce e trasformazione progressiva
Obiettivo: Calcolare un valore aggregato da una lista
'''

# Esercizio 03
# Titolo: "Somma dei quadrati (con reduce)"

'''
Traccia:
Scrivi una funzione somma_quadrati(numeri) che prende in input una lista di 
numeri interi e restituisce la somma dei quadrati di tutti i numeri presenti, 
utilizzando la funzione reduce dal modulo functools.

Suggerimento:

Importa reduce così:
from functools import reduce

La funzione reduce(f, iterable) applica la funzione f cumulativamente sugli elementi:
f(f(f(x1, x2), x3), x4) ...
'''
from functools import reduce

def somma_quadrati(numeri: list[int]) -> int:
    return reduce(lambda acc, x: acc + x ** 2, numeri, 0)

print(somma_quadrati([1, 2, 3, 4]))
