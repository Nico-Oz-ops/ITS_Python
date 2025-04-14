# Esercizio 05
'''
Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.
'''
def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    if len(x) != len(y):
        raise ValueError("Le liste devono essere della stessa lunghezza")
    
    somma = []
    for i in range(len(x)):
        somma.append(x[i] + y[i])
    
    return somma 

print(somma_elementi([1,1,1],[1,1,1]))




