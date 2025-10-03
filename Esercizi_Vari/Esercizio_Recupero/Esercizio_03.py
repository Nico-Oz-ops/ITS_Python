'''
Crea una classe chiamata LibraryManager che permetta di gestire una raccolta di libri. Ogni libro ha:
un ISBN (stringa univoca),
un titolo (stringa),
un autore (stringa),
un flag disponibile (booleano, True se il libro è disponibile per il prestito).
{
    "978-3-16-148410-0": {
        "titolo": "Il nome della rosa",
        "autore": "Umberto Eco",
        "disponibile": True
    }
}
Metodi richiesti:
- add_book(self, isbn: str, titolo: str, autore: str) -> dict | str
Aggiunge un nuovo libro al catalogo. disponibile sarà inizialmente True.
Se l’ISBN è già presente, solleva un ValueError.
 
- borrow_book(self, isbn: str) -> dict | str
Imposta disponibile a False, se il libro è disponibile.
Se il libro non esiste, solleva ValueError.
Se non è disponibile, restituisce "Libro non disponibile".
 
- return_book(self, isbn: str) -> dict | str
Imposta disponibile a True.
Se il libro non esiste, solleva ValueError.
 
- remove_book(self, isbn: str) -> dict | str
Rimuove il libro dal catalogo.
Se il libro non esiste, solleva ValueError.
 
- list_books(self) -> list[str]
Restituisce una lista di ISBN di tutti i libri in catalogo.
 
- get_book(self, isbn: str) -> dict | str
Restituisce i dettagli del libro dato il suo ISBN.
Se il libro non esiste, restituisce "Libro non trovato".
'''