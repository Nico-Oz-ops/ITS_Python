'''
Tema: Matrici + comprehension
Obiettivo: Trasformazione di liste di liste.

Nome: Trasposta di una matrice

Traccia:
Scrivi una funzione trasposta(matrice) che ritorni la matrice trasposta (righe ↔ colonne) 
utilizzando list comprehension.

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
'''
# Alternativa 1
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    num_righe = len(matrice)
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        nuova_riga = []
        for riga in range(num_righe):
            nuova_riga.append(matrice[riga][colonna])
        risultato.append(nuova_riga)

    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
print(trasposta(matrice))

# Alternativa 2
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    num_righe = len(matrice)
    num_colonne = len(matrice[0])

    return [[matrice[riga][colonna] for riga in range(num_righe)] for colonna in range(num_colonne)]

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
print(trasposta(matrice))

