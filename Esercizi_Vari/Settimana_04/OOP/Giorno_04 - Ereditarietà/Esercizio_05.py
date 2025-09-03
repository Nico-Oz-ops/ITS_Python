'''
Esercizio 5 - Mini-progetto animali

Tema: Ereditarietà + metodi multipli
Obiettivo: Integrazione di più classi con override e attributi specifici

Traccia:

    * Classe base Animale con attributi nome e eta e metodo verso().
    * Sottoclassi Gatto e Cane, override di verso().
    * Aggiungere metodo dormi() comune a tutti gli animali.
    * Creare istanze di Gatto e Cane e chiamare verso() e dormi().
'''

class Animale:
    def __init__(self, nome: str, eta: int):
        self.set_nome(nome)
        self.set_eta(eta)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_eta(self) -> int:
        return self.__eta 
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido.")
        self.__nome = nome
    
    def set_eta(self, eta: int):
        if not isinstance(eta, int) or eta < 0:
            raise ValueError("Età non valida.")
        self.__eta = eta
    
    def verso(self) -> str:
        return "Suono generico"
    
    def dormi(self) -> str:
        return "Zzzzz"
    
    def __str__(self):
        return f"Nome: {self.__nome}, Età: {self.__eta}"

class Gatto(Animale):
    def __init__(self, nome: str, eta: int):
        super().__init__(nome, eta)
    
    def verso(self) -> str:
        return "Miau...miau.....miauUUu"

class Cane(Animale):
    def __init__(self, nome: str, eta: int):
        super().__init__(nome, eta)
    
    def verso(self) -> str:
        return "Bau! Bau! Auuuu!"

juancho = Gatto("Juancho", 12)
morocho = Cane("Morocho", 7)
print(juancho)
print(juancho.verso())
print(juancho.dormi())

print("-" * 50)

print(morocho)
print(morocho.verso())
print(morocho.dormi())
        

