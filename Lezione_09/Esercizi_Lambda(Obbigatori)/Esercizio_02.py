# Esercizio 02
'''
Somma di due numeri
Crea una funzione lambda che accetti due numeri e 
restituisca la loro somma.
'''

from typing import Callable

somma:Callable[[float, float], float] = lambda a, b: a + b
print(somma(3, 4))

def somma(a:float, b:float):
    return a + b

print(somma(3, 4))