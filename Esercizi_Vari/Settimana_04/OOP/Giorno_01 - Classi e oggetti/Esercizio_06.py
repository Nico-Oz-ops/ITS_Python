'''
Tema: Attributi e metodi
Obiettivo: Calcolare proprietà usando metodi

Nome: Rettangolo

Traccia:
Crea una classe Rettangolo con attributi base e altezza.
Aggiungi un metodo area() che restituisce l’area del rettangolo.
Crea due rettangoli e stampa la loro area.
'''

class Rettangolo:

    def __init__(self, base: int, altezza: int):
        self.base = base
        self.altezza = altezza
    
    def area(self):
        area = self.base * self.altezza
        return f"Area di un rettangolo {self.base} x {self.altezza}: {area}"

ret1 = Rettangolo(5, 8)
ret2 = Rettangolo(4, 3)

print(ret1.area())
print(ret2.area())