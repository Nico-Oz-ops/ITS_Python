# Esercizio 01
'''
Scrivere in Python una funzione recursivePower che calcola la 
potenza di un numero utilizzando la ricorsione. 
La funzione deve ricevere due parametri in input:

base: il numero da elevare a potenza.
exponent: l’esponente a cui elevare la base.
'''

def recursivePower(a:int, b:int) -> int:
    if a == 0 and b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return int(a * recursivePower(a, b - 1))

print(f"3 elevato alla potenza di 4: {recursivePower(3, 4)}")
print(f"4 elevato alla potenza di 3: {recursivePower(4, 3)}")
print(f"2 elevato alla potenza di 5: {recursivePower(2, 5)}")
print(f"5 elevato alla potenza di 2: {recursivePower(5, 2)}")




x = 3.5 ** 4
print(x)
