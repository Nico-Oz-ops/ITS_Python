'''
Tema: Creazione di una classe semplice
Obiettivo: Imparare a definire una classe e creare istanze.

Nome: Automobile

Traccia:
Crea una classe Automobile con due attributi: marca e modello.
Istanzia almeno due oggetti diversi e stampali.
'''
# Alternativa 1
class Automobile:
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello

auto1 = Automobile("Nissan", "X-Trail")
auto2 = Automobile("Porsche", "911")

print(f"Auto 1: {auto1.marca}, {auto1.modello}\nAuto 2: {auto2.marca}, {auto2.modello}")
        

# Alternativa 2
class Automobile:

    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello
    
    def get_marca(self):
        return self.marca
    
    def get_modello(self):
        return self.modello

# Creazione di oggetti

auto1 = Automobile("Nissan", "X-Trail")
auto2 = Automobile("Porsche", "911")

print(f"Automobile_1: {auto1.get_marca()}, {auto1.get_modello()}\nAutomobile_2: {auto2.get_marca()}, {auto2.get_modello()}")
    
    