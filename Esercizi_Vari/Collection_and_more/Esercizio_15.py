'''
Tema: Liste e funzioni filter/map - Trasformazione e filtraggio di elementi
Obiettivo: Dato un elenco di numeri, restituire una nuova lista contenente solo i quadrati dei numeri pari.

Nome dell’esercizio: quadrati_dei_pari

Traccia:
Scrivi una funzione che prenda una lista di numeri interi e restituisca una lista 
con i quadrati dei numeri pari presenti nella lista originale.

Input:
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Suggerimento: puoi usare filter() per selezionare i numeri pari e map() 
per calcolarne il quadrato, oppure una list comprehension.
'''

# Alternativa 1
def quadrati_dei_pari(numeri: list[int]) -> list[int]:
    quadrati = []

    for numero in numeri:
        if numero % 2 == 0:
            quadrati.append(numero ** 2)
    
    return quadrati

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quadrati_dei_pari(numeri))

# Alternativa 2
def quadrati_dei_pari(numeri: list[int]) -> list[int]:
    pari = filter(lambda numero: numero % 2 == 0, numeri)
    return list(map(lambda numero: numero ** 2, pari))

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quadrati_dei_pari(numeri))