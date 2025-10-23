'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere una matrice ed elaborarne i valori.

Nome dell’esercizio: somma_elementi_matrice

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
ritorni la somma di tutti i suoi elementi.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ somma = 45
'''
# Alternativa 1 - senza uso di built-in
def somma_elementi_matrice(matrice: list[list[int]]) -> int:
    somma_tot = 0

    for riga in matrice:
        somma_riga = 0
        for elemento in riga:
            somma_riga += elemento
        somma_tot += somma_riga
    
    return somma_tot

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_elementi_matrice(matrice))

# Alternativa 2 - comprehension + sum()
def somma_elementi_matrice(matrice: list[list[int]]) -> int:
    return sum(sum(riga) for riga in matrice)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_elementi_matrice(matrice))


# Alternativa Lisa
def somma_elementi_matrice(matrice: list[list[int]]) -> int:
    somma = 0
    for sottolista in matrice:
        for num in sottolista:
            somma += num 
    return somma

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_elementi_matrice(matrice))