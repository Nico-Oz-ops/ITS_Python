# Esercizio 2
'''
Sistema di Gestione Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare 
tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio 
    di errore se nessun film contiene la parola cercata nel titolo.
 
Codice driver

    Crea un’istanza della classe MovieCatalog.
    Aggiungi nuovi film e registi.
    Aggiungi film a registi già presenti nel catalogo.
    Rimuovi film dal catalogo.
    Elenca i registi presenti nel catalogo.
    Visualizza film di uno specifico regista.
    Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.
'''

class MovieCatalog:

    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name:str, movies:list[str]):

        if director_name not in self.catalog:
            self.catalog[director_name] = set()
        
        if isinstance(movies, str): # controllo se "movies" è una stringa
            movies = [movies] # se "movies" è una stringa allora lo converte in una lista con un solo elemento

        self.catalog[director_name].update(movies)
        print(f"I film aggiunti del regista {director_name}: {movies}")   # potrei usare {', '.join(movies)} per avere in output una stringa senza i parentesi cuadre e gli apici
        
    def remove_movie(self, director_name:str, movie_name:str, remove_director=True):
        self.director_name = director_name
        self.movie_name = movie_name

        if director_name in self.catalog:

            if movie_name in self.catalog[director_name]:

                self.catalog[director_name].remove(movie_name)
                print(f"Film '{movie_name}' rimosso da {director_name}")

                if not self.catalog[director_name] and remove_director:
                    del self.catalog[director_name]
                    print(f"{director_name} è stato rimosso dal catalogo perché non ha più film")

            else:
                print(f"{movie_name} non è presente nella lista dei film di {director_name}")
        
        else:
            print(f"{director_name} non è presente nel catalogo")
    
    def list_directors(self):

        if self.catalog:
            print(f"I registi presenti nel catalogo:")
            
            for director in self.catalog:
                print(f"- {director}")
        
        else:
            print("Non c'è nessun regista presente nel catalogo")
    
    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            print(f"I film di {director_name}:")

            for movie in self.catalog[director_name]:
                print(f"- {movie}")
        
        else:
            print(f"Non si è trovato nessun film del regista {director_name}")
    
    def search_movies_by_title(self, title:str):
        risultato = {} # inizializza un dizionario vuoto per memorizzare i risultati trovati, organizzati per regista

        for director, movies in self.catalog.items(): # cicla attraverso il catalogo dei film (director e movies)
            matched = [movie for movie in movies if title.lower() in movie.lower()] # crea una lista dei film di quel regista che contengono la parola cercata(title), indipendentemente da maisucole e minuscole (uso di lower())
            if matched: # se ci sono film che corrispondono alla ricerca per quel regista li aggiunge nel dizionario risultato sotto il nome del regista
                risultato[director] = matched 
        
        if risultato: # controlla se ci sono stati risultati trovati
            for director, movies in risultato.items(): # se ci sono, allora stampa il nome del regista e poi stampa il nome del film
                print(f"Regista: {director}")
                for movie in movies:
                    print(f"- {movie}")
        else:
            print(f"Nessun film trovato con la parola '{title}' nel titolo")

# istanza della classe MovieCatalog()
catalogo = MovieCatalog()

# aggiungo nuovi registi e film
catalogo.add_movie("Steven Spielberg", ["Jurassic Park", "E.T."])
catalogo.add_movie("Quentin Tarantino", ["Kill Bill", "Bastardi Senza Gloria"])
catalogo.add_movie("Pablo Larrain", ["Jackie", "No"])
print("-" * 50)

# aggiungo film a registi già presenti nel catalogo
catalogo.add_movie("Quentin Tarantino", "Django Unchained")
catalogo.add_movie("Pablo Larrain", "Neruda")
print("-" * 50)

# rimuovo film dal catalogo
catalogo.remove_movie("Pablo Larrain", "Jackie")
print("-" * 50)

# elenco i registi
catalogo.list_directors()
print("-" * 50)

# visualizzare i film di un regista in specifico
catalogo.get_movies_by_director("Pablo Larrain")
print("-" * 50)

# cercare un film per parola chiave
catalogo.search_movies_by_title("bill")







