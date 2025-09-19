'''
Esercizio 3 - Minimo e massimo

Tema: Analisi di lista
Obiettivo: Trovare gli estremi

Traccia:
Scrivi una funzione che ritorni il valore minimo e massimo in una lista di numeri senza usare le funzioni min() e max().
'''

# Alternativa 1
def minimo_massimo(numeri: list[int]):
    if not numeri:
        return None, None
    
    minimo = numeri[0]
    massimo = numeri[0]

    for numero in numeri:
        if numero > massimo:
            massimo = numero
        
        if numero < minimo:
            minimo = numero
    
    return minimo, massimo

numeri = [4, 8, 15, 9, 10]
print(minimo_massimo(numeri))

# Alternativa 2
def minimo_massimo(numeri: list[int]):
    minimo = min(numero for numero in numeri)
    massimo = max(numero for numero in numeri)
    
    return minimo, massimo

print(minimo_massimo(numeri))