'''
Tema: Matrici + liste/dizionari + comprehension
Obiettivo: Trasformare strutture complesse.

Nome: Matrice di adiacenza → lista di archi

Traccia:
Hai un grafo rappresentato da una matrice di adiacenza (0 = nessun arco, 1 = arco).
Esempio:

grafo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]

Scrivi una funzione matrice_a_archi(grafo) che ritorni una lista di tuple (i, j) 
che rappresentano gli archi. Usa comprehension.

Output atteso con l’esempio:
[(0, 1), (1, 0), (1, 2), (2, 1)]
'''
# Alternativa 1
def matrice_a_archi(grafo: list[list[int]]) -> list[tuple[int, int]]:
    num_righe = len(grafo)
    num_colonne = len(grafo[0])
    risultato = []

    for riga in range(num_righe):
        for colonna in range(num_colonne):
            if grafo[riga][colonna] == 1:
                risultato.append((riga, colonna))
    return risultato

grafo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
print(matrice_a_archi(grafo))

# Alternativa 2
def matrice_a_archi(grafo: list[list[int]]) -> list[tuple[int, int]]:
    num_righe = len(grafo)
    num_colonna = len(grafo[0])

    return [(riga, colonna) for riga in range(num_righe) for colonna in range(num_colonna) if grafo[riga][colonna] == 1]

grafo = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]
print(matrice_a_archi(grafo))