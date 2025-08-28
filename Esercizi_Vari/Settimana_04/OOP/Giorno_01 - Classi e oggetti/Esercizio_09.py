'''
Tema: Attributi booleani e metodi
Obiettivo: Gestire stato interno ON/OFF

Nome: Lampadina

Traccia:
Crea una classe Lampadina con attributo accesa inizializzato a False.
Aggiungi metodi accendi(), spegni() e stato() che restituisce "accesa" o "spenta".
Testa la lampadina accendendola, spegnendola e controllando lo stato.
'''

class Lampadina:

    def __init__(self, accesa: bool = False):
        self.accesa = accesa
    
    def accendi(self):
        self.accesa = True
    
    def spegni(self):
        self.accesa = False

    def stato(self):
        return "accesa" if self.accesa else "spenta"

lamp = Lampadina()
print(lamp.stato())

lamp.accendi()
print(lamp.stato())

lamp.spegni()
print(lamp.stato())
