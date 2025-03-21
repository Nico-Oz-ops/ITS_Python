# Esercizio 8.16 - 

'''importa il modulo intero printing_functions. Per utilizzare una funzione
all'interno di printing_functions.py si dovrà usare il prefisso printing_functions
seguito dal nome della funzione... printing_functions.subtraction()'''
import printing_functions
printing_functions.subtraction(2, 9)
print("-" * 50)

'''si importa direttamente la funzione subtraction dal modulo printing_functions.
Quindi si chiama la funzione direttamente nel codice senza dover usare il prefisso del modulo
subtraction()'''
from printing_functions import subtraction
print(subtraction(3, 2))
print("-" * 50)

'''importa la funzione subtraction dal modulo printing_function, ma la rinomino "sot"
Quindi al posto di usare subtraction(), userò sot()'''
from printing_functions import subtraction as sot
print(sot(7, 2))
print("-" * 50)

'''si importa l'intero modulo printing_functions, ma si rinomina come "pf".
Quindi per usare la funzione dal modulo, dovrò chiamarla con il prefisso pf, pf.subtraction()'''
import printing_functions as pf
print(pf.subtraction(15, 3))
print("-" * 50)
'''questo import trae tutte le funzioni e variabili dal modulo printing_functions.
Si può chiamare direttamente qualsiasi funzione o variabile di printing_functions senza 
usare un prefisso'''
from printing_functions import * 

print(subtraction(15, 6))
print(somma(2, 9))

