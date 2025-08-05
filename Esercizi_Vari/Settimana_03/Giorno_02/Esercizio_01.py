'''
Tema: List comprehension
Obiettivo: Trasformazione compatta di una lista
'''

# Esercizio 01
# Titolo: "Numeri pari elevati al cubo"

'''
Traccia:
Scrivi una funzione cubi_pari(lista) che, data una lista di numeri interi, 
restituisce una nuova lista contenente i cubi di quelli che sono pari, usando una list comprehension.

Suggerimento:
Una list comprehension può filtrare e trasformare contemporaneamente:
'''

def cubi_pari(numeri: list[int]) -> list[int]:
    return [num ** 3 for num in numeri if num % 2 == 0]

print(cubi_pari([1, 2, 3, 4, 5, 6, 7, 8, 9]))



