'''
Esercizio: Gestione di una Videoteca

Obiettivo: Creare un sistema per gestire film, utenti e noleggi in una videoteca. Lo scopo è esercitarsi con:
    - Creazione di classi e oggetti
    - Liste di oggetti e dizionari
    - Metodi per modificare e leggere lo stato degli oggetti
    - Relazioni tra oggetti
 
Classi richieste:
 
1. Classe Film
Rappresenta un film. Deve avere:
 
*titolo: stringa
*regista: stringa
*anno: int
*disponibile: booleano (True se non è in prestito)
 
Metodi:
- __init__
- noleggia() → imposta disponibile a False
- restituisci() → imposta disponibile a True
- __str__() → restituisce qualcosa tipo "Titolo" di Regista (Disponibile/Non disponibile)
 
 
2. Classe Utente
Rappresenta un utente della videoteca. Deve avere:
 
*nome: stringa
*id_utente: stringa
*film_in_prestito: lista di oggetti Film
 
Metodi:
- __init__
- prendi_in_prestito(film: Film) → aggiunge il film a film_in_prestito e lo marca come non disponibile
- restituisci_film(film: Film) → rimuove il film da film_in_prestito e lo marca come disponibile
- __str__() → mostra il nome dell’utente e i titoli dei film in prestito
 
 
3. Classe Videoteca
Rappresenta la videoteca. Deve avere:
 
*film: dizionario di oggetti Film, chiave: titolo o ID
*utenti: dizionario di oggetti Utente, chiave: ID utente
 
Metodi:
- aggiungi_film(film: Film)
- aggiungi_utente(utente: Utente)
- noleggia_film(id_utente: str, titolo_film: str) → permette all’utente di prendere un film se disponibile
- restituisci_film(id_utente: str, titolo_film: str) → permette all’utente di restituire un film
- lista_film_disponibili() → restituisce i film che sono disponibili
'''

class Film:
    def __init__(self, titolo: str, regista: str, anno: int):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.disponibile: bool = True
    
    def noleggia(self):
        if self.disponibile:
            self.disponibile = False
        
        else:
            print(f"Il film {self.titolo} non è disponibile")
    
    def restituisci(self):
        if not self.disponibile:
            self.disponibile = True
        
        else:
            print(f"Il film {self.titolo} era già disponibile")
    
    def __str__(self):
        disponibilita = "Disponibile" if self.disponibile else "Non disponibile"
        return f"Titolo: {self.titolo} | Regista: {self.regista} ({disponibilita})"
        
class Utente:
    def __init__(self, nome: str, id_utente: str):
        self.nome = nome
        self.id_utente = id_utente
        self.film_in_prestito: list[Film] = []
             
    def prendi_in_prestito(self, film: Film):
        if not film.disponibile:
            print(f"Il film '{film.titolo}' non è disponibile per il noleggio")
            return
        
        if film not in self.film_in_prestito:
            self.film_in_prestito.append(film)
            film.noleggia()
        else:
            print(f"Il film '{film.titolo}' è stato già preso da '{self.nome}'")
    
    def restituisci_film(self, film: Film):
        if film in self.film_in_prestito:
            self.film_in_prestito.remove(film)
            film.restituisci()
        else:
            print(f"Il film '{film.titolo}' non è stato noleggiato da '{self.nome}'")

    def __str__(self):
        if not self.film_in_prestito:
            return f"{self.nome}, non ha film in prestito"

        film_prestito = "\n".join(f"- {film.titolo}" for film in self.film_in_prestito)
        return f"Film in prestito di {self.nome}:\n{film_prestito}"

class Videoteca:
    def __init__(self):
        self.film: dict[str, Film] = {}
        self.utenti: dict[str, Utente] = {}
    
    def aggiungi_film(self, film: Film):
        if film in self.film:
            print(f"Il film {film.titolo} esiste già")
        else:
            self.film[film.titolo] = film
    
    def aggiunge_utente(self, utente: Utente):
        if utente in self.utenti:
            print(f"{utente.nome} esiste già")
        else:
            self.utenti[utente.id_utente] = utente
    
    def noleggia_film(self, id_utente: str, titolo_film: str):
        if id_utente not in self.utenti:
            print(f"Utente con ID {id_utente} non trovato")
        
        if titolo_film not in self.film:
            print(f"{titolo_film} non fa parte di questa videoteca")
        
        utente = self.utenti[id_utente]
        film = self.film[titolo_film]

        if not film.disponibile:
            print(f"Il film '{titolo_film}' non è disponibile per il noleggio")
        
        return utente.prendi_in_prestito(film)
    
    def restituisci_film(self, id_utente: str, titolo_film: str): 
        if id_utente not in self.utenti:
            print(f"Utente con ID {id_utente} non trovato")
        
        if titolo_film not in self.film:
            print(f"Film '{titolo_film}' non trovato")
        
        utente = self.utenti[id_utente]
        film = self.film[titolo_film]

        return utente.restituisci_film(film)
    
    def lista_film_disponibili(self):
        film_disponibili = [film for film in self.film.values() if film.disponibile]
        
        if not film_disponibili:
            print(f"Nessun film disponibile in questo momento")
        
        else:
            print("\nI film disponibile sono:")
            for film in film_disponibili:
                print(f"- {film.titolo}({film.anno}) - {film.regista}")