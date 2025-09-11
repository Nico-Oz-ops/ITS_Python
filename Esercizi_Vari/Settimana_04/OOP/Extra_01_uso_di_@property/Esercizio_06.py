'''
Esercizio 6 - Rettangolo avanzato

Tema: Python OOP - @property

Obiettivo: Gestire proprietà calcolate dinamicamente.

Traccia:

1. Crea una classe Rettangolo con attributi _larghezza e _altezza.

2. Esporre larghezza e altezza tramite @property e setter con validazione (>0).

3. Aggiungi proprietà calcolate area e perimetro (solo getter).

4. Implementa __str__ per stampare larghezza, altezza, area e perimetro.

5. Crea un oggetto rettangolo e prova a modificare larghezza o altezza tramite setter.

Suggerimento:

* Usa i setter anche nell’__init__ per applicare la validazione fin dall’inizio.
'''
class Rettangolo:
    def __init__(self, larghezza: int|float, altezza: int|float):
        self.larghezza = larghezza
        self.altezza = altezza
    
    @property
    def larghezza(self):
        return self._larghezza
    
    @larghezza.setter
    def larghezza(self, larghezza: int|float):
        if not isinstance(larghezza, (int, float)) or larghezza <= 0:
            raise ValueError("Valore di larghezza non valido")
        self._larghezza = larghezza
    
    @property
    def altezza(self):
        return self._altezza 
    
    @altezza.setter
    def altezza(self, altezza: int|float):
        if not isinstance(altezza, (int, float)) or altezza <= 0:
            raise ValueError("Valore di altezza non valido")
        self._altezza = altezza
    
    @property
    def area(self):
        return self._larghezza * self._altezza
    
    @property
    def perimetro(self):
        return 2 * (self._larghezza + self._altezza)
    
    def __str__(self):
        return f"Caratteristiche del rettangolo:\n"\
        f"Altezza: {self.altezza}\nLarghezza: {self.larghezza}\nArea: {self.area}\nPerimetro: {self.perimetro}"

rettangolo1 = Rettangolo(5.5, 10)
print(rettangolo1)

try:
    rettangolo2 = Rettangolo(-5, 3)
    print(rettangolo2)

except ValueError as error:
    print(error)