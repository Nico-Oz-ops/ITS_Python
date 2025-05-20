# Esercizio 4
'''
Classe Quadrato
Classe Quadrato con:

Attributo: lato

Metodi:

area() → restituisce l’area del quadrato

perimetro() → restituisce il perimetro
'''

class Quadrato:

    def __init__(self, lato:int):
        self.lato = lato
    
    def area(self) -> int:
        return self.lato * self.lato
    
    def perimetro(self) -> int:
        return self.lato * 4 

quadrato = Quadrato(4)
print(quadrato.area())
print(quadrato.perimetro())

# Variante

class Quadrato:

    def __init__(self, lato:int):
        self.lato = lato
    
    def area(self) -> int:
        return self.lato ** 2
    
    def perimetro(self) -> int:
        return self.lato * 4 
    
    def info(self):
        print(f"Lato: {self.lato}")
        print(f"Area: {self.area()}")
        print(f"Perimetro: {self.perimetro()}")

quadrato = Quadrato(4)
quadrato.info()