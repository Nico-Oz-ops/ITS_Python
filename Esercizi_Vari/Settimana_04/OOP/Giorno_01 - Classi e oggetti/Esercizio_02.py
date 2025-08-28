'''
Tema: Metodi di istanza
Obiettivo: Aggiungere comportamento agli oggetti.

Nome: SalutoAnimale

Traccia:
Crea una classe Animale con un attributo nome e un metodo saluta() che stampa "Ciao, sono <nome>!".
Crea almeno due oggetti Animale e chiama il metodo su ciascuno.
'''

class Animale:

    def __init__(self, nome: str):
        self.nome = nome
    
    def saluta(self):
        return f"Ciao sono {self.nome}!"

animale1 = Animale("tigre")
animale2 = Animale("cane")

print(animale1.saluta())
print(animale2.saluta())