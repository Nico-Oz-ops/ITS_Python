'''
Tema: Matrici
Obiettivo: Calcolare la somma della diagonale principale e della diagonale secondaria.

Nome: somma_diagonali

Traccia:
Scrivi una funzione che, data una matrice quadrata (stesso numero di righe e colonne), 
ritorni una tupla (somma_principale, somma_secondaria) dove:

* somma_principale è la somma degli elementi matrice[i][i] (da in alto a sinistra a in basso a destra).
* somma_secondaria è la somma degli elementi matrice[i][n-1-i] (da in alto a destra a in basso a sinistra).

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def somma_diagonali(matrice: list[list[int]]) -> tuple[int, int]:
    n = len(matrice)
    somma_principale = sum(matrice[i][i] for i in range(n))
    somma_secondaria = sum(matrice[i][n - i - 1] for i in range(n))

    return ((somma_principale, somma_secondaria))

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonali(matrice))

# Alternativa 2
def somma_diagonali(matrice: list[list[int]]) -> tuple[int, int]:
    n = len(matrice)

    somma_principale = 0
    somma_secondaria = 0
    for i in range(n):
        somma_principale += matrice[i][i]
        somma_secondaria += matrice[i][n - i - 1]
    
    return (somma_principale, somma_secondaria)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonali(matrice)) 
    



