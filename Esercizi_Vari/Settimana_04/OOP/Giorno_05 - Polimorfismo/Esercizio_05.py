'''
Esercizio 5 - Figure geometriche avanzate (versione definitiva)

Tema: Polimorfismo + ereditarietà
Obiettivo: Calcolare aree e perimetri usando metodi comuni tra classi diverse.

Traccia:
1. Definisci una superclasse astratta FiguraGeometrica con due metodi astratti:

    * area()
    * perimetro()

2. Implementa le seguenti sottoclassi che ereditano da FiguraGeometrica:

    * Rettangolo (base, altezza)
    * Cerchio (raggio)
    * Triangolo (lati: a, b, c e base/altezza per l’area, oppure usa la formula di Erone).

3. Per ogni classe implementa i metodi area() e perimetro() in modo coerente con la figura.
4. Crea una lista contenente istanze di figure diverse.
5. Usa un unico ciclo per stampare area e perimetro di ciascuna figura.
'''

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rettangolo(FiguraGeometrica):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza 
    
    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return (self.base + self.altezza) * 2

class Cerchio(FiguraGeometrica):
    def __init__(self, raggio: int|float):
        super().__init__()
        self.raggio = raggio

    def area(self):
        return math.pi * (self.raggio ** 2)
    
    def perimetro(self):
        return 2 * (math.pi * self.raggio)

class Triangolo(FiguraGeometrica):
    def __init__(self, base: int, altezza: int, lato_a: int, lato_b: int, lato_c: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
        self.lato_a = lato_a
        self.lato_b = lato_b
        self.lato_c = lato_c
    
    def area(self) -> int:
        return (self.base * self.altezza) / 2
    
    def perimetro(self) -> int:
        return self.lato_a + self.lato_b + self.lato_c

figure = [
    Rettangolo(6, 8), 
    Cerchio(3.65), 
    Triangolo(4, 6, 6, 5, 4)
    ]

for figura in figure:
    print(f"**{figura.__class__.__name__}**\nArea: {figura.area():.2f}\nPerimetro: {figura.perimetro():.2f}\n")



'''
Per l'area del triangolo usando la formula di Erone, se ho tutti i lati (non sono necessari base e altezza):
         -------------------------
Area = \/s x (s-a) x (s-b) x (s-c)

dove s:
s = a + b + c / 2


def area(self):
    s = (self.lato_a + self.lato_b + self.lato_c) / 2
    return math.sqrt(s * (s - self.lato_a) * (s - self.lato_b) * (s - self.lato_c))
'''