'''
Tema:  Ricorsione numerica con due rami
Obiettivo: Scrivere una funzione ricorsiva per calcolare l’n-esimo numero di Fibonacci.
'''

# Esercizio 02
# Titolo: "Fibonacci"

'''
Traccia
Scrivi una funzione: def fibonacci(n: int) -> int:
che restituisce l’n-esimo numero nella sequenza di Fibonacci, definita così:

* fibonacci(0) = 0
* fibonacci(1) = 1

Per n >= 2: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

Suggerimento:
Servono due casi base:

Se n == 0, ritorna 0
Se n == 1, ritorna 1

Poi si fa la somma delle chiamate ricorsive a fibonacci(n-1) e fibonacci(n-2)
'''

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        return (fibonacci(n - 1)) + (fibonacci(n - 2))

print(fibonacci(5))