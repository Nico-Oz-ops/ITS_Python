from __future__ import annotations
from film import Film

class Azione(Film):
    def __init__(self, id_film, title):
        super().__init__(id_film, title)
        self.__genere = "Azione"
        self.__penale = float(3)
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self, giorno_ritardo: int) -> float:
        if not isinstance(giorno_ritardo, int) or giorno_ritardo < 0:
            raise ValueError("Numero di giorni di ritardo non validi")
        return self.__penale * giorno_ritardo
    

class Commedia(Film):
    def __init__(self, id_film, title):
        super().__init__(id_film, title)
        self.__genere = "Commedia"
        self.__penale = float(2.5)
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self, giorno_ritardo: int) -> float:
        if not isinstance(giorno_ritardo, int) or giorno_ritardo < 0:
            raise ValueError("Numero di giorni di ritardo non validi")
        return self.__penale * giorno_ritardo
    
class Dramma(Film):
    def __init__(self, id_film, title):
        super().__init__(id_film, title)
        self.__genere = "Dramma"
        self.__penale = float(2)
    
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale

    def calcolaPenaleRitardo(self, giorno_ritardo: int) -> float:
        if not isinstance(giorno_ritardo, int) or giorno_ritardo < 0:
            raise ValueError("Numero di giorni di ritardo non validi")
        return self.__penale * giorno_ritardo
