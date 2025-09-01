'''
7. Classe Libro con capitoli

Tema: __init__, __str__, __len__, __repr__
Obiettivo: Oggetto con struttura annidata

Traccia:
Crea una classe Libro con titolo e lista di capitoli (ogni capitolo è una stringa).

    * __str__ → "Titolo: …, Capitoli: …"
    * __len__ → numero di capitoli
    * __repr__ → "Libro('titolo', ['cap1', 'cap2', …])"
'''
class Libro:
    def __init__(self, titolo: str, capitoli: list[str] = None):
        self.titolo = titolo
        self.capitoli = capitoli if capitoli is not None else []
    
    def __str__(self):
        return f"Titolo: {self.titolo}, Capitoli: {self.capitoli}"
    
    def __len__(self):
        return len(self.capitoli)
    
    def __repr__(self):
        return f"Libro('{self.titolo}', {self.capitoli})"

libro1 = Libro("20 mil leguas de viaje submarino", ["cap1", "cap2", "cap3", "cap4", "cap5"])
print(libro1)
print([libro1])
print(len(libro1))


        