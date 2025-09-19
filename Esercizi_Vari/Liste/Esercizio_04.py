'''
Esercizio 4

Tema: Liste e somma condizionale
Obiettivo: Filtrare e sommare con funzioni built-in

Nome dell’esercizio: Somma numeri pari

Traccia:
Scrivi una funzione somma_pari(lista) che sommi tutti i numeri pari presenti in una lista.

Esempio:

somma_pari([1, 2, 3, 4, 5, 6])
# Output: 12
'''

# Alternativa 1
def somma_pari(numeri: list[int]):
    somma = 0

    for numero in numeri:
        if numero % 2 == 0:
            somma += numero
    
    return somma

numeri = [1, 2, 3, 4, 5, 6]
print(somma_pari(numeri))

# Alternativa 2
def somma_pari(numeri: list[int]):
    return sum(filter(lambda numero: numero % 2 == 0, numeri))

numeri = [1, 2, 3, 4, 5, 6]
print(somma_pari(numeri))

# Alternativa 3
def somma_pari(numeri: list[int]):
    return sum(numero for numero in numeri if numero % 2 == 0)

numeri = [1, 2, 3, 4, 5, 6]
print(somma_pari(numeri))