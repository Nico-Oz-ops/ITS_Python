'''
Esercizio 6 - Media Player

Tema: Polimorfismo con metodi complessi
Obiettivo: Simulare la riproduzione di diversi tipi di file multimediali utilizzando un unico metodo comune.

Traccia:

1. Definisci una superclasse astratta Media che rappresenta un contenuto multimediale.

    * Deve avere un metodo astratto play().

2. Crea tre sottoclassi concrete che ereditano da Media:

    * Canzone → rappresenta una canzone (titolo, artista).
    * Video → rappresenta un video (titolo, durata in minuti).
    * Podcast → rappresenta un podcast (titolo, autore, numero episodio).

3. Implementa in ciascuna sottoclasse il metodo play(), in modo che stampi un messaggio diverso, ad esempio:

    * Canzone: "Riproduco il brano '<titolo>' di <artista>"
    * Video: "Riproduco il video '<titolo>' (durata: <durata> min)"
    * Podcast: "Riproduco il podcast '<titolo>', episodio <num> di <autore>"

4. Crea una lista (playlist) contenente oggetti di tipo Canzone, Video e Podcast.

5. Con un unico ciclo for, esegui il metodo play() per ogni elemento della playlist.
'''

from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        pass

class Canzone(Media):
    def __init__(self, titolo: str, artista: str):
        super().__init__()
        self.set_titolo(titolo)
        self.set_artista(artista)
    
    def get_titolo(self) -> str:
        return self.titolo 
    
    def get_artista(self) -> str:
        return self.artista 
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido.")
        self.titolo = titolo
    
    def set_artista(self, artista: str):
        if not isinstance(artista, str) or artista.strip() == "":
            raise ValueError("Artista non valido.")
        self.artista = artista
    
    def play(self) -> str:
        return f"Riproduco il brano '{self.titolo}' di {self.artista}"

class Video(Media):
    def __init__(self, titolo: str, durata: int):
        super().__init__()
        self.set_titolo(titolo)
        self.set_durata(durata)
    
    def get_titolo(self) -> str:
        return self.titolo 
    
    def get_durata(self) -> int:
        return self.durata 
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido")
        self.titolo = titolo
    
    def set_durata(self, durata: int):
        if not isinstance(durata, int) or durata <= 0:
            raise ValueError("Durata non valida")
        self.durata = durata 
    
    def play(self):
        return f"Riproduco il video '{self.titolo}' (durata: {self.durata} min)"

class Podcast(Media):
    def __init__(self, titolo: str, autore: str, numero_episodio: int):
        super().__init__()
        self.set_titolo(titolo)
        self.set_autore(autore)
        self.set_numero_episodio(numero_episodio)
    
    def get_titolo(self) -> str:
        return self.titolo

    def get_autore(self) -> str:
        return self.autore
    
    def get_numero_episodio(self) -> int:
        return self.numero_episodio
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido")
        self.titolo = titolo
    
    def set_autore(self, autore: str):
        if not isinstance(autore, str) or autore.strip() == "":
            raise ValueError("Autore non valido")
        self.autore = autore
    
    def set_numero_episodio(self, numero_episodio):
        if not isinstance(numero_episodio, int) or numero_episodio <= 0:
            raise ValueError("Numero di episodio non valido")
        self.numero_episodio = numero_episodio
    
    def play(self):
        return f"Riproduco il podcast '{self.titolo}', episodio {self.numero_episodio} di {self.autore}"

playlist = [
    Canzone("Bohemian Rhapsody", "Queen"),
    Video("Introduzione a Python", 15),
    Podcast("Storia Romana", "Mario Rossi", 12)
]

for elemento in playlist:
    print(f"{elemento.play()}")