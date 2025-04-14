# Esercizio 9.3
'''
Utenti: crea una classe chiamata User. Crea due attributi chiamati first_name e last_name, 
quindi crea altri attributi che sono solitamente memorizzati in un profilo utente. 
Crea un metodo chiamato describe_user() che stampa un riepilogo delle informazioni dell'utente. 
Crea un altro metodo chiamato greet_user() che stampa un saluto personalizzato all'utente. 
Crea diverse istanze che rappresentano utenti diversi e chiama entrambi i metodi per ogni utente
'''

class User:

    def __init__(self, first_name:str, last_name:str, age:int, genre: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre

    def describe_user(self):
        print(f"\nNome: {self.first_name}\nCognome: {self.last_name}\nEtà: {self.age} anni\nGenere: {self.genre}")
    
    def greet_user(self):
        print(f"\nCiao, {self.first_name} {self.last_name}, come va oggi? Come posso aiutarti?")

pepe = User("Pepe", "Cortisona", 49, "Maschio")
pepe.describe_user()
pepe.greet_user()
print("-" * 60)

buha = User("Buhaiola", "Pig", 345, "Non definito")
buha.describe_user()
buha.greet_user()
print("-" * 60)

lolo = User("Lolo", "Pancrazio", 14, "Maschio")
lolo.describe_user()
lolo.greet_user()