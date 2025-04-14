# Esercizio 03
'''
Uso con filter()
Hai la seguente lista numeri = [5, 12, 17, 18, 24, 32]. 
Usa filter() con una lambda per ottenere solo i numeri pari.
'''

from typing import Callable

numeri = [5, 12, 17, 18, 24, 32]

pari:Callable[[int], int] = list(filter(lambda num: num % 2 == 0, numeri))
print(pari)

print("-" * 50)

def pari(numeri:list[int]):
    numeri_pari = []
    for numero in numeri:
        if numero % 2 == 0:
            numeri_pari.append(numero)
    return numeri_pari

numeri = [5, 12, 17, 18, 24, 32]
print(pari(numeri))

print("-" * 50)

pari = [x for x in numeri if x % 2 == 0]
print(pari)