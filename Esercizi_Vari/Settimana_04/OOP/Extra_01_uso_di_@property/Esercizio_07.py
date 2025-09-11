'''
Esercizio 7 - Cerchio

Tema: Python OOP - @property

Obiettivo: Proprietà calcolate dinamicamente da un singolo attributo.

Traccia:

1. Crea una classe Cerchio con attributo _raggio.

2. Esporre il raggio tramite @property e setter (raggio >0).

3. Aggiungi proprietà calcolate:

    * area = π * raggio²
    * circonferenza = 2 * π * raggio

4. Implementa __str__ per stampare raggio, area e circonferenza.

5. Crea un oggetto cerchio e prova a modificare il raggio tramite setter.

Suggerimento:

* Usa il modulo math per π.
'''
import math

class Cerchio:
    def __init__(self, raggio: int|float):
        self.raggio = raggio
    
    @property
    def raggio(self):
        return self._raggio
    
    @raggio.setter
    def raggio(self, raggio: int|float):
        if not isinstance(raggio, (int, float)) or raggio <= 0:
            raise ValueError("Valore di raggio non valido")
        self._raggio = raggio
    
    @property
    def area(self):
        return math.pi * (self._raggio ** 2)
    
    @property
    def circonferenza(self):
        return 2 * (math.pi * self._raggio)

    def __str__(self):
        return f"Cerchio:\nRaggio: {self.raggio}\nCirconferenza: {self.circonferenza:.2f}\nArea: {self.area:.2f}\n"

cerchio1 = Cerchio(4.5)
print(cerchio1)

try:
    cerchio2 = Cerchio(-3)
    print(cerchio2)

except ValueError as error:
    print(error)