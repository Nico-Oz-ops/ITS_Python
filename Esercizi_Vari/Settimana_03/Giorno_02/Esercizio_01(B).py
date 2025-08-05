'''
Tema: map, filter, lambda
Obiettivo: Applicare trasformazione e filtraggio funzionale
'''

# Esercizio 01-B
# Titolo: "Cubi dei numeri pari (con map e filter)"

'''
Traccia:
Scrivi una funzione cubi_pari(numeri) che prende una lista di interi e 
restituisce una nuova lista contenente i cubi dei soli numeri pari, utilizzando le funzioni filter() e map().

Non usare cicli for né list comprehension. Usa solo filter, map e lambda!!!

Suggerimento:

* Usa filter(lambda x: x % 2 == 0, numeri) per ottenere i pari
* Poi map(lambda x: x ** 3, ...) per trasformarli in cubi
* Infine racchiudi tutto in list(...) per ottenere il risultato finale
'''

def cubi_pari(numeri: list[int]) -> list[int]:

    num_pari = filter(lambda x: x % 2 == 0, numeri)
    num_cubi = map(lambda x: x ** 3, num_pari)

    return list(num_cubi)

print(cubi_pari([1, 2, 3, 4, 5, 6, 7, 8, 9]))



def cubi_pari(numeri: list[int]) -> list[int]:

    num_cubi = map(lambda x: x** 3, filter(lambda x: x % 2 == 0, numeri))
    return list(num_cubi)

print(cubi_pari([1, 2, 3, 4, 5, 6, 7, 8, 9]))






