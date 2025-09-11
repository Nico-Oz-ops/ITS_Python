'''
Esercizio 8 - Triangolo rettangolo

Tema: Python OOP - @property

Obiettivo: Proprietà calcolate dinamicamente con più attributi collegati.

Traccia:

1. Crea una classe TriangoloRettangolo con attributi _base e _altezza.

2. Esporre base e altezza tramite @property e setter (>0).

3. Aggiungi proprietà calcolate:

    * ipotenusa (teorema di Pitagora)
    * area = 0.5 * base * altezza

4. Implementa __str__ per stampare base, altezza, ipotenusa e area.

Suggerimento:

* Usa math.sqrt() per calcolare l’ipotenusa.
'''
import math

class TriangoloRettangolo:
    def __init__(self, base: int|float, altezza: int|float):
        self.base = base
        self.altezza = altezza
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base: int|float):
        if not isinstance(base, (int, float)) or base <= 0:
            raise ValueError("Base non valida")
        self._base = base
    
    @property
    def altezza(self):
        return self._altezza
    
    @altezza.setter
    def altezza(self, altezza: int|float):
        if not isinstance(altezza, (int, float)) or altezza <= 0:
            raise ValueError("Altezza non valida")
        self._altezza = altezza
    
    @property
    def ipotenusa(self):
        return math.sqrt(self.altezza ** 2 + self.base ** 2)
    
    @property
    def area(self):
        return 0.5 * self.altezza * self.base
    
    def __str__(self):
        return f"Caratteristiche del triangolo rettangolo:\n"\
        f"Base: {self.base}\n"\
        f"Altezza: {self.altezza}\n"\
        f"Ipotenusa: {self.ipotenusa}\n"\
        f"Area: {self.area}"

triarett1 = TriangoloRettangolo(2.5, 6)
print(triarett1)

print("-" * 50)

try:
    triarett2 = TriangoloRettangolo(4, -5)
    print(triarett2)

except ValueError as error:
    print(error)