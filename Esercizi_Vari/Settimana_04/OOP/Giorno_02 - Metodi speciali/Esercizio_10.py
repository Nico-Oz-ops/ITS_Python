'''
10. Classe Film con durata e genere

Tema: __init__, __str__, __eq__, __repr__

Obiettivo: Confrontare film e visualizzare info

Traccia:
Crea una classe Film con titolo, durata e genere.

    * __str__ → "Titolo: …, Durata: … min, Genere: …"
    * __repr__ → "Film('titolo', durata, 'genere')"
    * __eq__ → due film uguali se titolo e durata coincidono
'''

class Film:
    def __init__(self, titolo: str, durata: int, genere: str):
        self.titolo = titolo
        self.durata = durata
        self.genere = genere
    
    def __str__(self):
        return f"Titolo: {self.titolo}, Durata: {self.durata}, Genere: {self.genere}"
    
    def __repr__(self):
        return f"Film('{self.titolo}' - {self.durata} - '{self.genere}')"
    
    def __eq__(self, other):
        if not isinstance(other, Film): # Se other non è un Film, non so come confrontarlo
            return NotImplemented # "questa operazione non è implementata per questo tipo", restituirà False
        return (self.titolo, self.durata) == (other.titolo, other.durata)

film1 = Film("Star Wars", 180, "Fantascienza")
film2 = Film("Lord of the Rings", 180, "Fantascienza")
film3 = Film("Lord of the Rings", 180, "Fantascienza")
print(film1)
print(film2)
print(film3)
print(film1 == film2)
print(film2 == film3)
print(film2 == "star wars")