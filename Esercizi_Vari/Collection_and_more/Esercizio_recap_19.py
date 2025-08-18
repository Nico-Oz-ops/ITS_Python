'''
Tema: Matrici
Obiettivo: Calcolare la somma di ogni colonna.

Nome: somma_per_colonna

Traccia:
Scrivi una funzione che, data una matrice, ritorni una lista con la somma di ciascuna colonna.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def somma_per_colonna(matrice: list[list[int]]) -> list[int]:
    return [sum(riga[colonna] for riga in matrice) for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_colonna(matrice))

# Alternativa 2
def somma_per_colonna(matrice: list[list[int]]) -> list[int]:
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        somma = 0
        for riga in matrice:
            somma += riga[colonna]
        
        risultato.append(somma)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_colonna(matrice))
