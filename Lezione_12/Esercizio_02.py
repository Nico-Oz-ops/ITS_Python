# Esercizio 2

class MovieCatalog:

    '''
    Attributi della classe MovieCatalog:
    - self.catalog: dict[str, list[str]]
    '''

    # il metodo __init__ ci permette di inizializzare degli oggetti della classe MovieCatalog

    def __init__(self) -> None:
        self.setCatalog()
    
    # metodi getter
    # metodo che ritorna il valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    # metodi setter
    # metodo che consente di inizializzare l'attributo self.catalog
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}

    # metodo per visualizzare i dettagli di un catalogo
    def __str__(self) -> str:
        string:str = "Catalogo:"

        if self.catalog:
            for key, values in self.catalog.items():
                temp_string:str = "\n" + str(key) + ": " + str(values)
                string += temp_string
        
        return string
        # return str(self.catalog) # opzione per far diventare il dizionario in una stringa
    
    
    # metodi della classe MovieCatalog
    # metodo che aggiunge una lista di film di uno specifico regista al catalogo

    def add_movies(self, director_name:str, movies:list[str]) -> None:
        # Check se il regista non è valido
        if not director_name:
            print("Il regista non è valido")
        
        # Check se la lista di film non è valida
        elif not movies:
            print("La lista dei film non può essere vuota")
        
        # se i dati sono validi
        else:
            # se il regista è presente nel catalogo
            if director_name in self.catalog:
                
                # aggiungere la lista movies al catalogo
                # per ogni film nella lista movies
                for movie in movies:

                    # controllare se il film movie sia stato già aggiunto al catalogo

                    # dizionario[key] -> valore
                    # director_name è la chiave del dizionario che rappresenta il nome di un regista
                    # a questa chiave corrisponde una lista di film, ovvero i film prodotti dal regista in questione
                    # self.catalog[director_name] -> è il valore associato alla chiave director_name
                    # ovvero è la lista di tutti i film prodotti dal regista
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo")
                    
                    # se il film non è presente
                    else: 

                        # aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)
            
            # se il regista non è presente nel catalogo
            else:
                # creare un nuovo record
                self.catalog[director_name] = movies
    
    # metodo che rimuove un film dalla lista dei film prodotti da un regista
    def remove_movie(self, director_name:str, movie:str) -> None:
        if not director_name:
            print("Il regista non è valido")
        
        elif not movie:
            print("Il film non è valido")
        
        # se i dati sono validi
        else:
            # se il regista è presente nel catalogo e, in caso, controllare se il film movie è nella lista dei film prodotti dal regista
            # in questione
            if director_name in self.catalog and movie in self.catalog[director_name]:
                # rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)
            
            # verificare se la lista dei film è vuota
            if not self.catalog[director_name]:

                # rimuovere il record
                del self.catalog[director_name]
    
    # metodo che ritorna una lista contenenti i nomi di registi
    def list_directors(self) -> list[str]:
        # se il dizionario self.catalog non è vuoto
        if self.catalog:
            return list(self.catalog.keys())
        
        # altrimenti se il dizionario è vuoto
        else:
            return f"Non ci sono registi nel catalogo perché il catalogo è vuoto"
    
    # metodo che dato un regista restituisce tutti i film da esso prodotti
    def get_movies_by_director(self, director_name:str) -> list[str]:
        # check se il regista non è valido
        if not director_name:
            print("Il regista non è valido")
        
        # se valido
        else:
            # controllo se il regista è nel catalogo
            if director_name in self.catalog:
                return self.catalog[director_name]
            
            # se il regista non è nel catalogo

            else:
                return f"Il regista '{director_name}' non è nel catalogo"
            