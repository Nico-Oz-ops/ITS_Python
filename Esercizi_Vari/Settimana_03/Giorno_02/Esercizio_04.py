'''
Tema: map, filter, reduce, lambda
Obiettivo: Combinare trasformazioni e riduzioni funzionali
'''

# Esercizio 04
# Titolo: "Prodotto dei numeri dispari maggiori di 5"

'''
Traccia:
Scrivi una funzione prodotto_dispari_maggiori_di_5(numeri) che, 
data una lista di numeri interi, restituisce il prodotto di tutti i numeri che sono:

* dispari
* maggiori di 5

Usa solo funzioni funzionali: filter, reduce e lambda.

Suggerimento:

* Usa filter per tenere solo i numeri dispari maggiori di 5
* Usa reduce per moltiplicarli tutti insieme
* Ricorda di importare reduce da functools
* Se non ci sono numeri validi, puoi restituire 1 (identità della moltiplicazione)
'''
from functools import reduce

def prodotto_dispari_maggiori_di_5(numeri: list[int]) -> int:

    dispari = filter(lambda x: x % 2 == 1 and x > 5, numeri)

    return reduce(lambda acc, x: acc * x, dispari, 1)

print(prodotto_dispari_maggiori_di_5([1, 5, 3, 2, 4, 6, 7, 9, 11]))






