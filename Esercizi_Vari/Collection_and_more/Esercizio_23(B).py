'''
Tema: Matrici (liste di liste)
Obiettivo: Scorrere le colonne di una matrice

Nome dell’esercizio: Massimo di una colonna

Traccia:
Scrivi una funzione massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int 
che prende una matrice di numeri e un indice di colonna, e restituisce il valore massimo di quella colonna.

Suggerimento:
Per scorrere una colonna, fissa l’indice e prendi da ogni riga l’elemento corrispondente.
'''
# Alternativa 1
def massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int:
    return max(riga[indice_colonna] for riga in matrice)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(massimo_colonna(matrice, 1))

# Alternativa 2
def massimo_colonna(matrice: list[list[int]], indice_colonna: int) -> int:
    massimo = matrice[0][indice_colonna] # prendo il primo valore della colonna come base

    for riga in matrice:
        valore = riga[indice_colonna]   # prendo l'elemento della colonna in questa riga
        if valore > massimo: # confronto con il massimo attuale
            massimo = valore # aggiorno se è più grande
    
    return massimo

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(massimo_colonna(matrice, 0))