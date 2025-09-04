'''
Esercizio 1 - Versi degli animali (base)

Tema: Override di metodi
Obiettivo: Dimostrare polimorfismo semplice.

Traccia:
    * Crea una classe Animale con un metodo verso().
    * Crea le sottoclassi Cane, Gatto, Mucca che implementano verso() in modo diverso.
    * Crea una lista con istanze miste e, con un unico ciclo, stampa i versi di tutti.
'''
from abc import ABC, abstractmethod

class Animale(ABC):

    @abstractmethod
    def verso(self):
        pass

class Cane(Animale):
    def verso(self):
        return "Bau!....Bau!...Auuu!"

class Gatto(Animale):
    def verso(self):
        return "Brrrr....miau...comida"

class Mucca(Animale):
    def verso(self):
        return "MmmmuuuuuuUuuu..."

animali = [Cane(), Gatto(), Mucca()]
for animale in animali:
    print(f"{animale.__class__.__name__}: {animale.verso()}")
