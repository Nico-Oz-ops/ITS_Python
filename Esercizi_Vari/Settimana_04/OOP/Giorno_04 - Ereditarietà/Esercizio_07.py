'''
Esercizio 7 - Figure geometriche (esteso)

Partendo da Forma con metodo area(), implementa:

    * Rettangolo (base, altezza)
    * Cerchio (raggio)
    * Triangolo (base, altezza → area = base * altezza / 2)

Crea una lista di forme e stampa tutte le aree usando un loop unico.
'''
import math

# Metodo 1
class Forma:
    def area(self) -> int|float:
        return 0
    
class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self) -> int|float:
        return f"Area rettangolo: {self.base * self.altezza:.2f}"
    
class Cerchio(Forma):
    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = raggio
    
    def area(self) -> float:
        return f"Area cerchio: {math.pi * (self.raggio ** 2):.2f}"

class Triangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self) -> int|float:
        return f"Area triangolo: {(self.base * self.altezza) / 2:.2f}"

forme = [Rettangolo(5, 4), Cerchio(6), Triangolo(8, 6), Rettangolo(2, 7), Cerchio(2.5), Triangolo(4, 9)]
for forma in forme:
    print(forma.area())

'''        
Chat suggerisce che la stampa formattata si faccia nel ciclo for piuttosto che nel metodo area(), perciò:
print(f"{forma.__class__.__name__}: {forma.area():.2f}")

{forma.__class__.__name__}

    * forma -> è l’oggetto corrente (es. Rettangolo(5,4)).
    * forma.__class__ -> restituisce la classe dell’oggetto (Rettangolo, Cerchio, Triangolo).
    * forma.__class__.__name__ -> restituisce il nome della classe come stringa.
'''

# Metodo 2 - stampa formattata nel ciclo for
class Forma:
    def area(self) -> int|float:
        return 0
    
class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self) -> int|float:
        return self.base * self.altezza
    
class Cerchio(Forma):
    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = raggio
    
    def area(self) -> float:
        return math.pi * (self.raggio ** 2)

class Triangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def area(self) -> int|float:
        return (self.base * self.altezza) / 2

forme = [Rettangolo(5, 4), Cerchio(6), Triangolo(8, 6), Rettangolo(2, 7), Cerchio(2.5), Triangolo(4, 9)]
for forma in forme:
    print(f"Area {forma.__class__.__name__}: {forma.area():.2f}")