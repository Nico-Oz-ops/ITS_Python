'''
Tema: Liste e condizioni
Obiettivo: Ripassare cicli e filtri con liste.

Nome dell’esercizio: numeri_negativi

Traccia:
Scrivi una funzione che, data una lista di numeri interi, ritorni una nuova lista 
contenente solo i numeri negativi.

Esempio:
numeri = [5, -3, 0, -10, 7]  
→ risultato = [-3, -10]

Suggerimento: Puoi usare una list comprehension o un ciclo for con if.
'''
def numeri_negativi(numeri: list[int]) -> list[int]:
    return [numero for numero in numeri if numero < 0]

numeri = [5, -3, 0, -10, 7]  
print(numeri_negativi(numeri))
