# Esercizio 01

'''
Esercizio 1: Creazione di una classe astratta con metodi astratti

Iniziamo definendo una classe base astratta chiamata Shape. 
Questa classe dovrebbe includere due metodi astratti : uno chiamato area, 
che sarà responsabile del calcolo dell'area di una forma, e un altro chiamato perimeter, 
che calcolerà il perimetro. Poiché Shape è astratta, non fornirà implementazioni specifiche per questi metodi. 
Invece, imposta un modello per tutte le forme che erediteranno da essa.

Quindi, create due sottoclassi concrete , Circle e Rectangle , che estendono entrambe la classe Shape. 
Ognuna di queste sottoclassi deve fornire la propria implementazione dei metodi area e perimetro, 
basata sulle formule geometriche appropriate alle proprie forme.

Infine, scrivi un semplice programma driver (codice di test) che crei istanze di Circle e Rectangle, 
chiami i loro metodi area e perimetro e stampi i risultati. Questo ti aiuterà a verificare che la gerarchia 
delle classi funzioni come previsto.
'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Permiter(self):
        pass

class Circle(Shape):

    def __init__(self, raggio: float):
        super().__init__()

        self.raggio = raggio
    
    def Area(self):
        return math.pi * self.raggio ** 2
    
    def Permiter(self):
        return 2 * math.pi * self.raggio

class Rectangle(Shape):

    def __init__(self, base: float, altezza: float):
        super().__init__()

        self.base = base
        self.altezza = altezza
    
    def Area(self):
        return self.base * self.altezza
    
    def Permiter(self):
        return (self.base + self.altezza) * 2

# Programma driver (codice di test)
def main():

    cerchio = Circle(3)
    print("Cerchio")
    print(f"Area: {cerchio.Area(): .2f}")
    print(f"Perimetro: {cerchio.Permiter(): .2f}")

    print("-" * 25)

    rettangolo = Rectangle(5, 6)
    print("Rettangolo")
    print(f"Area: {rettangolo.Area(): .2f}")
    print(f"Perimetro: {rettangolo.Permiter(): .2f}")

if __name__ == "__main__":
    main()


        

