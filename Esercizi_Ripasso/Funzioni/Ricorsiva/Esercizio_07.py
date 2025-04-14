# Esercizio 7
'''
Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
'''

def recursiveFactorial(n:int) -> int:

    if n == 1 or n == 0:
        return 1
    
    else:
        return int(n * recursiveFactorial(n - 1))

print(f"5!: {recursiveFactorial(5)}")
print(f"8!: {recursiveFactorial(8)}")
print(f"11!: {recursiveFactorial(11)}")

