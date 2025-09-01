'''
4. Lunghezza di un oggetto

Tema: Metodi speciali - __len__
Obiettivo: Rendere una classe compatibile con len().

Nome dell’esercizio: Playlist

Traccia:
Crea una classe Playlist che contiene una lista di brani. Implementa __len__ per 
far sì che len(playlist) restituisca il numero di brani.

Suggerimento: Usa len(self.brani) all’interno di __len__.
'''
# Alternativa 1
class Playlist:
    def __init__(self, brani: list[str] = None):
        # meglio None invece di [] per evitare il problema dei valori mutabili come default
        self.brani = brani if brani is not None else []
    
    def __len__(self):
        return len(self.brani)
    
    def __str__(self):
        return f"Playlist: {self.brani}"

playlist = Playlist(["hola", "12power", "otherside"])
print(playlist)
print(len(playlist))

# Alternativa 2
class Playlist:
    def __init__(self):
        self.brani = []
    
    def aggiungere_brani(self, brano: str):
        self.brani.append(brano)
    
    def __len__(self):
        return len(self.brani)
    
    def __str__(self):
        return  f"Playlist: {self.brani}"
    
playlist2 = Playlist()
playlist2.aggiungere_brani("hola")
playlist2.aggiungere_brani("hello goodbye")
playlist2.aggiungere_brani("she loves you")
playlist2.aggiungere_brani("otherside")

print(playlist2)
print(len(playlist2))




        