# Esercizio 06
'''
Uso con reduce()
Usa reduce() (dal modulo functools) e una lambda per calcolare il 
prodotto di tutti gli elementi di una lista numeri = [2, 3, 4].
'''

from functools import reduce

numeri = [2, 3, 4]

prodotto = reduce(lambda x, y: x * y, numeri)
print(prodotto)


def prodotto(numeri:list[int]):
    prodotto = 1
    for num in numeri:
        prodotto *= num
    return prodotto

numeri = [2, 3, 4]
print(prodotto(numeri))