'''
Tema: Matrici
Obiettivo: Calcolare massimo e minimo per ogni colonna

Nome dell’esercizio: Massimo e minimo per colonna

Traccia:
Scrivi una funzione min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]] 
che restituisca per ogni colonna una tupla (minimo, massimo).

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output atteso
[(1, 7), (2, 8), (3, 9)]
'''
# Alternativa 1 - senza uso di built-in
def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    lista_nuova = []
    num_colonne = len(matrice[0])

    for colonna in range(num_colonne):
        val_minimo = matrice[0][colonna]
        val_massimo = matrice[0][colonna]

        for riga in matrice:
            if riga[colonna] < val_minimo:
                val_minimo = riga[colonna]
            
            if riga[colonna] > val_massimo:
                val_massimo = riga[colonna]
        
        lista_nuova.append((val_minimo, val_massimo))
    
    return lista_nuova

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(min_max_per_colonna(matrice))

# Alternativa 2 - uso di comprehension + built-in
def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    return [(min(riga[colonna] for riga in matrice), max(riga[colonna] for riga in matrice)) 
            for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(min_max_per_colonna(matrice))