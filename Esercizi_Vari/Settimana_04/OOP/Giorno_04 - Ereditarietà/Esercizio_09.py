'''
Esercizio 9 - Animali parlanti

Estendi la classe Animale (già fatta) aggiungendo altre sottoclassi:

    * Uccello (nuovo attributo: specie)
    * Mucca (override di verso() → “Muuuu”)

Crea una lista di animali (cani, gatti, uccelli, mucche) e fai un ciclo che stampa nome e verso() di ognuno.
'''
class Animale:

    def __init__(self, nome: str, eta: int):
        self.set_nome(nome)
        self.set_eta(eta)
    
    def get_nome(self):
        return self.nome

    def get_eta(self):
        return self.eta 

    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido.")
        self.nome = nome

    def set_eta(self, eta: int):
        if not isinstance(eta, int) or eta < 0:
            raise ValueError("Età non valida.")
        self.eta = eta

    def verso(self): 
        return "Suono generico"
      
class Cane(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    
    def verso(self):
        return f"{self.nome}: Bau! Bau! Auuu!"

class Gatto(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    
    def verso(self):
        return f"{self.nome}: Miau...miauuu"

class Uccello(Animale):
    def __init__(self, nome, eta, specie: str):
        super().__init__(nome, eta)
        self.set_specie(specie)
    
    def get_specie(self) -> str:
        return self.specie 
    
    def set_specie(self, specie: str):
        if not isinstance(specie, str) or specie.strip() == "":
            raise ValueError("Specie non valida.")
        self.specie = specie
    
    def verso(self):
        return f"{self.nome}: Fiuu, fiuuuu, fifi"

class Mucca(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    
    def verso(self):
        return f"{self.nome}: Mmmuuuuuuu"

animali = [Cane("Juancho", 5), Uccello("Piolìn", 2, "Papagallo"), Mucca("Bianconera", 6), Gatto("Renato", 9)]
for animale in animali:
    print(animale.verso())
