# Esercizio 2
'''
Strumenti musicali
Obiettivo: Usare il polimorfismo con classi astratte.
Traccia:
Crea una classe astratta StrumentoMusicale con un metodo astratto suona().
Crea due classi:
Chitarra: stampa "Strimpello la chitarra."
Pianoforte: stampa "Suono il pianoforte."
Scrivi una funzione esibizione(strumento) che prende uno strumento e chiama suona() su di esso.
Testa la funzione con istanze di Chitarra e Pianoforte
'''

from abc import ABC, abstractmethod

class StrumentoMusicale(ABC):

    @abstractmethod
    def suona(self) -> None:
        pass

class Chitarra(StrumentoMusicale):
  
    def suona(self):
        print("Strimpello la chitarra") 

class Pianoforte(StrumentoMusicale):

    def suona(self):
        print("Suono il pianoforte")
    
def esibizione(strumento:StrumentoMusicale):
    strumento.suona()

chi = Chitarra()
pi = Pianoforte()

esibizione(chi)
esibizione(pi)




