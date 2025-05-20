# Esercizio 2
'''
Classe Playlist
Classe Playlist con:

Attributi: nome, brani (lista)

Metodi:

aggiungi_brano(titolo)

rimuovi_brano(titolo)

mostra_brani() → stampa la lista
'''

class Playlist:

    def __init__(self, nome:str, brani:list[str]):
        self.nome = nome
        self.brani = brani
    
    def aggiungi_brano(self, titolo:str):
        self.brani.append(titolo.lower())
    
    def rimuovi_brano(self, titolo:str):
        if titolo in self.brani:
            self.brani.remove(titolo.lower())
        
        else:
            print(f"Il brano {titolo} non è nella playlist")
    
    def mostra_brani(self):
        print(f"La playlist '{self.nome}' ha i seguenti brani:")

        for i, brano in enumerate(self.brani, 1):
            print(f"{i} - {brano}")


playlist = Playlist("rock", ["123", "abc", "oh wao"])
playlist.aggiungi_brano("ejalès")
playlist.mostra_brani()
print("-" * 50)
playlist.rimuovi_brano("123")
playlist.mostra_brani()
        