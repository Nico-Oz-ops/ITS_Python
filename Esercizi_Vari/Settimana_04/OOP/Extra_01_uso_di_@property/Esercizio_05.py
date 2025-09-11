'''
Esercizio 5 - Controllo velocità auto

Tema: Python OOP - @property

Obiettivo: Rinforzare l’uso di @property e setter con validazione per valori numerici.

Traccia:

1. Crea una classe Auto con un attributo _velocita (float) che rappresenta la velocità in km/h.

2. Esporre l’attributo tramite @property e setter, assicurandoti che:

    * Il valore sia un numero (int o float).
    * La velocità sia compresa tra 0 e 300 km/h.

3. Implementa __str__ per stampare la velocità attuale dell’auto.

4. Crea un oggetto Auto e prova a modificare la velocità tramite il setter, testando valori validi e non validi.

Suggerimento:

* Usa la logica di validazione direttamente nel setter.
* Assegna il valore iniziale nell’__init__ passando dal setter per applicare subito la validazione.
'''
class Auto:
    def __init__(self, velocita: int|float):
        self.velocita = velocita
    
    @property
    def velocita(self):
        return self._velocita
    
    @velocita.setter
    def velocita(self, velocita: int|float):
        if not isinstance(velocita, (int, float)) or velocita < 0 or velocita > 300:
            raise ValueError("Valore di velocità non valido.")
        self._velocita = velocita
    
    def __str__(self):
        return f"Velocità attuale del veiculo: {self.velocita} Km/h"

# test di un valore di velocità compreso tra 0 e 300
auto1 = Auto(125)
print(auto1)

# invece per testare l'errore:
try:
    auto2 = Auto(350)
    print(auto2)
    
except ValueError as errore:
    print(errore)
