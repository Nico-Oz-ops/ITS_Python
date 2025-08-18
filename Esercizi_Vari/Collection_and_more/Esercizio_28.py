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

    return[[riga[colonna] for riga in matrice] for colonna in range(len(matrice[0]))]
    # ciclo esterno -> for colonna in range(len(matrice[0]))
    '''
    1. matrice[0] -> prende la prima riga della matrice originale
    2. len(matrice[0]) -> numero di colonne della matrice
    3. for colonna in range(...) -> scorre ogni indice di colonna
    Ogni indice di colonna diventerà una nuova riga nella matrice trasposta'''

    # ciclo interno -> [riga[colonna] for riga in matrice]
    '''
    1. for riga in matrice -> Scorre tutte le righe della matrice originale
    2. riga[colonna] -> Per ciascuna riga prende l’elemento alla colonna
    Questi valori, presi dalla stessa colonna ma da tutte le righe, diventano la nuova riga nella trasposta
    '''

matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
print(trasposta(matrice))
