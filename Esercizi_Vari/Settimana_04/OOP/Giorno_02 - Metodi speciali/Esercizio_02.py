'''
2. Rappresentazione leggibile

Tema: Metodi speciali - __str__
Obiettivo: Migliorare la leggibilità in output.

Nome dell’esercizio: Libro

Traccia:
Crea una classe Libro con attributi titolo e autore. Implementa il metodo __str__ 
in modo che stampando l’oggetto appaia:

"Titolo: <titolo>, Autore: <autore>"

Suggerimento: Ricorda che __str__ deve ritornare una stringa.
'''
class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo = titolo
        self.autore = autore
    
    def __str__(self) -> str:
        return f"Titolo: {self.titolo}, Autore: {self.autore}"

libro1 = Libro("Cent'anni di solitudine", "Gabriel Garcìa Màrquez")
print(libro1)

