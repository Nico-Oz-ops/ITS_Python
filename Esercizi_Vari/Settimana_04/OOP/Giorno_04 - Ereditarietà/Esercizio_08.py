'''
Esercizio 8 - Veicoli

Crea una classe Veicolo con attributi marca e modello e metodo info().

Crea sottoclassi:

    * Auto (aggiungi porte)
    * Moto (aggiungi cilindrata)

Override del metodo info() in ciascuna sottoclasse per includere gli attributi extra.
'''

class Veicolo:
    def __init__(self, marca: str, modello: str):
        self.set_marca(marca)
        self.set_modello(modello)
    
    def get_marca(self):
        return self.__marca
    
    def get_modello(self):
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
        return f"Caratteristiche del veicolo:\nMarca: {self.__marca}\nModello: {self.__modello}"

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, porte: int):
        super().__init__(marca, modello)
        self.set_porte(porte)
    
    def get_porte(self) -> int:
        return self.__porte
    
    def set_porte(self, porte: int):
        if not isinstance(porte, int) or porte <= 0:
            raise ValueError("Porte non valide.")
        self.__porte = porte
    
    def info(self):
        return super().info() + f"\nNumero di porte: {self.__porte}"

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, cilindrata: int):
        super().__init__(marca, modello)
        self.set_cilindrata(cilindrata)
    
    def get_cilindrata(self) -> int:
        return self.__cilindrata
    
    def set_cilindrata(self, cilindrata: int):
        if not isinstance(cilindrata, int) or cilindrata < 0:
            raise ValueError("Cilindrata non valida.")
        self.__cilindrata = cilindrata
    
    def info(self):
        return super().info() + f"\nCilindrata: {self.__cilindrata}cc"

auto = Auto("Porsche", "911", 2)
moto = Moto("Honda", "CBR 600 RR", 600)
print(auto.info())
print("-" * 40)
print(moto.info())
    
 