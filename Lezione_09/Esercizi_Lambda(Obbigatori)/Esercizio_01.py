# Esercizio 1
'''
Scrivi una funzione lambda che prenda un 
numero intero e ritorni il suo quadrato.
'''

from typing import Callable

quadrato:Callable[[int], int] = lambda x: x ** 2
print(quadrato(5))

def square(x:int):
    return x ** 2

print(square(5))