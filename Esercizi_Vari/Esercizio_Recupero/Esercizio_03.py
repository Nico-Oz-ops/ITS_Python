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

class LibraryManager:
    def __init__(self):
        self.libri = {}
    

    def add_book(self, isbn: str, titolo: str, autore: str) -> dict|str:
        if isbn in self.libri:
            raise ValueError("Errore: il libro è già presente nel catalogo")
        self.libri[isbn] = {"titolo": titolo, "autore": autore, "disponibile": True}
        return {isbn: self.libri[isbn]}
    
    def borrow_book(self, isbn: str) -> dict|str:
        if isbn not in self.libri:
            raise ValueError("Errore: il libro non esiste in questo catalogo")
        
        if self.libri[isbn]["disponibile"] == False:
            return "Libro non disponibile"
        else:
            self.libri[isbn]["disponibile"] = False
            return {isbn: self.libri[isbn]}

    def return_book(self, isbn: str):
        if isbn not in self.libri:
            raise ValueError("Errore: il libro non esiste")
        self.libri[isbn]["disponibile"] = True
        return {isbn: self.libri[isbn]}
    
    def remove_book(self, isbn: str):
        if isbn not in self.libri:
            raise ValueError("Errore: il libro non esiste")
        libro_rimosso = self.libri.pop(isbn)
        return {isbn: libro_rimosso}
    
    def list_books(self) -> list[str]:
        return list(self.libri.keys()) # oppure return [libro for libro in self.libri.keys()]
    
    def get_book(self, isbn: str):
        if isbn not in self.libri:
            return "Libro non trovato"
        return {isbn: self.libri[isbn]}
    


        

        