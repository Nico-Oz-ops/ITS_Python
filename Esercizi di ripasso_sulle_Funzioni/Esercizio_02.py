# Esercizio 02
'''
Scrivi una funzione che accetti una lista di numeri e ritorni 
la somma dei numeri che sono divisibili sia per 2 che per 3.
'''

def somma_condizionale(numeri: list[int]) -> int:
    somma = 0
    for numero in numeri:
        if numero % 2 == 0 and numero % 3 == 0:
            somma += numero
    
    return somma

print(somma_condizionale([1, 2, 3, 6, 12]))
print(somma_condizionale([5, 7, 11]))