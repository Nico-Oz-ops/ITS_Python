'''
3. Confronto tra oggetti

Tema: Metodi speciali - __eq__
Obiettivo: Definire un criterio personalizzato di uguaglianza.

Nome dell’esercizio: Studente

Traccia:
Crea una classe Studente con attributi nome e matricola.
Implementa __eq__ in modo che due studenti siano considerati uguali se hanno la stessa matricola.

Suggerimento: Ricorda che __eq__ deve restituire True o False.
'''

class Studente:
    def __init__(self, nome: str, matricola: str):
        self.nome = nome
        self.matricola = matricola
    
    def __eq__(self, other):
        return self.matricola == other.matricola

studente1 = Studente("Nico", "123NvJ")
studente2 = Studente("Marco", "123Mb")
studente3 = Studente("Mirko", "123Mb")

print(studente1 == studente2)
print(studente1 == studente3)
print(studente2 == studente3)