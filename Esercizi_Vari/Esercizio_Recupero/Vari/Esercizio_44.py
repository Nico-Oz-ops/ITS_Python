'''
Filtra e trasforma numeri

Scrivi una funzione con il seguente header:

filter_and_square(nums: list[int], soglia: int) -> list[int]

che prenda una lista di interi e un valore di soglia, e restituisca una nuova lista
contenente i quadrati (n**2) di tutti i numeri di nums che sono maggiori di soglia e pari
'''

def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    return [num ** 2 for num in nums if num >= soglia and num % 2 == 0]

numeri = [1, 8, 6, 3, 2, 12, 14, 15, 19]
soglia = 7
print(filter_and_square(numeri, soglia))