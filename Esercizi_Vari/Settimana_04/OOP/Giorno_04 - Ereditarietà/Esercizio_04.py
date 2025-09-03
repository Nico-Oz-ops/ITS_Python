'''
Esercizio 4 - Forma base e Cerchio

Tema: Polimorfismo tra più sottoclassi
Obiettivo: Stesso metodo con comportamenti diversi

Traccia:

1. Crea una classe base Forma con:
    *Metodo area() che restituisce 0.

2. Crea una sottoclasse Rettangolo che:
    * Eredita da Forma.
    * Ha attributi base e altezza.
    * Sovrascrive il metodo area() per restituire base * altezza.

3. Crea una sottoclasse Cerchio che:
    * Eredita da Forma.
    * Ha attributo raggio.
    * Sovrascrive il metodo area() per calcolare l’area del cerchio usando la formula π * raggio**2.

4. Crea una lista di oggetti forme contenente istanze di Rettangolo e Cerchio.

5. Itera sulla lista e stampa l’area di ogni forma chiamando semplicemente il 
   metodo area() (dimostrando il polimorfismo).

Suggerimento: puoi usare import math per ottenere math.pi.
'''

import math

class Forma:
    def area(self):
        return 0

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self):
        return f"Area rettangolo: {self.base * self.altezza:.2f}"

class Cerchio(Forma):
    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = raggio
    
    def area(self):
        return f"Area cerchio: {math.pi * (self.raggio ** 2):.2f}"

forme = [Rettangolo(4, 2), Cerchio(5), Cerchio(3), Rettangolo(2, 9)]

for forma in forme:
    print(forma.area())

# Suggerimento di Chat per una stampa più pythonica

# Classe base
class Forma:
    def area(self) -> float:
        return 0.0

# Sottoclasse Rettangolo
class Rettangolo(Forma):
    def __init__(self, base: float, altezza: float):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self) -> float:
        return self.base * self.altezza

# Sottoclasse Cerchio
class Cerchio(Forma):
    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = raggio
    
    def area(self) -> float:
        return math.pi * (self.raggio ** 2)

# Lista di oggetti Forma
forme = [Rettangolo(4, 2), Cerchio(5), Cerchio(3), Rettangolo(2, 9)]

# Stampa le aree usando polimorfismo
for forma in forme:
    print(f"{forma.__class__.__name__} area: {forma.area():.2f}")
    
