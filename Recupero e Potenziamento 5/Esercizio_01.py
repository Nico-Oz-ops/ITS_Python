# Esercizio 1.

'''
Data una matrice quadrata di dimensione m x m, il carico di una posizione (r,c), indicato con k(r,c), 
è dato dalla differenza tra la somma degli elementi della riga r e la somma degli elementi della colonna c.
Ad esempio, nella seguente matrice:

1   2   1   1
0   0   0   1
1   1   2   0
2   0   0   0

c(0,0) = 1
c(1,0) = -3
c(3,3) = 0

1.A Scrivere in Python una funzione genera che data in input la dimensione dim della matrice genera una matrice 
quadrata di dimensione dim x dim, ovvero una matrice che ha dim righe e dim colonne. Ogni elemento di questa 
matrice è un numero random tra 0 e 13.
Inoltre, in ogni riga, ogni elemento della riga deve essere diverso dal primo elemento della riga stessa.

1.B Scrivere una funzione printMAT, che data in input una matrice, la stampa in output, in modo tale che 
ogni elemento della matrice occupi in output 5 caratteri.

1.C Scrivere una funzione calcolaCarico, che dati in input una matrice, un indice riga r ed un indice colonna c, 
calcola e restituisce il carico della matrice k(r,c) per la riga r e la colonna c.  

1.D Scrivere una funzione caricoNullo, che data in input una matrice, restituisce una lista di tuple, dove ogni 
tupla rappresenta una coppia di indici (r,c) per cui il carico della matrice è nullo. Ovvero, dovete trovare tutte 
le righe r e le colonne c per cui il carico della matrice k(r,c)=0 e memorizzare ogni coppia (tupla) in una lista.

1.E Scrivere una funzione caricoMax, che data in input una matrice restituisce una tupla di indici r e c per i 
quali si ha il carico massimo della matrice. Ovvero, dovete trovare la coppia di indice riga r e 
indice colonna c per cui il carico k(r,c) ha valore massimo. Prima di restituire la tupla di indici (r,c) 
stampare il valore del carico massimo.

1.F Scrivere una funzione caricoMin, che data in input una matrice restituisce una tupla di indici r e c per i 
quali si ha il carico minimo della matrice. Ovvero, dovete trovare la coppia di indice riga r e indice colonna c 
per cui il carico k(r,c) ha valore minimo. Prima di restituire la tupla di indici (r,c) stampare il valore del 
carico minimo.

1.G Scrivere un codice Python che:
    richiamando la funzione genera, genera una matrice di dimensione 5 x 5 e richiamando la funzione printMAT 
    stampa tale matrice a schermo.
    individua quante posizioni sono a carico nullo e quali sono, stampandole a schermo, ricorrendo alla 
    funzione caricoNullo.
    stampi a schermo gli indici riga rmax  e colonna cmax per cui si ha il carico massimo della matrice. 
    Ricorrendo alla funzione calcolaCarico, stampare, poi, il carico della matrice k(rmax, cmax) per 
    verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMax.
    stampi a schermo gli indici riga rmin  e colonna cmin per cui si ha il carico minimo della matrice. 
    Ricorrendo alla funzione calcolaCarico, stampare, poi, il carico della matrice k(rmin, cmin) per 
    verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMin.
'''

from random import randint

# 1.A
def genera(n: int) -> list[list[int]]:
    # creo una riga della matrice
    # ogni riga è una lista di interi
    # inizializzo la riga come una lista vuota
    matrix = []
    for r in range(n):
        row = []

    # il primo elemento della riga è un numero random tra 0 e 13
        primo_elemento = randint(0, 13)
    
    # aggiungo il primo elemento alla riga
        row.append(primo_elemento)
    
    # per ogni colonna della riga, aggiungo un numero random tra 0
    # e 13, diverso dal primo elemento della riga
        for c in range(1, n):

            elemento = primo_elemento
            while elemento == primo_elemento:
                elemento = randint(0, 13)

            # aggiungo l'elemento alla riga 
            row.append(elemento)
        matrix.append(row)
    
    return matrix

# 1.B
def printMAT(matrix: list[list[int]]) -> list[list[int]]:

    for row in range(len(matrix)):

        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]:<5}", end=" ")
        
        print("\n")

if __name__ == "__main__":

    matrice: list[list[int]] = genera(5)
    printMAT(matrice)

# 1.C 
def calcolaCarico(matrix: list[list[int]], r: int, c: int) -> int:
    if r < 0 or r > len(matrix) or c < 0 or c > len(matrix[0]):
        raise ValueError ("Errore, l'elemento è fuori dai limiti della matrice")
    
    somma_riga = sum(matrix[r])
    somma_colonna = sum(matrix[r][c] for r in range(len(matrix)))
    carico = somma_riga - somma_colonna

    return carico

if __name__ == "__main__":

    print("\n")
    matrix = genera(3)
    printMAT(matrix)
    r = randint(0,2)
    c = randint(0,2)

    print(f"La differenza tra la somma 'riga {r + 1}' e la somma della 'colonna {c + 1}' è: {calcolaCarico(matrix, r, c)}")

# 1.D
def caricoNullo(matrix: list[list[int]]) -> list[tuple]:
    carico_nullo = []

    for r in range(len(matrix)):

        for c in range(len(matrix[r])):

            if calcolaCarico(matrix, r, c) == 0:
                carico_nullo.append((r, c))

    return carico_nullo

if __name__ == "__main__":

    matrix = genera(3)
    printMAT(matrix)
    r = randint(0, 3)
    c = randint(0, 3)
    print(f"Carico nullo: \n{caricoNullo(matrix)}")

# 1.E

def caricoMax(matrix: list[list[int]]) -> tuple:
    max_carico = None
    max_indici = (0, 0)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            carico = calcolaCarico(matrix, r, c)
            if (max_carico == None) or (carico > max_carico):
                max_carico = carico
                max_indici = (r, c)

    return max_indici, max_carico

if __name__ == "__main__":

    matrix = genera(3)
    printMAT(matrix)
    posizione, valore = caricoMax(matrix)

    print(f"Il carico massimo è {valore} nella posizione {posizione}")

# 1.F

def caricoMin(matrix: list[list[int]]) -> tuple:
    min_carico = None
    min_indici = (0, 0)

    for r in range(len(matrix)):

        for c in range(len(matrix[r])):

            carico = calcolaCarico(matrix, r, c)
            if (min_carico == None) or carico < min_carico:
                min_carico = carico
                min_indici = (r, c)
    
    return min_indici, min_carico

if __name__ == "__main__":
    
    matrix = genera(3)
    printMAT(matrix)
    posizione_min, valore_min = caricoMin(matrix)

    print(f"Il carico minimo è {valore_min} nella posizione {posizione_min}")
    print("\n")


# 1.G

if __name__ == "__main__":

    matrice = genera(5)
    printMAT(matrice)

    # carico nullo
    print("Posizione a Carico Nullo:")
    print(f"{caricoNullo(matrice)}\n")

    # carico massimo
    posizione_max, valore_max = caricoMax(matrice)
    print(f"Posizione a Carico massimo '{(posizione_max)}', con carico <<{valore_max}>>")
    carico_verifica_max = calcolaCarico(matrice, *posizione_max)
    print(f"Verifica carico massimo con calcolaCarico: <<{carico_verifica_max}>>\n")

    # carico minimo
    posizione_min, valore_min = caricoMin(matrice)
    print(f"Posizione a Carico minimo '{(posizione_min)}, con carico <<{valore_min}>>")
    carico_verifica_min = calcolaCarico(matrice, *posizione_min)
    print((f"Verifica carico minimo con calcolaCarico: <<{carico_verifica_min}>>\n"))















