'''
Esercizio: filter_and_join

Scrivi una funzione chiamata filter_and_join che prende in input:
    * una lista di numeri interi nums
    * un valore minimo min_val (intero)

La funzione deve:
    * Filtrare tutti i numeri nella lista che sono maggiore o uguale a min_val.
    * Convertire i numeri filtrati in stringhe.
    * Restituire una stringa contenente tutti i numeri filtrati concatenati, separati da un punto e virgola ";"
'''
def filter_and_join(nums: list[int], min_val: int) -> str:
    
    return ";".join(str(num) for num in nums if num >= min_val)

numeri = [1, 8, 7, 6, 9, 15]
valore = 6

print(filter_and_join(numeri, valore))
