# Esercizio 9.2
'''
Tre ristoranti: inizia con la classe dell'esercizio 9-1. 
Crea tre istanze diverse dalla classe e chiama describe_restaurant() per ogni istanza.
'''
class Ristorante:

    def __init__(self, restaurante_name:str, cuisine_type:str):
        self.restaurante_name = restaurante_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nNome Ristorante: {self.restaurante_name}\nTipo di Cucina: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("\nIl ristorante è aperto!")

rest_2 = Ristorante("Nicolino Salchichòn", "cileno")
rest_2.describe_restaurant()
rest_3 = Ristorante("La Puzzona Mangia Bene", "americana")
rest_3.describe_restaurant()
rest_4 = Ristorante("Patacones express", "panamense")
rest_4.describe_restaurant()


