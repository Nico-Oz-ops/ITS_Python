'''
Scrivi una funzione chiamata double_and_filter che prende:
    * una lista di numeri interi nums
    * un valore massimo max_val (intero)

La funzione deve:
    * Moltiplicare ogni numero della lista per 2.
    * Filtrare solo i numeri doppiati che sono minori o uguali a max_val.
    * Restituire una stringa con questi numeri, separati da uno spazio (" "), nell’ordine originale
'''

def double_and_filter(nums: list[int], max_val: int) -> str:
    filtro = [str(num * 2) for num in nums if num * 2 <= max_val]
    return " ".join(filtro)

numeri = [4, 2, 3]
valore = 10

print(double_and_filter(numeri, valore))
