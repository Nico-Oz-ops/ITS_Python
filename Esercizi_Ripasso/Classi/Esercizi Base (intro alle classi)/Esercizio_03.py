# Esercizio 03
'''
Crea una classe Animale con:
Attributi: nome, specie
Metodo: parla() che stampa una frase tipo:
"L'animale Cane di nome Fido fa un verso."
'''

class Animale:
    
    def __init__(self, nome:str, specie:str):
        self.nome = nome
        self.specie = specie
    
    def parla(self):
        print(f"L'animale {self.specie} di nome {self.nome} fa un verso")

animale = Animale("Fido", "Cane")
animale.parla()


# Variante
class Animale:
    
    def __init__(self, nome:str, specie:str):
        self.nome = nome
        self.specie = specie
    
    def parla(self):
        versi = {
            "cane": "bau bau",
            "gatto": "miao",
            "mucca": "muu",
            "pecora": "bee"
        }

        verso = versi.get(self.specie, "un verso indefinito")
        print(f"L'animale {self.specie} di nome {self.nome} fa {verso}.")

animale = Animale("Fido", "cane")
animale.parla()

animale = Animale("Clotilde", "pecora")
animale.parla()

animale = Animale("Dorotis", "agnello")
animale.parla()
