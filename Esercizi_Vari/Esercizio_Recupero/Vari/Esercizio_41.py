'''
Tema: Matrici
Obiettivo: Capire come scambiare righe e colonne

Nome: Trasposta di una matrice

Traccia:
Scrivi una funzione trasposta(matrice: list[list[int]]) -> list[list[int]] che 
restituisca la matrice trasposta, cioè una nuova matrice dove le righe diventano colonne e le colonne diventano righe.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

# output atteso
[
    [1, 4],
    [2, 5],
    [3, 6]
]
'''
# Alternativa 1 - senza uso di built-in o comprehension
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    num_colonne = len(matrice[0])
    nuova_lista = []

    for colonna in range(num_colonne):
        nuova_riga = []

        for riga in matrice:
            nuova_riga.append(riga[colonna])
        
        nuova_lista.append(nuova_riga)
    
    return nuova_lista

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

print(trasposta(matrice))

# Alternativa 2 - comprehension
def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    return [[riga[colonna] for riga in matrice] for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]

print(trasposta(matrice))