'''
Tema: Matrici (liste di liste)
Obiettivo: Scorrere le colonne di una matrice

Nome dell’esercizio: Massimo di una colonna

Traccia:
Scrivi una funzione massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int 
che prende una matrice di numeri e un indice di colonna, e restituisce il valore massimo di quella colonna.

Suggerimento:
* Per scorrere una colonna, fissa l’indice e prendi da ogni riga l’elemento corrispondente.
* Non utilizzare funzioni built-in
'''

# Alternativa 1 - senza uso di built-in
def massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int:
    massimo = matrice[0][indice_colonna]

    for riga in matrice:
        valore = riga[indice_colonna]
        if valore > massimo:
            massimo = valore
    
    return massimo

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
indice_colonna = 1
print(massimo_colonna(matrice, indice_colonna))


# Alternativa 2
def massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int:
    return max([riga[indice_colonna] for riga in matrice])

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
indice_colonna = 1
print(massimo_colonna(matrice, indice_colonna))