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

Gestire gli errori, validare gli input e aggiungere una nuova forma (triangolo).
'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimiter(self):
        pass

def numero_valido(valore, nome):
    try:
        valore = float(valore)
        if valore <= 0:
            raise ValueError(f"'{nome}' deve essere un valore positivo")
        return valore
    
    except ValueError as e:
        print(f"Errore: {e}")
        return None

class Circle(Shape):

    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = numero_valido(raggio, "Raggio")
        if self.raggio is None:
            raise ValueError("'Raggio' non valido")
    
    def Area(self):
        return math.pi * self.raggio ** 2
    
    def Perimiter(self):
        return 2 * math.pi * self.raggio

class Rectangle(Shape):

    def __init__(self, base: float, altezza: float):
        super().__init__()
        self.base = numero_valido(base, "Base")
        self.altezza = numero_valido(altezza, "Altezza")
        if self.base is None or self.altezza is None:
            raise ValueError("Dimensioni non valide")
    
    def Area(self):
        return self.base * self.altezza
    
    def Perimiter(self):
        return (self.base + self.altezza) * 2

class Triangolo(Shape):

    def __init__(self, base: float, altezza: float, lato1: float, lato2: float, lato3: float):
        super().__init__()
        self.altezza = numero_valido(altezza, "Altezza")
        self.base = numero_valido(base, "Base")
        self.lato1 = numero_valido(lato1, "Lato1")
        self.lato2 = numero_valido(lato2, "Lato2")
        self.lato3 = numero_valido(lato3, "Lato3")

        if None in [self.base, self.altezza, self.lato1, self.lato2, self.lato3]:
            raise ValueError("Dimensioni non valide")
    
    def Area(self):
        return 0.5 * self.base * self.altezza
    
    def Perimiter(self):
        return self.lato1 + self.lato2 + self.lato3
        

# Programma driver (codice di test)
def main():
    try:

        cerchio = Circle(3)
        print("Cerchio")
        print(f"Area: {cerchio.Area(): .2f}")
        print(f"Perimetro: {cerchio.Perimiter(): .2f}")

        print("-" * 25)

        rettangolo = Rectangle(5, -6)
        print("Rettangolo")
        print(f"Area: {rettangolo.Area(): .2f}")
        print(f"Perimetro: {rettangolo.Perimiter(): .2f}")

        print("-" * 25)

        triangolo = Triangolo(6, 4, 6, 8, 10)
        print("Triangolo")
        print(f"Area: {triangolo.Area(): .2f}")
        print(f"Perimetro: {triangolo.Perimiter(): .2f}")
    
    except ValueError as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()