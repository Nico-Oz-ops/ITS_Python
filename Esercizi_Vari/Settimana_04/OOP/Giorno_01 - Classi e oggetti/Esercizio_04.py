'''
Tema: Metodo speciale __init__
Obiettivo: Usare il costruttore per inizializzare automaticamente gli attributi.

Nome: Libro

Traccia:
Crea una classe Libro con attributi titolo e autore. Inizializzali nel metodo __init__.
Crea 2 libri e stampane titolo e autore.
'''

class Libro:

    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore

libro1 = Libro("20 poemas de amor y una canciòn desesperada", "Pablo Neruda")
libro2 = Libro("La svastica sul sole", "Philip K. Dick")

print(f"{libro1.titolo} - {libro1.autore}\n{libro2.titolo} - {libro2.autore}")
        