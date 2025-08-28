'''
Tema: Classi con più metodi
Obiettivo: Gestire informazioni e metodi multipli

Nome: Studente

Traccia:
Crea una classe Studente con attributi nome e voto.
Aggiungi un metodo promosso() che restituisce True se il voto è ≥ 18, altrimenti False.
Crea due studenti e verifica se sono promossi.
'''

class Studente:

    def __init__(self, nome: str, voto: int):
        self.nome = nome
        self.voto = voto
    
    def promosso(self):
        if self.voto >= 18:
            return True
        else:
            return False

studente1 = Studente("Juan", 25)
studente2 = Studente("Mike", 17)

print(studente1.promosso())
print(studente2.promosso())