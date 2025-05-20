# Esercizio 1
'''
Crea una classe Libro con:
Attributi: titolo, autore
Metodo: descrizione() che stampa una frase tipo:
"Il libro Il Piccolo Principe è stato scritto da Antoine de Saint-Exupéry."
'''

class Libro:

    def __init__(self, titolo:str, autore:str):
        self.titolo = titolo
        self.autore = autore
    
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore}")

libro = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry")
libro.descrizione()


        