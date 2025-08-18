'''
Tema: Matrici (liste di liste)
Obiettivo: Sommare i valori di ciascuna riga e di ciascuna colonna

Nome dell’esercizio: Somma righe e colonne

Traccia:
Scrivi due funzioni:

* somma_righe(matrice: list[list[int]]) -> list[int] → restituisce una lista con la somma di ciascuna riga.
* somma_colonne(matrice: list[list[int]]) -> list[int] → restituisce una lista con la somma di ciascuna colonna.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Somma righe
# Alternativa 1
def somma_righe(matrice: list[list[int]]) -> list[int]:
    return [sum(riga) for riga in matrice]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(somma_righe(matrice))

# Alternativa 2
def somma_righe(matrice: list[list[int]]) -> list[int]:
    risultato = []

    for riga in matrice:
        somma = 0
        for elemento in riga:
            somma += elemento
        
        risultato.append(somma)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_righe(matrice))

# Somma colonne
# Alternativa 1
def somma_colonne(matrice: list[list[int]]) -> list[int]:
    return [sum(riga[colonna] for riga in matrice) for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(somma_colonne(matrice))

# Alternativa 2
def somma_colonne(matrice: list[list[int]]) -> list[int]:
    num_colonne = len(matrice[0])
    risultato = []

    for colonna in range(num_colonne):
        somma = 0
        for riga in matrice:
            somma += riga[colonna]
            
        risultato.append(somma)
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(somma_colonne(matrice))      
