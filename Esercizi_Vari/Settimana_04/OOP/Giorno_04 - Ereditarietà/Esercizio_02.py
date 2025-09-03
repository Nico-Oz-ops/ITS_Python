'''
Esercizio 2 - Veicolo base e Auto

Tema: Costruttore con super()
Obiettivo: Usare il costruttore della classe base nella sottoclasse

Traccia:

    * Classe Veicolo con attributi marca e modello.

    * Metodo info() che stampa "Marca: <marca>, Modello: <modello>".

    * Classe Auto che eredita da Veicolo e aggiunge attributo porte.

    * Sovrascrivere info() per stampare anche il numero di porte.

    * Testare creando un’istanza di Auto.
'''

class Veicolo:
    def __init__(self, marca: str, modello: str):
        self.set_marca(marca)
        self.set_modello(modello)
    
    def get_marca(self) -> str:
        return self.__marca
    
    def get_modello(self) -> str:
        return self.__modello
    
    def set_marca(self, marca: str):
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError("Marca non valida.")
        self.__marca = marca
    
    def set_modello(self, modello: str):
        if not isinstance(modello, str) or modello.strip() == "":
            raise ValueError("Modello non valido.")
        self.__modello = modello
    
    def info(self):
        return f"Marca: {self.__marca}, Modello: {self.__modello}"

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, porte: int):
        super().__init__(marca, modello)
        self.set_porte(porte)
    
    def get_porte(self) -> int:
        return self.__porte
    
    def set_porte(self, porte: int):
        if not isinstance(porte, int) or porte < 0 or porte > 5:
            raise ValueError("Numero di porte non valide.")
        self.__porte = porte
    
    def info(self):
        return super().info() + f", Numero di porte: {self.__porte}"

auto = Auto("Porsche", "911", 2)
print(auto.info())
        
