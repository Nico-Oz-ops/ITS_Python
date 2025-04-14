# Esercizio 9.5
'''
Tentativi di accesso: aggiungi un attributo denominato login_attempts alla tua 
classe User dall'esercizio 9-3. Scrivi un metodo denominato increment_login_attempts() 
che incrementa il valore di login_attempts di 1. Scrivi un altro metodo denominato reset_login_attempts() 
che reimposta il valore di login_attempts a 0. Crea un'istanza della classe User e 
chiama increment_login_attempts() più volte. Stampa il valore di login_attempts per assicurarti che sia 
stato incrementato correttamente, quindi chiama reset_login_attempts(). 
Stampa nuovamente login_attempts per assicurarti che sia stato reimpostato a 0.
'''

class User:

    def __init__(self, first_name:str, last_name:str, age:int, genre: str, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\nNome: {self.first_name}\nCognome: {self.last_name}\nEtà: {self.age} anni\nGenere: {self.genre}\nTentativo di Accesso: {self.login_attempts}")
    
    def greet_user(self):
        print(f"\nCiao, {self.first_name} {self.last_name}, come va oggi? Come posso aiutarti?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

gino = User("Gino", "Rossi", 65, "maschio", 2)
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.describe_user()

print("-" * 50)

gino.reset_login_attempts()
gino.describe_user()