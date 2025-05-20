# Esercizio 1
'''
Crea una classe astratta chiamata Figura, che rappresenta una figura geometrica.
Deve contenere un metodo astratto chiamato calcola_area() (non deve avere codice dentro, solo la dichiarazione).
Crea una classe chiamata Rettangolo, che estende Figura.
Deve avere due attributi: base e altezza.
Deve implementare il metodo calcola_area() che restituisce l'area del rettangolo (base × altezza).
Crea una seconda classe chiamata Quadrato, che estende anche lei Figura.
Deve avere un solo attributo: lato.
Deve implementare il metodo calcola_area() che restituisce l’area del quadrato (lato × lato).
Nel programma principale:
Crea un oggetto Rettangolo con base 4 e altezza 5.
Crea un oggetto Quadrato con lato 3.
Stampa l’area di ciascuna figura
'''

from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def calcola_area(self) -> None:
        pass

class Rettangolo(Figura):

    def __init__(self, base:float, altezza:float):
        self.base = base
        self.altezza = altezza
    
    def calcola_area(self):
        return self.base * self.altezza

class Quadrato(Figura):

    def __init__(self, lato):
        super().__init__()
        self.lato = lato
    
    def calcola_area(self):
        return self.lato * self.lato

# oggetto rettangolo 
rettangolo:Rettangolo = Rettangolo(4, 5)
print(f"L'area del rettangolo è: {rettangolo.calcola_area()}")

# oggetto quadrato
quadrato:Quadrato = Quadrato(3)
print(f"L'area del quadrato è: {quadrato.calcola_area()}")