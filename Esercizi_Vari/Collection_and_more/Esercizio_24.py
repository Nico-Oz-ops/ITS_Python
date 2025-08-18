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
Il ragionamento è lo stesso del massimo:

* Calcola il numero di colonne con len(matrice[0]).
* Per ogni colonna, scorri tutte le righe e prendi il valore corrispondente.
* Confronta i valori per ottenere il minimo.
'''
# Alternativa 1
def minimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        valore_min = matrice[0][colonna]
        for riga in matrice:
            if riga[colonna] < valore_min:
                valore_min = riga[colonna]
        risultato.append(valore_min)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(minimo_per_colonna(matrice))

# Alternativa 2
def minimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    return [min(riga[colonna] for riga in matrice) for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(minimo_per_colonna(matrice))

