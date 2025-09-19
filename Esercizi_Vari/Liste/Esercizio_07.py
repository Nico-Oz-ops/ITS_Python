'''
Esercizio 2 - Elementi positivi

Tema: Filtraggio
Obiettivo: Creare una nuova lista con soli elementi positivi

Traccia:

Scrivi una funzione che, data una lista di numeri, ritorni una nuova lista contenente solo i numeri maggiori di 0.

Suggerimento: Prova con list comprehension.
'''
# Alternativa 1
def elementi_positivi(numeri: list[int]):
    return [numero for numero in numeri if numero > 0]

numeri = [0, 1, -7, 3, -5, 5]
print(elementi_positivi(numeri))

#Alternativa 2
def elementi_positivi(numeri: list[int]):
    return list(filter(lambda numero: numero > 0, numeri))

print(elementi_positivi(numeri))

# Alternativa 3
def elementi_positivi(numeri: list[int]):
    positivi = []
    for numero in numeri:
        if numero > 0:
            positivi.append(numero)
    
    return positivi
print(elementi_positivi(numeri))