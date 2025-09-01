'''
14. Classe Libro con confronto di pagine

Tema: __init__, __str__, __eq__, __len__

Obiettivo: Confrontare libri per numero di pagine

Traccia:
Crea una classe Libro con titolo e lista di pagine (una stringa per pagina).

    *__str__ → "Titolo: …, Pagine totali: …"
    *__len__ → numero di pagine
    *__eq__ → due libri uguali se hanno stesso numero di pagine
'''
class Libro:
    def __init__(self, titolo: str, pagine: list[str] = None):
        self.titolo = titolo
        self.pagine = pagine if pagine is not None else []
    
    def __len__(self):
        return len(self.pagine)
    
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return NotImplemented
        return len(self.pagine) == len(other.pagine)
    
    def __str__(self):
        return f"Titolo: {self.titolo}, Pagine totali: {len(self.pagine)}"

libro1 = Libro("Caperucita roja", ["pag1", "pag2", "pag3", "pag4"])
libro2 = Libro("Papelucho Historiador", ["pag5", "pag6", "pag7", "pag8"])
libro3 = Libro("El Hombre en busqueda de sentido", ["pag9", "pag10", "pag11"])

print(libro1)
print(libro2)
print(libro3)
print(libro1 == libro2)
print(libro2 == libro3)