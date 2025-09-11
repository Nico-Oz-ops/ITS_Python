'''
Esercizio 10 - Controllo rettangolo modificabile

Tema: Python OOP - @property

Obiettivo: Proprietà calcolate con aggiornamento dinamico e validazioni multiple.

Traccia:

1. Crea una classe RettangoloModificabile con _larghezza e _altezza.

2. Esporre larghezza e altezza tramite @property e setter con validazione (>0).

3. Aggiungi proprietà calcolate:

    * area
    * perimetro
    * diagonale (teorema di Pitagora)

4. Implementa __str__ per stampare larghezza, altezza, area, perimetro e diagonale.

5. Crea un oggetto rettangolo modificabile e prova a cambiare larghezza/altezza tramite setter, 
    verificando aggiornamenti automatici di tutte le proprietà.

Suggerimento:

* Usa math.sqrt() per la diagonale.
'''
import math

class RettangoloModificabile:
    def __init__(self, larghezza: int|float, altezza: int|float):
        self.larghezza = larghezza
        self.altezza = altezza
    
    @property
    def larghezza(self):
        return self._larghezza
    
    @larghezza.setter
    def larghezza(self, larghezza: int|float):
        if not isinstance(larghezza, (int, float)) or larghezza <= 0:
            raise ValueError("Larghezza non valida.")
        self._larghezza = larghezza
    
    @property
    def altezza(self):
        return self._altezza
    
    @altezza.setter
    def altezza(self, altezza: int|float):
        if not isinstance(altezza, (int, float)) or altezza <= 0:
            raise ValueError("Altezza non valida.")
        self._altezza = altezza
    
    @property
    def area(self):
        return self.larghezza * self.altezza
    
    @property
    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)
    
    @property
    def diagonale(self):
        return math.sqrt(self.larghezza ** 2 + self.altezza ** 2)
    
    def __str__(self):
        return f"Caratteristiche di un rettangolo:\n"\
        f"Altezza: {self.altezza}\nLarghezza: {self.larghezza}\nArea: {self.area:.2f}\n"\
        f"Perimetro: {self.perimetro:.2f}\nDiagonale: {self.diagonale:.2f}"

rett1 = RettangoloModificabile(12, 6)
print(rett1)

print("-" * 50)

try:
    rett2 = RettangoloModificabile(2.3, 0)
    print(rett2)

except ValueError as error:
    print(error)

