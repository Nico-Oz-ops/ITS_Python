# Esercizio 9_4
'''
Numero servito: inizia con il tuo programma dall'esercizio 9-1. 
Aggiungi un attributo chiamato number_served con un valore predefinito di 0. 
Crea un'istanza chiamata restaurant da questa classe. Stampa il numero di clienti 
serviti dal ristorante, quindi modifica questo valore e stampalo di nuovo. 
Aggiungi un metodo chiamato set_number_served() che ti consente di impostare il numero 
di clienti serviti. Chiama questo metodo con un nuovo numero e stampa di nuovo il valore. 
Aggiungi un metodo chiamato increment_number_served() che ti consente di incrementare il 
numero di clienti serviti. Chiama questo metodo con qualsiasi numero tu voglia che potrebbe 
rappresentare quanti clienti sono stati serviti in, ad esempio, un giorno lavorativo. 
'''

# from Esercizio_9_1 import Ristorante

# rest = Ristorante("La Buhaiola Ricorsiva", "italiano")
# rest.number_served = 0

# print(rest.describe_restaurant())
# print(rest.number_served)

class Ristorante:

    def __init__(self, restaurante_name:str, cuisine_type:str, number_served:int=0):
        self.restaurante_name = restaurante_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"\nNome Ristorante: {self.restaurante_name}\nTipo di Cucina: {self.cuisine_type}\nNumero di Clienti: {self.number_served}")
    
    def open_restaurant(self):
        print("\nIl ristorante è aperto!")
    
    def set_number_served(self, number_served:int) -> None:
        self.number_served = number_served
    
    def increment_number_served(self, number_served:int) -> None:
        self.number_served += number_served


rest = Ristorante("La Buhaiola Ricorsiva", "italiano", number_served = 0)
rest.describe_restaurant()
rest.open_restaurant()

rest.set_number_served(45)
rest.describe_restaurant()

rest.increment_number_served(15)
rest.describe_restaurant()
