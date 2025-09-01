'''
8. Classe Playlist con controlli

Tema: __init__, __str__, __len__, __eq__

Obiettivo: Confrontare playlist e contarne i brani

Traccia:
Crea una classe Playlist con lista di brani.

    * __str__ → "Playlist con X brani: …"
    * __len__ → numero di brani
    * __eq__ → due playlist sono uguali se contengono gli stessi brani (ordine NON importante)
'''

class Playlist:
    def __init__(self, brani: list[str] = None):
        self.brani = brani if brani is not None else []
    
    def __len__(self):
        return len(self.brani)
    
    def __str__(self):
        return f"Playlist con {len(self.brani)} brani: {self.brani}"
    
    def __eq__(self, other):
        return sorted(self.brani) == sorted(other.brani) # bisogna implementare sorted(), per garantire l'ordine delle liste a confrontare

playlist1 = Playlist(["breathe", "song 2", "aerplane", "friends"])
playlist2 = Playlist(["around the world", "perfect life", "another day"])
playlist3 = Playlist(["breathe", "song 2", "aerplane", "friends"])

print(playlist1)
print(playlist2)
print(playlist3)

print(playlist1 == playlist2)
print(playlist1 == playlist3)
print(playlist2 == playlist3)
    
    