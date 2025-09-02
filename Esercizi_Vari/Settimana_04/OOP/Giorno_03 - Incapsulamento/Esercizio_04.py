'''
Esercizio 4 - Gestione di una libreria di libri

Tema: Attributi privati, getter/setter, metodi di controllo
Obiettivo: Creare una classe Libro con incapsulamento e metodi per aggiornare dati

Traccia:
Crea una classe Libro con attributi privati:

    * __titolo (stringa)
    * __autore (stringa)
    * __pagine (int, >0)

Implementa:

    * get_titolo(), get_autore(), get_pagine()
    * set_titolo(titolo), set_autore(autore), set_pagine(pagine) (controllo: titolo e autore non vuoti, pagine >0)
    * aggiungi_pagine(n) → aggiunge n pagine al libro (n>0)
    * __str__() → stampa tutte le informazioni del libro in modo leggibile

Suggerimento:

    * Tutti gli attributi devono essere privati (__titolo, __autore, __pagine)
    * Tutti i controlli di validità devono essere fatti nei setter
'''
class Libro:
    def __init__(self, titolo: str, autore: str, pagine: int):
        self.set_titolo(titolo)
        self.set_autore(autore)
        self.set_pagine(pagine)
    
    def get_titolo(self) -> str:
        return self.__titolo
    
    def get_autore(self) -> str:
        return self.__autore
    
    def get_pagine(self) -> int:
        return self.__pagine
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Errore, titolo non valido")
        self.__titolo = titolo
    
    def set_autore(self, autore: str):
        if not isinstance(autore, str) or autore.strip() == "":
            raise ValueError("Errore, autore non valido")
        self.__autore = autore
    
    def set_pagine(self, pagine: int):
        if not isinstance(pagine, int) or pagine < 0:
            raise ValueError("Errore, pagine non valide")
        self.__pagine = pagine
    
    def aggiungi_pagine(self, pagina: int):
        if not isinstance(pagina, int) or pagina < 0:
            raise ValueError("Errore, pagina non valida")
        self.__pagine += pagina
    
    def __str__(self):
        return f"Titolo: {self.__titolo}, Autore: {self.__autore}, Pagine: {self.__pagine}"

libro1 = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 96)
libro2 = Libro("1984", "George Orwell", 328)

print(libro1)
print(libro2)

libro1.aggiungi_pagine(5)
print(libro1)
libro2.aggiungi_pagine(10)
print(libro2)
    
        