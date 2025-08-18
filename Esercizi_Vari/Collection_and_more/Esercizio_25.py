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

Suggerimento:
* Scorri le colonne come abbiamo fatto prima.
* Per ogni colonna, calcola sia il minimo che il massimo.
* Mettili insieme in una tupla e aggiungila alla lista finale.
'''
# Alternativa 1
def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        valore_min = matrice[0][colonna]
        valore_max = matrice[0][colonna]

        for riga in matrice:
            if riga[colonna] < valore_min:
                valore_min = riga[colonna]
            if riga[colonna] > valore_max:
                valore_max = riga[colonna]

        risultato.append((valore_min, valore_max))
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(min_max_per_colonna(matrice))

# Alternativa 2
def min_max_per_colonna(matrice: list[list[int]]) -> list[tuple[int, int]]:
    return [(min(riga[colonna] for riga in matrice), max(riga[colonna] for riga in matrice))
            for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(min_max_per_colonna(matrice))
