'''
Esercizio 1 - Animale e Cane

Tema: Classe base e sottoclasse semplice
Obiettivo: Capire come creare una sottoclasse e aggiungere attributi

Traccia:

    * Crea una classe Animale con attributi nome e eta e metodo verso() che stampa "Suono generico".

    * Crea una sottoclasse Cane che:

        * Eredita da Animale.

        * Sovrascrive il metodo verso() per stampare "Bau".

        * Aggiunge un nuovo attributo specifico, ad esempio razza.

    * Crea un’istanza di Cane, stampa nome, eta e razza, e chiama verso().

Suggerimento: usa super().__init__() per inizializzare gli attributi ereditati dalla superclasse.
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
            raise ValueError("Nome non valido")
        self.__nome = nome
    
    def set_eta(self, eta: int):
        if not isinstance(eta, int) or eta < 0:
            raise ValueError("Età non valida")
        self.__eta = eta
    
    def verso(self) -> str:
        print("Suono generico")
    
    def __str__(self):
        return f"Nome: {self.__nome}\nEtà: {self.__eta} anni."
        
class Cane(Animale):
    def __init__(self, nome: str, eta: int, razza: str):
        super().__init__(nome, eta) # inizializzo nome e eta della superclasse
        self.set_razza(razza)
    
    def get_razza(self) -> str:
        return self.__razza
    
    def set_razza(self, razza: str):
        if not isinstance(razza, str) or razza.strip() == "":
            raise ValueError("Razza non valida")
        self.__razza = razza
    
    def verso(self):
        print("Bau! Bau!")
    
    def __str__(self):
        return super().__str__() + f"\nRazza: {self.__razza}"

cane = Cane("Jack", 12, "pastore tedesco")
print(cane)
cane.verso()
