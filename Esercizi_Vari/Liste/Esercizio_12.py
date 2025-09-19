'''
Esercizio 7 - Liste annidate

Tema: Liste di liste
Obiettivo: Sommare elementi annidati

Traccia:
Scrivi una funzione che, data una lista di liste di numeri, ritorni la somma totale di tutti i numeri.
'''
# Alternativa 1
def somma_annidata(numeri: list[list[int]]):
    return sum(sum(elemento for elemento in sottolista) for sottolista in numeri)

numeri = [[1, 2], [3, 4], [5]]
print(somma_annidata(numeri))


# Alternativa 2
def somma_annidata(numeri: list[list[int]]):
    somma = 0

    for sottolista in numeri:
        somma_elementi = 0
        for numero in sottolista:
            somma_elementi += numero
        somma += somma_elementi
    
    return somma

print(somma_annidata(numeri))