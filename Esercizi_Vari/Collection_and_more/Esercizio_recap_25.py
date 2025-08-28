'''
Tema: Matrici (liste di liste)
Obiettivo: Allenarti con gli indici.

Nome: Somma diagonale principale

Traccia:
Scrivi una funzione somma_diagonale(matrice) che, data una matrice quadrata, 
ritorni la somma degli elementi della diagonale principale.

Input:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def somma_diagonale_principale(matrice: list[list[int]]) -> int:
    n = len(matrice)
    
    somma = 0
    for i in range(n):
        somma += matrice[i][i]
    
    return somma 

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonale_principale(matrice))

# Alternativa 2
def somma_diagonale_principale(matrice: list[list[int]]) -> int:
    n = len(matrice)

    return sum(matrice[i][i] for i in range(n))

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonale_principale(matrice))