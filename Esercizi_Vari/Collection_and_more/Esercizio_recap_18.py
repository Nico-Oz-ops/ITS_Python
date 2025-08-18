'''
Tema: Matrici
Obiettivo: Calcolare la somma di ogni riga.

Nome: somma_per_riga

Traccia:
Scrivi una funzione che, data una matrice, ritorni una lista con la somma di ciascuna riga.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    return [sum(riga) for riga in matrice]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))

# Alternativa 2
def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    risultato = []

    for riga in matrice:
        somma = 0
        for elemento in riga:
            somma += elemento

        risultato.append(somma)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))

# Alternativa 3
def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    risultato = []

    for riga in matrice:
        risultato.append(sum(riga))
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))
