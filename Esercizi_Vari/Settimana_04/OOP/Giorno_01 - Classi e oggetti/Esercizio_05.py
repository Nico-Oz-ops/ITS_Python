'''
Tema: Metodo speciale __str__
Obiettivo: Personalizzare la rappresentazione degli oggetti.

Nome: Film

Traccia:
Crea una classe Film con attributi titolo e anno.
Definisci il metodo __str__ per restituire una stringa come:
"<titolo> (anno: <anno>)".
Crea 2 film e stampali.
'''

class Film:

    def __init__(self, titolo: str, anno: int):
        self.titolo = titolo
        self.anno = anno
    
    def __str__(self):
        return f"{self.titolo} (anno: {self.anno})"

film1 = Film("iHostage", 2025)
film2 = Film("Evelyn", 2018)
print(film1)
print(film2)