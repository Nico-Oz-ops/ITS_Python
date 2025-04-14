# Esercizio 9.11
'''
Amministrazione importata: crea un modulo users.py contenente tre classi:

Utente: memorizza nome, cognome, nome utente ed email; include i metodi describe_user() e greet_user().
Privilegi: contiene un elenco di privilegi e un metodo show_privileges() per visualizzarli.
Admin: memorizza un'istanza Utente e un'istanza Privilegi come attributi.
In un file separato main.py, importa le classi, crea un'istanza User e un'istanza Privileges, 
passale ad Admin e chiama describe_user() e show_privileges() per verificare che tutto funzioni correttamente.
'''

class User:

    def __init__(self, nome:str, cognome:str, username:str, email:str):
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.email = email
    
    def describe_user(self):
        return f"\nNome: {self.nome}\nCognome: {self.cognome}\nUsername: {self.username}\nEmail: {self.email}\nPrivilegi:"
    
    def greet_user(self):
        return f"\nCiao, {self.nome} {self.cognome}, come va oggi? Come posso aiutarti?"
    
class Privilegi:

    def __init__(self, privilegi=None):
        if privilegi is None:
            privilegi = ["accesso a tutto", "fai quello che vuoi"]
        self.privilegi = privilegi
    
    def show_privileges(self):
        return "\n".join(f"- {privilegio}" for privilegio in self.privilegi)

class Admin:

    def __init__(self, utente, privilegi):
        self.utente = utente
        self.privilegi = privilegi
    
    def describe_user(self):
        return self.utente.describe_user()

    def show_privileges(self):
        return self.privilegi.show_privileges()





        