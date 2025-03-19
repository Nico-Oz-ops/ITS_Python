# Esercizio 01 - Calcolo cateto

import math

a = int(input("Inserire un numero intero: "))
b = int(input("Inserire un numero intero: "))

if a > b:
    c = math.sqrt((a ** 2) - (b ** 2)) # calcolo di cateto "c"
    print(f"Il cateto è: {c:.3f}")
else:
    print("Errore!")