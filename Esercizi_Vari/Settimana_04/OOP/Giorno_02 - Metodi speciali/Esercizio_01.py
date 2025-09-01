'''
1. Classe con inizializzazione

Tema: Metodi speciali - __init__
Obiettivo: Creare oggetti inizializzati con valori personalizzati.

Nome dell’esercizio: Persona

Traccia:
Crea una classe Persona con attributi nome e età. Usa __init__ per assegnarli al 
momento della creazione dell’oggetto. Crea due istanze e stampale.

Suggerimento: Non serve ancora __str__, la stampa mostrerà l’oggetto con l’indirizzo in memoria.
'''

class Persona:

    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta

persona1 = Persona("Javi", 30)
persona2 = Persona("Josè", 20)
print(persona1.nome, persona1.eta)
print(persona2.nome, persona2.eta)

        