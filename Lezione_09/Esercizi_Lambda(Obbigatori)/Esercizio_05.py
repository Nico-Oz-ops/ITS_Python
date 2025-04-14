# Esercizio 05
'''
Funzione lambda con if
Crea una funzione lambda che prenda un numero e 
ritorni "pari" se è divisibile per 2, altrimenti "dispari".
'''

from typing import Callable

pari_dispari:Callable[[int], str] = lambda num: "pari" if num % 2 == 0 else "dispari"
print(pari_dispari(2))
print(pari_dispari(5))

print("-" * 50)

def pari_dispari(numero:int):
    if numero % 2 == 0:
        return "pari"
    else:
        return "dispari"

print(pari_dispari(11))
print(pari_dispari(12))


