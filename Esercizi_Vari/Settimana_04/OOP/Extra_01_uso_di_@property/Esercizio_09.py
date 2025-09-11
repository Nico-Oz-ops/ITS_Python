'''
Esercizio 9 - Cubo

Tema: Python OOP - @property

Obiettivo: Proprietà calcolate dinamicamente (3D).

Traccia:

1. Crea una classe Cubo con attributo _lato.

2. Esporre lato tramite @property e setter (>0).

3. Aggiungi proprietà calcolate:

    * volume = lato³
    * superficie = 6 * lato²

4. Implementa __str__ per stampare lato, volume e superficie.

Suggerimento:

* Setter utilizzato anche nell’__init__.
'''

class Cubo:
    def __init__(self, lato: int|float):
        self.lato = lato

    @property
    def lato(self):
        return self._lato
    
    @lato.setter
    def lato(self, lato: int|float):
        if not isinstance(lato, (int, float)) or lato <= 0:
            raise ValueError("Lato non valido")
        self._lato = lato
    
    @property
    def volume(self):
        return self.lato ** 3
    
    @property
    def superficie(self):
        return 6 * (self.lato ** 2)

    def __str__(self):
        return f"Caratteristiche di un cubo:\n"\
        f"Lato: {self.lato}\nVolume: {self.volume:.2f}\nSuperficie: {self.superficie:.2f}"

cubo1 = Cubo(5)
print(cubo1)

try: 
    
    cubo2 = Cubo(0)
    print(cubo2)

except ValueError as error:
    print(error)
