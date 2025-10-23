'''
Esercizio 1 - Base

Obiettivo: Capire la struttura e l’uso minimo di una classe astratta.

Nome dell’esercizio: FormaGeometrica

Traccia:

- Crea una classe astratta chiamata FormaGeometrica con:

    * un metodo astratto area()
    * un metodo astratto perimetro()

- Crea due classi concrete che la estendono: Rettangolo e Cerchio.

    * Implementa i due metodi per ciascuna forma.
    * Crea e stampa area e perimetro di entrambe.

Suggerimento: usa from abc import ABC, abstractmethod
'''
from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rettangolo(FormaGeometrica):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimetro(self):
        return 2 * (self.a + self.b)
    
    def info(self):
        print(f"Info rettangolo: \nArea: {self.area()}\nPerimetro: {self.perimetro()}")

class Cerchio(FormaGeometrica):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.r
    
    def info(self):
        print(f"Info cerchio: \nArea: {self.area():2.f}\nPerimetro: {self.perimetro():.2f}")

    
rettangolo = Rettangolo(4, 6)
rettangolo.info()       

cerchio = Cerchio(4) 
cerchio.info()