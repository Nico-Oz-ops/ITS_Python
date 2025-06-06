# Esercizio 2

'''
Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:
Attributi:
● movie_id: str - Identificatore di un film.
● title: str - Titolo del film.
● director: str - Regista del film.
● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:
● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
film '{self.title}' è già noleggiato."
● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
stato noleggiato da questo cliente."

2. Classe Customer:
Attributi:
● customer_id: str - Identificativo del cliente.
● name: str - Nome del cliente.
● rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:
● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
noleggiato."
● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
noleggiato da questo cliente."

3. Classe VideoRentalStore:
Attributi:
● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
l'oggetto Movie.
● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
valore l'oggetto Customer.
Metodi:
● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
ID '{movie_id}' esiste già."
● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
con ID '{customer_id}' è già registrato."
● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
"Cliente o film non trovato."
● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
noleggiati dal client (customer.rented_movies) se il cliente esiste nel
videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
lista vuota.
'''

class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
    
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
    
    def rent(self):
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è gia noleggiato.")
    
    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
    
    def __str__(self):
        return f"{self.title} di {self.director} - {'Noleggiato' if self.is_rented else 'Disponibile'}"

class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = None):
        self.customer_id = customer_id
        self.name = name
        
        if rented_movies is None:
            rented_movies = []
        self.rented_movies = rented_movies
    
    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            self.rented_movies.append(movie)
            movie.rent()
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")

    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
    
    def __str__(self):
        return f"{self.title} di {self.director} - {'Noleggiato' if self.is_rented else 'Disponibile'}"

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = None, customers: dict[str, Customer] = None):
        if movies is None:
            movies = {}
        if customers is None:
            customers = {}
        self.movies = movies
        self.customers = customers
    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")

        else:
            self.movies[movie_id] = Movie(movie_id, title, director)
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")

        else:
            self.customers[customer_id] = Customer(customer_id, name)
    
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
        
        else:
            print("cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
        
        else:
            print("Cliente o film non trovato.")
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id in self.customers:
            customer = self.customers[customer_id]

            return customer.rented_movies
        
        else:
            print("Cliente non trovato.")
            return []

if __name__ == "__main__":

    # creo l'istanza di VideoRentalStore
    vrs = VideoRentalStore()

    # aggiungo film
    vrs.add_movie("001", "Inception", "Christopher Nolan")
    vrs.add_movie("002", "The Grand Budapest Hotel", "Wes Anderson")
    vrs.add_movie("003", "Parasite", "Bong Joon-ho")

    # registrazione dell'utente
    vrs.register_customer("C123", "Nicolino Bandino")
    vrs.register_customer("C159", "Mananà Annanna")

    # noleggio film
    vrs.rent_movie("C159", "003")
    vrs.rent_movie("C123", "002")
    vrs.rent_movie("C123", "001")

    # elenco dei film noleggiati dall'utente
    rented_c123 = vrs.get_rented_movies("C123")
    customer_c123 = vrs.customers["C123"]

    print(f"= Elenco dei film noleggiati da {customer_c123.name} =")
    for movie in rented_c123:
        print(f"- {movie.title} - {movie.director}")
    print("-" * 50)
    
    rented_c159 = vrs.get_rented_movies("C159")
    customer_c159 = vrs.customers["C159"]

    print(f"= Elenco dei film noleggiati da {customer_c159.name} =")
    for movie in rented_c159:
        print(f"- {movie.title} - {movie.director}")
    
    # restituire un film
    vrs.return_movie("C123", "001")


        











