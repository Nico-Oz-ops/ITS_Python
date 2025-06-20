'''
CODICE SENZA COMMENTI

A.1 Scrivere in Python una funzione generaMAT(n: int) che generi una matrice di dimensione n x n. La matrice deve contenere tutte le tabelline di tutti i numeri da 1 a n. 

A.2 Scrivere una funzione printMAT(mat: list[list[int]]), che data in input una matrice, la stampa in output, in modo tale che ogni elemento della matrice occupi in output 5 caratteri.

A.3 Scrivere nel main un codice Python che sfruttando la funzione generaMAT() crei una matrice 10 x 10 contenente tutte le tabelline di tutti i numeri da 1 a 10. Visualizzare a schermo la matrice creata ricorrendo alla funzione printMAT(). 

Esempio di Output: 

1    2    3    4    5    6    7    8    9    10   

2    4    6    8    10   12   14   16   18   20   

3    6    9    12   15   18   21   24   27   30   

4    8    12   16   20   24   28   32   36   40   

5    10   15   20   25   30   35   40   45   50   

6    12   18   24   30   36   42   48   54   60   

7    14   21   28   35   42   49   56   63   70   

8    16   24   32   40   48   56   64   72   80   

9    18   27   36   45   54   63   72   81   90   

10   20   30   40   50   60   70   80   90   100 


'''

# A.1 

def generaMAT(n: int) -> list[list[int]]:
    
    # definiamo la matrice mat. Ricordiamoci che in Python (senza uso di librerie) una matrice può essere rappresentata come una lista,
    # i cui elementi sono liste di numeri interi:
    mat: list[list[int]] = []
   
    # crea n righe con un clico for esterno
    for r in range(n): 

        # creiamo una lista che rappresenta ogni riga.
        row: list[int] = []
        # nel nostro caso, row è una lista di numeri interi 

        # con un ciclo for più interno, andiamo a riempire la lista row. 
        # riempire la lista row con dei numeri interi, significa andare a definire le colonne!

        # quindi, creiamo le colonne.
        # poichè la matrice deve avere n righe e n colonne, essendo una matrice di dimensione n x n, farò
        for c in range(n): 

            
            # poichè voglio che la matrice rappresenti le tabelline dei numeri da 1 a n, 
            # ogni riga dovrà rappresentare una tabellina in particolare:
            # ad esempio, la prima riga (r = 0) rappresenterà la tabellina del 1,
            # la seconda riga (r = 1) rappresenterà la tabellina del 2,
            # la terza riga ( r = 2) rappresenterà la tabellina del 3 e cos' via.

            # quindi, una generica riga rappresenterà una tabellina e questa riga è rappresentata dalla lista row. 
            # pertanto, ogni elemento di row sarà dato da:
            x: int = (r+1) * (c + 1)

            # una volta ottenuto il valore x di un elemento, aggiungo l'elemento alla riga 
            row.append(x) 

            # ripetendo questa operazione per tutti i valori di c che vanno da 0 a n-1, 
            # io riempio la lista row con tutti i valori che vanno a coprire una determinata riga della matrice 

        # una volta riempita tutta la riga della matrice, nel ciclo for più esterno devo aggiungere la lista row alla matrice
        # questo perchè la matrice la dobbiamo pensare come lista di liste.
        # quindi, devo appendere la lista row riempita con n numeri interi alla lista mat.
        mat.append(row)

        # ripetendo questo procedimento per tutte le n righe, ottengo la matrice. 

        # ritorno la matrice.
    return mat


# A.2 
def printMAT(mat: list[list[int]]) -> None:

    # scorro le righe (ogni elemento di mat è una lista)
    for r in range(len(mat)):

        # per poter ottenere un elemento della matrice, data una riga r, devo scorrere anche tutte le colonne che trovo lungo la riga r. 
        # ricordiamo che la riga r è una lista, in particolare una lista di numeri interi. 
        # Quindi, ho bisogno di un ciclo per scorrere la lista. 
        # Quanto è lunga questa lista r di numeri interi ? è lunga len(mat[r]). 
        # in quanto mat[r] indica proprio la riga r della matrice. 

        # scorro le  colonne (leggi riga per riga. Ogni elemento di una riga, definisce una colonna)
        for c in range(len(mat[r])):

            # stampa ogni valore della matrice in modo nell'output l'elemento occupi 5 caratteri
            print(f"{mat[r][c]:<5}", end="")

            # pertanto, data una riga r, ripetendo questa procedura per tutte le colonne c della riga, 
            # io posso stampare in output tutta una riga della matrice
            # stampata tutta la riga r della matrice, esco dal ciclo for più interno e ritorno nel ciclo for esterno.
        
        # Quando torno nel ciclo for più esterno, ho stampato in output tutta una riga r. 
        # per una corretta formattazione della matrice (pensata come una tabella), alla fine di ogni riga devo andare a capo
        # quindi, 
        print("\n")

        # ripetendo questo procedimento per tutte le righe r della matrice, posso stampare in output l'intera matrice (pensata come una tabella)
    

# A.3
# definisco il metodo main:
if __name__ == '__main__':
    
    # scrivo il codice richiesto

    # inizializzo una matrice di dimenaione 10 x 10, ovvero una matrice con n= 10 righe e n= 10 colonne.
    matrice: list[list[int]] = generaMAT(10)

    # mostriamo in output la matrice
    printMAT(matrice)

            
             
            



