# Esercizio 3
'''
Creare una classe figlia Bus che erediterà tutte le variabili e i metodi della classe Vehicle.
Creare un oggetto Bus che erediterà tutte 
le variabili e i metodi della classe Vehicle padre e visualizzarlo.
'''

class Vehicle:

    def __init__(self, name:str, max_speed:float, mileage:float):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# class Bus(Vehicle):
    
#     def __str__(self):
#         return super().__str__() + f"\nInformazione riguardo il bus scolastico\nNome: {self.name}\nVelocità Massima: {self.max_speed}k/hr\nChilometraggio: {self.mileage}"

scuola_bus = Bus("Volvo", 150, 8000)
print(f"Dati di bus scolastico:\nNome:{scuola_bus.name}\nVelocità massima:{scuola_bus.max_speed}\nChilometraggio:{scuola_bus.mileage}")
