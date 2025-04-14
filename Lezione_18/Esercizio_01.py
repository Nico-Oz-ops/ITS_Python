# Esercizio 1
'''
Radice quadrata sicura: scrivi una funzione safe_sqrt(number)che calcola la 
radice quadrata di un numero usando math.sqrt(). 
Gestisci ValueError se l'input è negativo restituendo un messaggio informativo.
'''

import math

def safe_sqrt(number:int) -> float:

    try:
        num_sqrt = math.sqrt(number)
        return num_sqrt
    
    except ValueError:
        return"Per favore inserire un valore valido"

print(safe_sqrt(-2))
print(f"{safe_sqrt(10):.3f}")
print(safe_sqrt(0))

