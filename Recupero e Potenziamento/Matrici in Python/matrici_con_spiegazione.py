'''
CODICE CON SPIEGAZIONE

A.1 Scrivere in Python una funzione generaMAT(n: int) che generi una matrice di dimensione n x n. 
La matrice deve contenere tutte le tabelline di tutti i numeri da 1 a n. 

A.2 Scrivere una funzione printMAT(mat: list[list[int]]), che data in input una matrice, la stampa in output, 
in modo tale che ogni elemento della matrice occupi in output 5 caratteri.

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

    # possiamo pensare ad una matrice come una lista i cui elementi sono liste di numeri interi, ovvero una sorta di liste annidate. 
    # Per avere un'immagine più concreta, visualizziamo la matrice come una serie di n liste poste una sotto l'altra fino a formare una sorta di tabella. 
    '''
    matrice = [
        [1, 2, 3, 4,  5,  6,  7,  8,  9, 10],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        [3, 6, 9, 12,15, 18, 21, 24, 27, 30]
    ]

    '''
    # quindi in una matrice possiamo riconoscere delle righe e delle colonne.
    # Le righe le leggiamo verticalmente, mentre le colonne le leggiamo orizzontalmente.
    # Per definire la posizione di un elemento all'interno di una matrice abbiamo bisogno di due indici, un indice riga r ed un indice colonna c. 
    # L'indice riga r assume valori tra  0 (prima riga) fino al numero di righe - 1 (ultima riga ha indice r=n-1)
    # L'indice colonna c assume valori tra 0 (prima colonna) fino al numero colonne - 1 (ultima colonna ha indice c = n-1)
    # Nell'esempio, viene riportata una matrice di dimensione 3 x 10, ovvero una matrice che ha 3 righe e 10 colonne e con i rispettivi indici r e c
    # quindi r assume valori tra 0 e 2 (3 righe -1 = 2)
    # e c assume valori tra 0 e 9 (10 colonne - 1 = 9)
    '''
    matrice:

                c0      c1      c2      c3      c4      c5      c6      c7      c8      c9
              ---------------------------------------------------------------------------------
    r0        |   1   |   2   |   3   |  4   |   5    |   6   |   7   |   8   |   9   |   10  |
              ---------------------------------------------------------------------------------
    r1        |   2   |   4   |   6   |   8   |   10  |   12  |   14  |   16  |   18  |   20  |
              ---------------------------------------------------------------------------------
    r2        |   3   |   6   |   9   |   12  |   15  |   18  |   21  |   24  |   27  |   30  |
              ---------------------------------------------------------------------------------  

    '''

    # quindi, un elemento della matrice è dato da matrice(0,2) = 3 , ovvero l'elemento che corrisponde alla riga 0 (r=0) e colonna 2 (c=2)
    # che altro non è che l'elemento in posizione sulla prima riga, terza colonna. 
    # l'elemento matrice(1,4) = 10, è l'elemento che corrisponde alla riga 1 (r=1) e colonna 4 (c=4), ovvero 
    # l'elemento situato sulla seconda riga, quinta colonna

    # definiamo ora la matrice mat. Ricordiamoci che in Python (senza uso di librerie) una matrice può essere rappresentata come una lista,
    # i cui elementi sono liste di numeri interi:
    mat: list[list[int]] = []

    # per lavorare con  una matrice (riempirla e/o stamparla in output) devo lavorare con due cicli for annidati:
    # il ciclo for più esterno riempira'/leggera' verticalmente le righe, mentre il ciclo for più interno leggera'/riempira' orizzontalemnte 
    # le colonne

    # vediamo come riempire una matrice: 

    # La matrice è una lista, e come tale va trattata. 

    # In particolare, è una lista di liste, in cui queste liste sono disposte una sotto l'altra. 
    
    # creiamo le varie righe
    # poichè il testo ci richiede di creare una matrice di dimensione n x n, la nostra matrice avrà n righe e n colonne

    # crea n righe
    for r in range(n): # ricordiamo che r assume valori tra 0 e n-1 e che il primo elemento di una lista si ha in posizione 0

        # abbiamo detto che una matrice è una lista di liste, dove le liste vengono disposte una sotto l'altra,
        # andando a definire una sorta di struttura tabellare
        # quindi, ogni riga della matrice sarà una lista!

        # creiamo una lista che rappresenta ogni riga.
        # questa lista la dobbiamo creare ad ogni ripetizione del ciclo for più esterno perchè rappresenta una specifica riga da riempire
        row: list[int] = []
        # nel nostro caso, row è una lista di numeri interi 

        # con un ciclo for più interno, andiamo a riempire la lista row. 
        # riempire la lista row con dei numeri interi, significa andare a definire le colonne!

        # quindi, creiamo le colonne.
        # poichè la matrice deve avere n righe e n colonne, essendo una matrice di dimensione n x n, farò
        for c in range(n): # ricordiamo che c assume valori tra 0 e n-1 e che il primo elemento di una lista si ha in posizione 0

            # come funzionano questi due cicli annidati?
            # parte ciclo esterno 
            # r= 0
            # parte il ciclo interno che legge tutti i valori di c che vanno da 0 a n-1
            # torno nel ciclo esterno
            # r = 1
            # parte il ciclo interno che legge tutti i valori di c che vanno da 1 a n-1 
            # torno nel ciclo esterno
            # r = 2 
            # parte il ciclo interno che legge tutti i valori di c che vanno da 1 a n-1
            # e cosi via 

            # Capito come funzionano questi cicli annidati, 
            # devo definire il valore di ogni elemento di ogni riga della matrice. 
            # poichè voglio che la matrice rappresenti le tabelline dei numeri da 1 a n, 
            # ogni riga dovrà rappresentare una tabellina in particolare:
            # ad esempio, la prima riga (r = 0) rappresenterà la tabellina del 1,
            # la seconda riga (r = 1) rappresenterà la tabellina del 2,
            # la terza riga ( r = 2) rappresenterà la tabellina del 3 e cos' via.

            # quindi, una generica riga rappresenterà una tabellina e questa riga è rappresentata dalla lista row. 
            # pertanto, ogni elemento di row sarà dato da:
            x: int = (r+1) * (c + 1)

            # poichè r parte da 0, se scrivessi x = r * c, avrei che la prima riga della matrice sarebbe la tabellina dello 0
            # e non la tabellina dell'1. 
            # poiche anche c parte da 0, se scrivessi x = (r+1)*c, otterrei come primo elemento della prima riga 0. 
            # Se voglio la tabellina dell'1 devo scrivere x = (r+1) * (c+1), così quando r = 0, il primo elemento della prima riga è
            # x = (r+1) * (c+1) = (0+1) * (0+1) = 1 * 1 = 1 .
            # Piu' in generale, 
            # io vado a riempire la prima riga con x = (0+1) * (c+1), ovvero 1 * (c+1) = c+1, con c che varia tra 0 e n-1
            
            

            '''
            matrice:

                        c0      c1      c2      c3      c4      c5      c6      c7      c8      c9
                    ---------------------------------------------------------------------------------
            r0        |   1   |   2   |   3   |  4   |   5    |   6   |   7   |   8   |   9   |   10  |
                    ---------------------------------------------------------------------------------
            r1        |   2   |   4   |   6   |   8   |   10  |   12  |   14  |   16  |   18  |   20  |
                    ---------------------------------------------------------------------------------
            r2        |   3   |   6   |   9   |   12  |   15  |   18  |   21  |   24  |   27  |   30  |
                    ---------------------------------------------------------------------------------  

            '''

            # Infatti, se ad esempio, voglio sapere quanto fa 1*7, dovrò fare r0*c6= 7 , in quanto 1 * 7 fa parte della tabellina del 1
            # se voglio sapere quanto fa 2*10, dovrò fare r1*c9=20, in quanto 2 * 10 fa parte della tabellina del 2
            # se voglio sapere quanto fa 3*5, dovrò fare r2*c4=15, in quanto 3 * 5 fa parte della tabellina del 3

            # notate che sto leggendo la matrice come se fosse una sorta di tabella. 
            # quindi ogni elemento di una matrice corrisponde ad un valore di una specifica tabbellina, in particolare,
            # ogni valore della matrice è dato dalla moltiplicazione tra una specifica riga ed una specifica colonna. 

            # una volta ottenuto il valore x di un elemento, aggiungo l'elemento alla riga 
            row.append(x) 

            # ripetendo questa operazione per tutti i valori di c che vanno da 0 a n-1, 
            # io riempio la lista row con tutti i valori che vanno a coprire una determinata riga della matrice 
            # quindi per ogni iterazione io riempio la matrice riga per riga

        # una volta riempita tutta una riga della matrice, esco dal ciclo for più interno e ritorno nel ciclo for più esterno.
        # una volta riempita tutta la riga della matrice, nel ciclo for più esterno devo aggiungere la lista row alla matrice
        # questo perchè la matrice la dobbiamo pensare come lista di liste.
        # quindi, devo appendere la lista row riempita con n numeri interi alla lista mat.
        mat.append(row)

        # ripetendo questo procedimento per tutte le n righe, ottengo la matrice. 

        # dunque, ho creato n liste, disposte uno sotto l'atra e ho riempito ogni lista con n numeri interi, 
        # ottenendo una matrice, ovvero una lista i cui elementi sono liste di numeri interi 
    
    # esco dal ciclo for più esterno 

    # ----------------------------------------------------------------------------------------------------------------------------------------

    # in sintesi:
    # una matrice è una lista di liste.
    # 
    # per creare una matrice: 
    #  
    # for r in range(numero_righe):
        # creo lista 
        # for c in range(numero_colonne):
            # riempio lista con dei valori, ovvero facendo lista.append(valore)
        # appendo lista alla matrice, creando una riga della matrice (matrice.append(lista))
    
    # ripeto il procedimento per tutte le righe

    # -----------------------------------------------------------------------------------------------------------------------------------------

    # ritorno la matrice.
    return mat


# A.2 
def printMAT(mat: list[list[int]]) -> None:

    # abbiamo detto che una matrice è una lista i cui elementi sono liste di ineri. 
    # ogni elemento della lista è individuato da un indice riga r e un indice colonna c, per cui si ha che un generico elemento della matrice mat 
    # è dato da:
    # mat[r,c], dove 
    # mat[r] indica la riga  r della matrice 
    # mat[r][c] indica la colonna c della riga r 
    # ad esempio, mat[1,2] indica la terza colonna della riga seconda riga (ovvero l'elemento che si trova alla seconda riga sulla terza colonna)

    # vediamo come stampare a schermo la matrice: 
    
    # scorri tutte le righe 
    # perchè devo usare len(mat) ?
    # perchè una matrice è una lista i cui elementi sono altre liste. Quindi, devo trattare la matrice come una normale lista. 
    # Immaginiamo la matrice come una lista di liste, dove ognuna di queste liste rappresenta una riga e queste righe sono disposte l'una sotto l'alatra
    # se voglio sapere quante righe ha una matrice, devo considerare la lunghezza della lista mat, ovver len(mat)
    for r in range(len(mat)):

        # per poter ottenere un elemento della matrice, data una riga r, devo scorrere anche tutte le colonne che trovo lungo la riga r. 
        # ricordiamo che la riga r è una lista, in particolare una lista di numeri interi. 
        # Quindi, ho bisogno di un ciclo per scorrere la lista. 
        # Quanto è lunga questa lista r di numeri interi ? è lunga len(mat[r]). 
        # in quanto mat[r] indica proprio la riga r della matrice. 

        # scorri colonne (ogni elemento di mat è una lista)
        for c in range(len(mat[r])):

            # stampa ogni valore della matrice in modo nell'output l'elemento occupi 5 caratteri
            # quindi, data la riga r e la colonna c, ottengo l'elemento mat[r][c] della matrice
            # spieghiamo la scrittura {mat[r][c]:<5}
            # mat[r][c] è l'elemento della matrice situato sulla riga r e colonna c
            # : -> indicano una formattazione dell'output
            # < -> indicano un allineamento a sinistra dell'output
            # 5 -> indica che l'elemento della matrice mat deve occupare 5 caratteri, 5 posizioni quando viene stampato a schermo.
            # immaginiamo che ogni linea di output sia una sorta di griglia composta da tante cellette, dove ogni celletta rappresenta 
            # una posizione nell'output: 
            '''
            -------------------------------------------------------------------------------------------------------------------------
            |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 
            -------------------------------------------------------------------------------------------------------------------------
            
            '''
            # stampare gli elementi della prima riga della matrice, dove ogni elemento deve occupare 5 posizioni in output significa fare questo:

            '''
            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            | 1 |   |   |   |   | 2 |   |   |   |   | 3 |   |   |   |   | 4 |   |   |   |   | 5 |   |   |   |   | 6 |   |   |   |   | 7 |   |   |   |   | 8 |   |   |   |   | 9 |   |   |   |   | 10 |   |   |   |  |
            ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            '''
            # per default, la funzione print di Python va a capo dopo ogni print. 
            # se vogliamo stamapre dei numeri tutti sulla stessa riga dobbiamo modificare questo comportamento della funzione print,
            # forzando la funzione a stampare tutto sulla stessa riga. Quindi, ciò che dobbiamo fare è impostare il parametro end del print in questo modo,
            # ovvero end="" (carattere vuoto)

            # quindi per stampare in maniera ordinata ogni elemento della matrice farò:
            print(f"{mat[r][c]:<5}", end="")

            # pertanto, data una riga r, ripetendo questa procedura per tutte le colonne c della riga, 
            # io posso stampare in output tutta una riga della matrice
            # stampata tutta la riga r della matrice, esco dal ciclo for più interno e ritorno nel ciclo for esterno.
        
        # Quando torno nel ciclo for più esterno, ho stampato in output tutta una riga r. 
        # per una corretta formattazione della matrice (pensata come una tabella), alla fine di ogni riga devo andare a capo
        # quindi, 
        print("\n")

        # ripetendo questo procedimento per tutte le righe r della matrice, posso stampare in output l'intera matrice (pensata come una tabella)

        # ----------------------------------------------------------------------------------------------------------------------------------------

        # in sintesi:
        # una matrice è una lista di liste.
        # 
        # per stampare una matrice: 
        #  
        # for r in range(numero_righe): 
            # for c in range(numero_colonne):
                # stampo in output l'elemento mat[r][c] della matrice
                # ripetendo questa procedura per tutte le colonne della riga r, ho stampato tutta la riga r
            # stampata tutta la riga r, vado a capo 
        
        # ripeto il procedimento per tutte le righe

        # -----------------------------------------------------------------------------------------------------------------------------------------

    
    

# A.3
# definisco il metodo main:
if __name__ == '__main__':
    
    # scrivo il codice richiesto

    # inizializzo una matrice di dimenaione 10 x 10, ovvero una matrice con n= 10 righe e n= 10 colonne.
    matrice: list[list[int]] = generaMAT(10)

    # mostriamo in output la matrice
    printMAT(matrice)

            
             
            



