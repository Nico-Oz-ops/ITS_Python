'''
2. RENDERING GRAFICO

Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. 
Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

1. Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della 
forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() 
per disegnare su schermo la forma.

2. Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della 
forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore. 
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
(Vedi Esempio di output)

3. Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e 
della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il 
nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
(Vedi Esempio di output)

4. Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del 
triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma 
su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori 
passati nel costruttore. Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") 
lungo il suo perimetro. (Vedi Esempio di output)
 
Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina 
ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, 
separate da uno spazio.

Esempi di output:
Ecco un Quadrato di lato 4!

* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

Ecco un Triangolo avente base 4 ed altezza 4!
*      
* *    
*   *  
* * * *
L'area di questo triangolo vale: 8.0
'''

from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome: str):
        self.nome = nome
    
    @abstractmethod
    def getArea(self) -> float:
        pass
    
    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato: int, nome: str = "Quadrato"):
        super().__init__(nome)
        self.lato = lato
    
    def getArea(self) -> float:
        return self.lato ** 2
    
    def render(self):
        print(f"Ecco un {self.nome} di lato {self.lato}!\n")
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1 or j == 0 or j == self.lato - 1:
                    print("*", end=" ")

                else:
                    print(" ", end=" ")
            print()

        print(f"L'area di questo {self.nome.lower()} vale: {self.getArea()}")

class Rettangolo(Forma):
    def __init__(self, altezza: int, larghezza: int):
        super().__init__("Rettangolo")
        self.altezza = altezza
        self.larghezza = larghezza
    
    def getArea(self) -> float:
        return self.altezza * self.larghezza
    
    def render(self):
        print(f"Ecco un {self.nome} avente base {self.larghezza} ed altezza {self.altezza}!\n")
        for riga in range(self.altezza):
            for colonna in range(self.larghezza):
                if riga == 0 or riga == self.altezza - 1 or colonna == 0 or colonna == self.larghezza - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        print(f"L'area di questo {self.nome.lower()} vale: {self.getArea()}")
    
class Triangolo(Forma):
    def __init__(self, lato: int):
        super().__init__("Triangolo")
        self.lato = lato

    def getArea(self) -> float:
        return self.lato * self.lato / 2
    
    def render(self):
        print(f"Ecco un {self.nome} avente base {self.lato} ed altezza {self.lato}!\n")
        for riga in range(1, self.lato + 1):
            for colonna in range(1, riga + 1):
                if riga == self.lato or colonna == 1 or riga == colonna:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo {self.nome} vale: {self.getArea()}")
        

        

quadrato = Quadrato(4)
quadrato.render()

print()
rettangolo = Rettangolo(4, 8)
rettangolo.render()

print()
triangolo_rettangolo = Triangolo(4)
triangolo_rettangolo.render()
    



