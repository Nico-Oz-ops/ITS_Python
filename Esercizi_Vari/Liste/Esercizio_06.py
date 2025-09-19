'''
Esercizio 1 - Somma e prodotto

Tema: Operazioni base su liste
Obiettivo: Sommare tutti gli elementi di una lista e calcolare il prodotto

Traccia:

Scrivi una funzione che, data una lista di numeri interi, ritorni la somma e il prodotto di tutti gli elementi.
Suggerimento: Usa un ciclo for o le funzioni sum() e reduce().
'''
from functools import reduce

# Alternativa 1
def somma_prodotto(numeri: list[int]):
    somma = sum(numeri)
    prodotto = reduce(lambda a, b: a * b, numeri)

    return somma, prodotto

numeri = [1, 2, 3, 4, 5]
print(somma_prodotto(numeri))

#Alternativa 2
def somma_prodotto(numeri: list[int]):
    somma = 0
    prodotto = 1

    for numero in numeri:
        somma += numero
        prodotto *= numero
    
    return somma, prodotto

numeri = [1, 2, 3, 4, 5]
print(somma_prodotto(numeri))