'''
Esercizio 3 - Gestione di un account social

Tema: Attributi privati e metodi di accesso
Obiettivo: Creare una classe AccountSocial con attributi privati e controlli di sicurezza

Traccia:
Crea una classe AccountSocial con attributi privati:

    * __username (stringa)
    * __password (stringa)

Implementa metodi:

    * get_username() → ritorna l’username
    * set_username(username) → modifica l’username (non vuoto)
    * set_password(password) → modifica la password solo se lunga almeno 8 caratteri, altrimenti lancia ValueError
    * verifica_password(password) → ritorna True se la password corrisponde a quella memorizzata, altrimenti False

Suggerimento:

    * Usa self.__username e self.__password come attributi privati.
    * verifica_password serve come metodo sicuro per controllare la password senza esporla direttamente.
'''
class AccountSocial:
    def __init__(self, username: str, password: str):
        self.set_username(username)
        self.set_password(password)
    
    def get_username(self) -> str:
        return self.__username
    
    # def get_password(self) -> str: # Pratica corretta è: mai restituire la password in chiaro. Pericoloso per motivi di sicurezza 
    #     return self.__password     # e privacy: chiunque abbia accesso all’oggetto può leggerla facilmente. Per questo si crea il metodo "verifica_password"
    
    def set_username(self, username: str):
        if not isinstance(username, str) or username.strip() == "":
            raise ValueError("Errore, username non valido")
        self.__username = username
    
    def set_password(self, password: str):
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError("Errore, password non valida")
        self.__password = password
    
    def verifica_password(self, password: str):
        return self.__password == password
    
    def __str__(self):
        return f"Username: {self.__username}\nPassword: {'*' * len(self.__password)}"

accountsoc = AccountSocial("JuaNito123", "walala159")
print(accountsoc)

print(accountsoc.verifica_password("walalala159"))
print(accountsoc.verifica_password("walala159"))
        