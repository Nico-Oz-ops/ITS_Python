'''
Tema: Matrici quadrate
Obiettivo: Lavorare con indici riga/colonna specifici

Nome: Somma diagonali

Traccia:
Scrivi una funzione somma_diagonali(matrice: list[list[int]]) -> tuple[int, int] che restituisca una tupla con:

* Somma della diagonale principale (dall’alto a sinistra al basso a destra)
* Somma della diagonale secondaria (dall’alto a destra al basso a sinistra)

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output atteso
(15, 15)  # diagonale principale: 1+5+9=15, diagonale secondaria: 3+5+7=15
'''
# Alternativa 1
def somma_diagonali(matrice: list[list[int]]) -> tuple[int, int]:
    somma_principale = 0
    n = len(matrice)

    for i in range(n):
        somma_principale += matrice[i][i]
    
    somma_secondaria = 0
    for i in range(n):
        somma_secondaria += matrice[i][n - i - 1]
    
    return (somma_principale, somma_secondaria)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonali(matrice))

# Altertnativa 2
def somma_diagonali(matrice: list[list[int]]) -> tuple[int, int]:
    n = len(matrice)

    somma_principale = sum(matrice[i][i] for i in range(n))
    somma_secondaria = sum(matrice[i][n - i - 1] for i in range(n))

    return (somma_principale, somma_secondaria)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_diagonali(matrice))