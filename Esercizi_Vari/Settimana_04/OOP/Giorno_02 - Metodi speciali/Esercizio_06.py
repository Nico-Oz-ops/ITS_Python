'''
6. Classe Studente con voti

Tema: __init__, __str__, __eq__, __len__
Obiettivo: Gestire un insieme di voti per ogni studente

Traccia:
Crea una classe Studente con nome e lista di voti.

    * __str__ → "Studente: <nome>, Voti: <voti>"
    * __eq__ → uguale se la media dei voti è uguale
    * __len__ → restituisce il numero di voti
'''

class Studente:
    def __init__(self, nome: str, voti: list[int] = None):
        self.nome = nome
        self.voti = voti if voti is not None else []
    
    def __eq__(self, other):
        if not self.voti or not other.voti: # modo semplice e sicuro per evitare la divisione per zero quando calcolo la media.
            return False
        return sum(self.voti) / len(self.voti) == sum(other.voti) / len(other.voti)
    
    def __len__(self):
        return len(self.voti)
    
    def __str__(self):
        return f"Studente: {self.nome}, Voti: {self.voti}"

studente1 = Studente("Nico", [25, 30, 25, 30])
studente2 = Studente("Max", [26, 27, 29, 23, 26, 28])
studente3 = Studente("Clara", [30, 30, 30, 20])
studente4 = Studente("Lusi", [])

print(studente1)
print(len(studente1))
print(studente2)
print(len(studente2))
print(studente3)
print(len(studente3))
print(studente4)
print(len(studente4))

print(studente1 == studente2)
print(studente1 == studente3)
print(studente2 == studente4)
        


