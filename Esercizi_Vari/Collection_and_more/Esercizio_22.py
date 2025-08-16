'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere righe e colonne e applicare funzioni built-in.

Nome dell’esercizio: massimo_per_riga

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
restituisca una lista contenente il valore massimo di ciascuna riga.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ risultato = [3, 6, 9]

Suggerimento: Usa la funzione built-in max() su ciascuna riga.
'''
# Alternativa 1
def massimo_per_riga(matrice: list[list[int]]) -> list[int]:
    return list(max(riga) for riga in matrice)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(massimo_per_riga(matrice))

# Alternativa 2
def massimo_per_riga(matrice: list[list[int]]) -> list[int]:
    lista_massimi = []

    for riga in matrice:
        lista_massimi.append(max(riga))
    
    return lista_massimi

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(massimo_per_riga(matrice))

# Alternativa 3
def massimo_per_riga(matrice: list[list[int]]) -> list[int]:
    lista_massimi = []

    for riga in matrice:

        max_riga = riga[0]
        for elemento in riga:
            if elemento > max_riga:
                max_riga = elemento
        
        lista_massimi.append(max_riga)
    
    return lista_massimi

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(massimo_per_riga(matrice))


