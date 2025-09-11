'''
Esercizio 1 - Calcolo automatico di un attributo

Tema: @property base
Obiettivo: Creare un attributo calcolato usando @property.

Nome dell’esercizio: Area del rettangolo

Traccia:

1. Crea una classe Rettangolo che abbia:

    * attributi larghezza e altezza (passati al costruttore)

    * un metodo area decorato con @property che restituisce l’area del rettangolo.

Suggerimento: L’uso di @property permette di accedere al metodo come se fosse 
un attributo: r.area invece di r.area().
'''
class Rettangolo:
    def __init__(self, larghezza: int, altezza: int):
        self.larghezza = larghezza
        self.altezza = altezza
    
    @property
    def area(self):
        return self.larghezza * self.altezza

rettangolo = Rettangolo(5, 6)
print(f"Area del rettangolo: {rettangolo.area}")