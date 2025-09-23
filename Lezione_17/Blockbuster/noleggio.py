from __future__ import annotations
from movie_genre import Azione, Dramma, Commedia

class Noleggio:
    def __init__(self, film_list: list[Azione|Dramma|Commedia] = None):
        self.film_list = film_list if film_list is not None else []
        self.rented_film = dict()
    
    def isAvailable(self, film: Azione|Dramma|Commedia) -> bool:
        # if not isinstance(film, (Azione, Commedia, Dramma)):
        #     raise ValueError ("Film non valido")
        # else:
        #     trovato = False
        #     for f in self.film_list:
        #         if f.__title == film:
        #             trovato == True
        #             print(f"Il film scelto è disponibile: {film.__title}")
                
        #         else:
        #             print(f"Il film scelto non è disponibile: {film.__title}")
        
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}")
            return False
    
    def rentAMovie(self, film: Azione|Dramma|Commedia, clientID: int):
        if self.isAvailable(film):
            self.film_list.remove(film)

            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")
    
    def giveBack(self, film: Azione|Dramma|Commedia, clientID: int, days: int):
        if film in self.rented_film[clientID] and clientID in self.rented_film:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)

            penale_da_pagare = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale_da_pagare} euro")

    def printMovies(self):
        if not self.film_list:
            print("Nessun film disponibile in negozio")
            return
        
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()}")
    
    def RentMovies(self, clientID: int):
        if not self.rented_film[clientID]:
            print("Nessun film disponibile da parte del cliente")
            return
        
        for film in self.rented_film[clientID]:
            print(f"{film.getTitle()} - {film.getGenere()}")

        









