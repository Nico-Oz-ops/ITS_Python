# dal modulo esercizio 2.py importare la classe MovieCatalog

from Esercizio_02 import MovieCatalog

# inizializzare un catalogo, ovvero un oggetto della classe MovieCatalog
catalog: MovieCatalog = MovieCatalog()
# print(catalog)

catalog.add_movies("Steven Spielberg", ["Casper", "Ritorno al futuro"])
# print(catalog)

catalog.add_movies("Steven Spielberg", ["E.T."])
# print(catalog)

catalog.add_movies("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"])
# print(catalog)

catalog.remove_movie("Quentin Tarantino", "Kill Bill")
print(catalog)
catalog.remove_movie("Quentin Tarantino", "Pulp Fiction")
print(catalog)

print(catalog.list_directors())

print(catalog.get_movies_by_director("Tim Burton"))
print(catalog.get_movies_by_director("Steven Spielberg"))