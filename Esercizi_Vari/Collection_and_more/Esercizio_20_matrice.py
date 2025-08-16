'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere una matrice ed elaborarne i valori.

Nome dell’esercizio: somma_elementi_matrice

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
ritorni la somma di tutti i suoi elementi.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ somma = 45

Suggerimento: Usa due cicli for annidati (uno per le righe e uno per le colonne).
'''

# Alternativa 1
def somma_elementi_matrice(matrice: list[list[int]]) -> int:

    somma = 0
    for riga in matrice:
        for elemento in riga:
            somma += elemento

    return somma

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(somma_elementi_matrice(matrice))

# Alternativa 2
def somma_elementi_matrice(matrice: list[list[int]]) -> int:
        return sum(sum(riga) for riga in matrice) 
    

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(somma_elementi_matrice(matrice))