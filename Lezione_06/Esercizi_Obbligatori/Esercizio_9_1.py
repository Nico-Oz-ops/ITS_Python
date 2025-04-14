# Esercizio 9.1
'''
Ristorante: crea una classe chiamata Ristorante. Il metodo __init__() per Ristorante
dovrebbe memorizzare due attributi: un restaurant_name e un cuisine_type. Crea un metodo
chiamato describe_restaurant() che stampi queste due informazioni e un metodo chiamato open_restaurant()
che stampi un messaggio che indica che il ristorante è aperto. Crea un'istanza chiamata ristorante dalla tua
classe. Stampa i due attributi singolarmente e poi chiama entrambi i metodi.
'''

class Ristorante:

    def __init__(self, restaurante_name:str, cuisine_type:str):
        self.restaurante_name = restaurante_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nNome Ristorante: {self.restaurante_name}\nTipo di Cucina: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("\nIl ristorante è aperto!")
        
if __name__ == "__main__":

    rest = Ristorante("La Buhaiola Ricorsiva", "italiano")
    rest.describe_restaurant()
    rest.open_restaurant()
