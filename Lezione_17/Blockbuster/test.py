from film import Film
from noleggio import Noleggio
from movie_genre import Azione, Commedia, Dramma

film_list = [
    Azione(1, "Mad Max: Fury Road"),
    Azione(2, "Mission Impossible"),
    Azione(3, "Rogue One: A Star Wars Story"),
    Azione(4, "John Wick"),
    Azione(5, "Il cavaliere oscuro"),
    Commedia(6, "A quacuno piace caldo"),
    Commedia(7, "Io & Annie"),
    Commedia(8, "Ti presento i miei"),
    Commedia(9, "I soliti ignoti"),
    Dramma(10, "Schindler's List")
]

noleggio = Noleggio(film_list)

print("Quale film vuoi noleggiare?\n")
noleggio.printMovies()
print("-" * 50)

# cliente noleggia il primo film
noleggio.rentAMovie(film_list[0], clientID=101)

# lo stesso cliente noleggia un secondo film
noleggio.rentAMovie(film_list[2], clientID=101)

# noleggio da parte di un secondo cliente
noleggio.rentAMovie(film_list[2], clientID=103) # avviso film non disponibile















'''
# Simulazione reso del secondo film noleggiato dal cliente 1
def returnMovie(store: VideoStore, film, clientID: int):
    if clientID in store.rented_film and film in store.rented_film[clientID]:
        store.rented_film[clientID].remove(film)
        store.film_list.append(film)
        print(f"Cliente {clientID} ha restituito il film '{film.getTitle()}'.")
    else:
        print(f"Cliente {clientID} non ha noleggiato il film '{film.getTitle()}'.")

returnMovie(noleggio, film_list[1], clientID=101)  # Mad Max restituito

# --- Stampa dei film disponibili in negozio ---
print("\nFilm disponibili in negozio:")
noleggio.printMovies()
'''