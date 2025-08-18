'''
Tema: Matrici
Obiettivo: Calcolare la trasposta della matrice.

Nome: trasposta

Traccia:
Scrivi una funzione che, data una matrice, ritorni la sua trasposta (righe ↔ colonne).

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    return[[riga[colonna] for riga in matrice] for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(trasposta(matrice))

# Alternativa 2
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        nuova_riga = []
        for riga in matrice:
            nuova_riga.append(riga[colonna])
        
        risultato.append(nuova_riga)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(trasposta(matrice))




