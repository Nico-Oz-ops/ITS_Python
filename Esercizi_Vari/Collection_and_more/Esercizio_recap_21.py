'''
Tema: Matrici
Obiettivo: Sommare tutti gli elementi della matrice.

Nome: somma_totale

Traccia:
Scrivi una funzione che ritorni la somma di tutti i valori della matrice.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
# Alternativa 1
def somma_totale(matrice: list[list[int]]) -> int:
    return sum(sum(riga) for riga in matrice)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_totale(matrice))

# Alternativa 2
def somma_totale(matrice: list[list[int]]) -> int:
    somma_totale = 0

    for riga in matrice:
        somma_riga = 0
        for elemento in riga:
            somma_riga += elemento
        somma_totale += somma_riga
    
    return somma_totale

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_totale(matrice))