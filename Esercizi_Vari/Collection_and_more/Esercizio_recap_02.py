'''
Tema: Filter e lambda
Obiettivo: Ripasso di filter + lambda

Nome dell’esercizio: Numeri positivi e pari

Traccia:
Scrivi una funzione filtra_positivi_pari(numeri: list[int]) -> list[int] che 
restituisce una nuova lista contenente solo i numeri positivi e pari della lista di partenza.

Suggerimento:
Usa filter con una lambda.
'''

# Alternativa 1
def filtra_positivi_pari(numeri: list[int]) -> list[int]:
    return list(filter(lambda numero: numero > 0 and numero % 2 == 0, numeri))

numeri = [1, 2, -6, -7, -85, 5, 6, 88, 46]
print(filtra_positivi_pari(numeri))

# Alternativa 2
def filtra_positivi_pari(numeri: list[int]) -> list[int]:
    return [numero for numero in numeri if numero > 0 and numero % 2 == 0]

numeri = [-7, -55, -4, -3, 66, 60, 85, 90, 45]
print(filtra_positivi_pari(numeri))