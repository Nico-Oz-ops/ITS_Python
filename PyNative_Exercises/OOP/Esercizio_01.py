# Esercizio 1
'''
Creare una classe con attributi di istanza:
Scrivi un programma Python per creare una 
classe Vehicle con attributi max_speed di mileage istanza.
'''

class Vehicle:

    def __init__(self, max_speed:float, mileage:float):
        self.max_speed = max_speed
        self.mileage = mileage
    
    # def __str__(self):
    #     return f"Velocità massima: {self.max_speed}km/hr\nChilometraggio: {self.mileage}km "
    
    def __call__(self):
        if self.max_speed <= 30:
            return "Velocità adatta a centri urbani"
        elif 30 < self.max_speed <= 90:
            return "Velocità adatta a strada statale"
        else:
            return "Velocità adatta a autostrada"

veh = Vehicle(130, 20000)
print(veh())

        