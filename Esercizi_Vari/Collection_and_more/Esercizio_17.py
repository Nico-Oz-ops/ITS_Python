'''
Tema: Riduzione e trasformazione di dati
Obiettivo: Combinare filtraggio, trasformazione e aggregazione in un'unica funzione.

Nome dell’esercizio: Somma dei cubi dei numeri dispari

Traccia:
Scrivi una funzione somma_cubi_dispari(numeri) che:

* Prenda in input una lista di numeri interi.
* Filtri solo i numeri dispari.
* Eleva ciascun numero dispari al cubo.
* Sommi tutti i cubi e restituisca il risultato.

numeri = [1, 2, 3, 4, 5]

Suggerimento: Puoi usare filter → map → reduce oppure un ciclo tradizionale.
'''

from functools import reduce

# Alternativa 1
def somma_cubi_dispari(numeri: list[int]) -> int:

    somma_cubi = 0
    for numero in numeri:
        if numero % 2 == 1:
            somma_cubi += numero ** 3
    
    return somma_cubi

numeri = [1, 2, 3, 4, 5]
print(somma_cubi_dispari(numeri))

# Alternativa 2
def somma_cubi_dispari(numeri: list[int]) -> int:
    num_dispari = filter(lambda numero: numero % 2 == 1, numeri) # con filter() seleziono solo i dispari
    num_dispari_cubi = map(lambda numero: numero ** 3, num_dispari) # con map() elevo al cubo ciascun numero filtrato (num_dispari)

    return reduce(lambda a, b: a + b, num_dispari_cubi, 0) 
# con reduce() sommo i cubi passando due argomenti (una funzione e un iterabile)
# aggiungo 0 perché se l'iterabile num_dispari_cubi fosse vuoto, senza valore iniziale 
# allora mi restituirebbe TypeError

numeri = [1, 2, 3, 4, 5]
print(somma_cubi_dispari(numeri))




