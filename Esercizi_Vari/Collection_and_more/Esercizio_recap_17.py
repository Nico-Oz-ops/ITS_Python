'''
Tema: Matrici
Obiettivo: Prendere una matrice e trovare per ogni riga il valore massimo e minimo.

Nome: max_min_per_riga

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), ritorni una lista di tuple (max, min) per ogni riga.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''

# Alternativa 1
def max_min_per_riga(matrice: list[list[int]]) -> list[tuple[int, int]]:
    return[(max(riga), min(riga)) for riga in matrice]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(max_min_per_riga(matrice))

# Alternativa 2
def max_min_per_riga(matrice: list[list[int]]) -> list[tuple[int, int]]:
    risultato = []

    for riga in matrice:
        valore_max_riga = riga[0]
        valore_min_riga = riga[0]
        for valore in riga:
            if valore > valore_max_riga:
                valore_max_riga = valore
            
            if valore < valore_min_riga:
                valore_min_riga = valore
        
        risultato.append((valore_max_riga, valore_min_riga))
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(max_min_per_riga(matrice))

# Alternativa 3
def max_min_per_riga(matrice: list[list[int]]) -> list[tuple[int, int]]:
    risultato = []

    for riga in matrice:
        massimo = max(riga)
        minimo = min(riga)
        for elemento in riga:
            if elemento > massimo:
                massimo = elemento
            if elemento < minimo:
                minimo = elemento

        risultato.append((massimo, minimo))
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(max_min_per_riga(matrice))