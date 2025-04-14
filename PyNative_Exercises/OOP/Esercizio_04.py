# Esercizio 4
'''
Ereditarietà delle classi
Crea una classe Bus che erediti dalla classe Vehicle. 
Assegna all'argomento capacità Bus.seating_capacity() il valore predefinito di 50.

Utilizzare il seguente codice per la classe Vehicle padre.
'''

class Vehicle:

    def __init__(self, name:str, max_speed:int, mileage:int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity:int):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=35)

bus = Bus("Volvo", 150, 8000)
print(bus.seating_capacity())



        