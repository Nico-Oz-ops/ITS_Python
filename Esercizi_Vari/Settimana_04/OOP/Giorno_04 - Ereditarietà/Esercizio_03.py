'''
Esercizio 3 - Forma base e Rettangolo

Tema: Sovrascrittura di metodi (override)
Obiettivo: Polimorfismo semplice con metodi condivisi

Traccia:

    * Classe Forma con metodo area() che restituisce 0.

    * Sottoclasse Rettangolo con attributi base e altezza, override di area() per calcolare l’area reale.

    * Testare con un rettangolo e stampare l’area.
'''
class Forma:
    def area(self) -> int:
        return 0

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int):
        super().__init__()

        self.base = base
        self.altezza = altezza
    
    def area(self):
        return super().area() + (self.base * self.altezza)
    # siccome la base è sempre 0 (metodo area nella class Forma che restituisce 0), potrei scrivere:
    # return self.base * self.altezza

rettangolo = Rettangolo(5, 2)
print(rettangolo.area())