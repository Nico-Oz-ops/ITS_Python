'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere le colonne di una matrice.

Nome dell’esercizio: massimo_per_colonna

Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
restituisca una lista contenente il valore massimo di ciascuna colonna.

Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ risultato = [7, 8, 9]

Suggerimento: Scorri le colonne usando l’indice, oppure prova a trasporre la matrice con zip().
'''
# Alternativa 1
def massimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    num_colonne = len(matrice[0])             # calcolo il numero di colonne
    risultato = []

    for colonna in range(num_colonne):        # scorro ogni colonna
        valore_massimo = matrice[0][colonna]  # prendo il primo valore della colonna, considerando che inizialmente sia il massimo
        for riga in matrice:                  # scorro tutte le righe
            if riga[colonna] > valore_massimo: # vado a confrontare il valore attuale "riga[colonna]" con il valore_massimo
                valore_massimo = riga[colonna] # se il valore attuale è maggiore al massimo allora aggiorno

        risultato.append(valore_massimo)       # aggiungo il massimo trovato per questa colonna
    
    return risultato

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(massimo_per_colonna(matrice))

# Alternativa 2
def massimo_per_colonna(matrice: list[list[int]]) -> list[int]:
    return[max(riga[colonna] for riga in matrice) for colonna in range(len(matrice[0]))]

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(massimo_per_colonna(matrice))


