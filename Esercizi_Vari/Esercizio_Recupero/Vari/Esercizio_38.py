'''
Tema: Matrici (liste di liste)
Obiettivo: Calcolare i valori minimi delle colonne

Nome dell’esercizio: Minimo per colonna

Traccia:
Scrivi una funzione minimo_per_colonna(matrice: list[list[int]]) -> list[int] che prende una matrice di 
numeri e restituisce una lista contenente il valore minimo di ogni colonna.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Suggerimento:
* Non utilizzare funzioni built-in
'''
# Alternativa 1 - senza uso di built-in
def minimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    lista = []
    num_colonne = len(matrice[0])

    for colonna in range(num_colonne):
        val_minimo = matrice[0][colonna]
        
        for riga in matrice:
            if riga[colonna] < val_minimo:
                val_minimo = riga[colonna]
            
        lista.append(val_minimo)
    
    return lista

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(minimo_per_colonna(matrice))

# Alternativa 2 - comprehension e min()
def minimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    return [min(riga[colonna] for riga in matrice) for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(minimo_per_colonna(matrice))
        
