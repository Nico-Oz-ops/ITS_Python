# Esercizio 04
'''
Somma delle Diagonali di una Matrice (Quadrata o Rettangolare)

Data una matrice 2D (lista di liste) di interi con dimensioni n X n, scrivi due funzioni:

1. sum_primary_diagonal(matrix) che restituisce la somma della “diagonale
primaria” (dall’angolo in alto a sinistra verso il basso a destra).

2. sum_secondary_diagonal(matrix) che restituisce la somma della “diagonale
secondaria” (dall’angolo in alto a destra verso il basso a sinistra).

Requisiti:

● Entrambe le funzioni accettano una lista di liste.
● Restituisci un intero per ciascuna funzione.

Esempi:

mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

sum_primary_diagonal(mat1) # restituisce 1 + 5 + 9 = 15
sum_secondary_diagonal(mat1) # restituisce 3 + 5 + 7 = 15
'''

def sum_primary_diagonal(matrix: list[list[int]]) -> int:

    righe = len(matrix) # conta quante righe ha la matrice
    colonne = len(matrix[0]) if righe > 0 else 0 # conta quante colonne ha la matrice se ha almeno una riga

    somma = 0

    for i in range(min(righe, colonne)): # serve a non uscire dai bordi della matrice
        j = i # per la diagonale principale, riga e colonna sono uguali
        somma += matrix[i][j]
    
    return somma

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:

    righe = len(matrix)
    colonne = len(matrix[0]) if righe > 0 else 0

    somma = 0

    for i in range(min(righe, colonne)):
        j = colonne - 1 - i # dà l’indice della colonna che si muove da destra verso sinistra mentre "i" cresce.
        somma += matrix[i][j]
    
    return somma


mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print("Matrice 1")
print(f"Diagonale primaria: {sum_primary_diagonal(mat1)}")
print(f"Diagonale secondaria: {sum_secondary_diagonal(mat1)}\n") 

mat2 = [
    [1, 2],
    [4, 5],
    [6, 7]
]
print("Matrice 2")
print(f"Diagonale primaria: {sum_primary_diagonal(mat2)}")
print(f"Diagonale primaria: {sum_secondary_diagonal(mat2)}\n")

mat3 = [
    [1, 2, 3],
    [4, 5, 6],
]
print("Matrice 3")
print(f"Diagonale primaria: {sum_primary_diagonal(mat3)}")
print(f"Diagonale primaria: {sum_secondary_diagonal(mat3)}")