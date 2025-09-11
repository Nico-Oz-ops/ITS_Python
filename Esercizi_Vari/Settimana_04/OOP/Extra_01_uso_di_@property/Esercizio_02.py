'''
Esercizio 2 - Validazione con setter

Tema: @property con getter e setter
Obiettivo: Impedire valori negativi modificando un attributo tramite un setter.

Nome dell’esercizio: Età con controllo

Traccia:
1. Crea una classe Persona che abbia:

    * un attributo privato _eta

    * una proprietà eta con getter e setter

    * il setter deve lanciare un ValueError se l’età è negativa

Suggerimento:
Usa @property per il getter e @eta.setter per il setter.
'''
class Persona:
    def __init__(self, eta: int):
        self._eta = eta
    
    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self, eta: int):
        if not isinstance(eta, int) or eta < 0:
            raise ValueError("Il valore dell'età non è valido")
        self._eta = eta

juan = Persona(25)
print(f"L'età di Juan è {juan.eta}")