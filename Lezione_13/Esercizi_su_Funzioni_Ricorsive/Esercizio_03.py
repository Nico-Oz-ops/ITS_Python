# Esercizio 3
'''
Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.
'''

def recursiveFactorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * recursiveFactorial(n - 1)

print(f"Il fattoriale di 5 è: {recursiveFactorial(5)}")

# Opzione 2 - calcolo del fattoriale usando un ciclo while

while True:
    num_int = input("Inserire un numero intero positivo: ")
    if num_int.isdigit() and int(num_int) >= 0:
        num_int = int(num_int)
        break
    else:
        print("Errore. Inserire un numero intero e positivo")

if num_int == 0:
    print("Il fattoriale di 0 è 1")

else:
    fattoriale = 1
    i = 1
    while i <= num_int:
        fattoriale *= i
        i += 1

print(f"Il fattoriale di {num_int} è: {fattoriale}")




print( 3 < 4)