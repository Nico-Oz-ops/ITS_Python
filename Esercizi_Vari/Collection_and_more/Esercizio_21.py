'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere le righe e applicare operazioni riga per riga.

Nome dell’esercizio: somma_per_riga

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
restituisca una lista contenente la somma di ogni riga.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ risultato = [6, 15, 24]

Suggerimento: Usa un ciclo for per scorrere le righe e calcolare la somma di ciascuna.
'''
# Alternativa 1
def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    return list(sum(riga) for riga in matrice)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))

# Alternativa 2
def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    lista_somma = []
    
    for riga in matrice:
        somma = 0
        for elemento in riga:
            somma += elemento
        
        lista_somma.append(somma)
    
    return lista_somma

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))