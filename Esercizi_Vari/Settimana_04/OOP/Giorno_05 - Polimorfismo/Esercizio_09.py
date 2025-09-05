'''
Esercizio 9 - Zoo interattivo

Tema: Polimorfismo + proprietà
Obiettivo: Far interagire oggetti polimorfici in un contesto di zoo virtuale.

Traccia:

1. Definisci una classe base AnimaleZoo con:

    * un metodo info() che restituisce informazioni generali sull’animale (ad esempio il tipo o nome).
    * un metodo verso() che restituisce il verso caratteristico dell’animale.

2. Crea quattro sottoclassi che ereditano da AnimaleZoo:

    * Leone
    * Elefante
    * Pappagallo
    * Serpente

3. Implementa per ciascuna sottoclasse il metodo verso() con un suono specifico (ad esempio “Roar” per il leone).

4. Scrivi una funzione mostra_zoo(lista_animali) che, dato un elenco di animali:

    * stampa per ciascun animale il nome, il tipo (classe) e il verso.

5. Crea una lista di animali mista e chiama mostra_zoo() per simulare lo zoo interattivo.
'''

class AnimaleZoo:
    def __init__(self, nome: str):
        self.tipo = self.__class__.__name__ # in questo caso, il tipo viene preso dal nome di ogni sottoclasse
        self.nome = nome

    def info(self):
        return f"Tipo: {self.tipo}\nNome: {self.nome}"
    
    def verso(self):
        return "Suono generico"

class Leone(AnimaleZoo):
    def __init__(self, nome):
        super().__init__(nome)
    
    def verso(self):
        return "Roaaaar!"
    
class Elefante(AnimaleZoo):

    def verso(self):
        return "Brrrrrffff"

class Pappagallo(AnimaleZoo):

    def verso(self):
        return "Fiu fiu, ciao... fiu fiu"

class Serpente(AnimaleZoo):

    def verso(self):
        return "Psssssssss, snif snif"

def mostraZoo(animali: list[AnimaleZoo]):
    for animale in animali:
        print(f"{animale.info()}\nVerso: {animale.verso()}\n")

animali = [Leone("Simba"),
           Elefante("Dumbo"),
           Pappagallo("Piolìn"),
           Serpente("Snake")
           ]
mostraZoo(animali)
