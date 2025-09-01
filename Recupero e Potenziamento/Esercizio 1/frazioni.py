# Esercizio 1

'''
- 1.A Si Scriva in Python in un file frazioni.py una classe Frazione, i cui attributi privati siano 
    rispettivamente numeratore e denominatore.
    Si definiscano i metodi __init__, setter, getter, __str__, value.
    In particolare:
    - il metodo value(), deve restituire il valore della frazione, ovvero numeratore / denominatore 
      arrotondato a 3 cifre decimali;
    - il metodo __str__ deve mostare in output la frazione nel seguente modo: "numeratore / denominatore ";
    - i metodi setter devono controllare che il valore inserito sia un intero, in caso contrario il 
      numeratore ed il denominatore devono essere impostati per default rispettivamente a 13 e 5. 
      Inoltre, il metodo setter relativo al denominatore deve assicurarsi che questo non sia mai uguale a 0. 
      Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

    Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la 
    funzione is_integer().


- 1.B Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
    Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.
    Infatti,
    - i divisori di 12 sono:
        12 = 1, 2, 3, 4, 6, 12
    - i divisori di 18 sono:
        18 = 1, 2, 3, 6, 9, 18

    il divisore più grande che 12 e 18 hanno in comune è 6.

    Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
    Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y, allora la funzione deve ritornarlo 
    come numero intero.
    Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y, la funzione deve 
    ritornare 1.
   

    Suggerimento: per semplicità, per implementare la funzione richiesta, trovare una soluzione che 
    generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y per evitare di replicare 
    righe di codice.
   
- 1.C Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni, 
    ovvero il più grande divisore comune tra numeratore e denominatore è 1.

    Sia l una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

    Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di 
    frazioni ritorni in output una lista di frazioni irriducibili.
    Nello specifico:
    - se una frazione f della lista data in input è già irriducibile, allora inserire questa frazione f 
      nella lista da ritornare in output.
    - se una frazione f della lista data in input può essere semplificata, in una frazione irriducibile f1, 
      allora si deve prima semplicare la frazione f, ottenendo la frazione irriducibile f1 e poi inserire f1 
      nella lista da ritornare in output.

    Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione 
    semplifica.
    Inserire in modo adeguato le seguenti frazioni nella lista l.
   
- 1.D Scrivere in Python una funzione chiamata fractionCompare() che prende in input la lista di frazioni l 
    originale e la lista con le frazioni di l semplificata.
    Usando il metodo value(), dimostrare che il valore di ogni funzione di entrambe le liste non cambia, 
    stampandolo in output.
    Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538
   

- 1.E Scrivere un codice Python che inizializzi la seguente lista l di frazioni, dove ogni frazione è un 
    oggetto della classe Frazione:
    l = 2.5/0,   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15
    Sfruttando la funzione semplifica, generare una nuova lista chiamata l_s, contente una versione 
    semplificata delle frazioni della lista l.
    Infine, richiamando la funzione fractionCompare, dimostrare che le funzioni delle lista l e l_s 
    sono equivalenti, ovvero hanno lo stesso valore.'''


# 1.A 
class Frazione:

    def __init__(self, numeratore: int, denominatore: int) -> float:
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)
    
    def set_numeratore(self, numeratore: int):

        if isinstance(numeratore, (int, float)) and float(numeratore).is_integer():
            self._numeratore = numeratore
        else:
            self._numeratore = 13
    
    def set_denominatore(self, denominatore: int):

        if isinstance(denominatore, (int, float)) and float(denominatore).is_integer() and denominatore != 0:
            self._denominatore = denominatore
        else:
            self._denominatore = 5
    
    def get_numeratore(self) -> int:
        return self._numeratore
    
    def get_denominatore(self) -> int:
        return self._denominatore
    
    def value(self) -> float:
        return round((self._numeratore / self._denominatore), 3)
    
    def __str__(self):
        return f"{self._numeratore} / {self._denominatore} = {self.value()}"

# 1.B 

def mcd(x: int, y: int) -> int:

    if x < y:
        x, y = y, x # assicuro che x sia sempre il maggiore
    
    while y != 0: # finché "y" non è zero continuo a calcolare il resto 

        x, y = y, x % y
    
    return x

# 1.B - versione prof

def mcd(x: int, y: int) -> int:
    # se x e y non hanno divisori in comune, sicuramente avranno in comune 1 come massimo comune divisore,
    # perché tutti i numeri sono divisibili per 1.

    max_divisor = 1

    # se y > x, modifichiamo il valore di end

    if y > x:
        end = y
    
    for i in range(1, end + 1):

        # l'indice i gioca il ruolo di divisore per i numeri x e y
        # i divisori di 'x' sono dati da:
        # x % i == 0

        # i divisori di 'y' sono dati da:
        # y % i == 0

        # troviamo i divisori comuni, ovvero i valori di i per cui la divisione x/i da resto 0 
        # e la divisione y/i da resto 0
        if x % i == 0 and y % i == 0:

            # una volta trovato 'i' per cui ottengo un divisore comune per 'x' e 'y'
            # devo controllare se questo divisore in comune sia il più grande
            if i > max_divisor:
                max_divisor = i

    return max_divisor

# 1.C
def semplifica(l: list[Frazione]) -> list[Frazione]:

    list_semplificata = []

    for frazione in l:
        num = frazione.get_numeratore()
        den = frazione.get_denominatore()
        divisore = mcd(num, den)

        if divisore == 1:
            list_semplificata.append(frazione)
        
        else:
            num_semp = num // divisore
            den_semp = den // divisore

            list_semplificata.append(Frazione(num_semp, den_semp))

    return list_semplificata

# 1.D
def fractionCompare(l: list[Frazione], list_semplificata: list[Frazione]) -> None:

    for i in range(len(l)):
        print(f"Valore frazione originale: {l[i].value()} --- Valore frazione ridotta: {list_semplificata[i].value()}")


#1.E
if __name__ == "__main__":

    l = [
        Frazione(2.5, 0),
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15),
    ]

    l_s = semplifica(l)
    fractionCompare(l, l_s)





    


        