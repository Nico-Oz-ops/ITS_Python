# Esercizio 9
'''
Una progressione armonica è definita come il prodotto dei reciproci dei primi n numeri interi positivi, 
ovvero il risultato della moltiplicazione di 1 diviso ogni numero intero da 1 fino a n.
Ad esempio, se n = 6, la progressione armonica A vale:
A = 1/6 * 1/5 * 1/4 * 1/3 * 1/2 * 1 = 0.001389.

Scrivere in Python una funzione ricorsiva chiamata armonica che dato un numero n intero positivo, 
calcoli la relativa progressione armonica, arrotondando il risultato finale a 6 cifre decimali.
'''

def recursiveArmonica(n:int) -> float:
    if n == 1:
        return 1
    else:
        return round(1 / n * recursiveArmonica(n - 1), 6)

print(f"Se n = 6, la progressione armonica è uguale a: {recursiveArmonica(6)}")
print(f"Se n = 3, la progressione armonica è uguale a: {recursiveArmonica(3)}")
print(f"Se n = 9, la progressione armonica è uguale a: {recursiveArmonica(9)}")