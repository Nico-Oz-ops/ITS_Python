'''
Esercizio 4 - Strumenti musicali

Tema: Polimorfismo + metodi comuni
Obiettivo: Utilizzare lo stesso metodo per comportamenti diversi tra le sottoclassi.

Traccia:

1. Crea una classe base Strumento con un metodo astratto o generico suona().

2. Implementa le sottoclassi:

    * Chitarra
    * Pianoforte
    * Batteria

    Ogni sottoclasse deve avere un proprio comportamento nel metodo suona(), 
    ad esempio stampando un messaggio diverso.

3. Crea una funzione concerto(lista_strumenti) che prende una lista di strumenti e li fa suonare tutti in sequenza 
    chiamando suona() su ciascuno.

Esempio di comportamento atteso:

*   Chitarra → stampa "La chitarra suona: strum strum"
*   Pianoforte → stampa "Il pianoforte suona: ding ding"
*   Batteria → stampa "La batteria suona: boom boom"
'''
from abc import ABC, abstractmethod

class Strumento(ABC):

    @abstractmethod
    def suona(self):
        pass

class Chitarra(Strumento):
    def suona(self):
        return "La chitarra suona: strum strum"

class Pianoforte(Strumento):
    def suona(self):
        return "Il pianoforte suona: ding ding"

class Batteria(Strumento):
    def suona(self):
        return "La batteria suona: tumtum pa! tumtum pa!"

def concerto(lista_strumenti: list[Strumento]):
    for strumento in lista_strumenti:
        print(strumento.suona())

strumenti = [Chitarra(), Pianoforte(), Batteria()]
concerto(strumenti)

