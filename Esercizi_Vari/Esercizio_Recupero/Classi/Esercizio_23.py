'''
Tema: Gestione di una collezione di oggetti tramite dizionario e metodi di manipolazione.

Obiettivo: Creare una classe che gestisca un insieme di entità (in questo caso libri), 
con operazioni CRUD (Create, Read, Update, Delete) e un campo booleano che può essere aggiornato.

Nome dell’esercizio: LibraryManager

Traccia:

Scrivi una classe chiamata LibraryManager che permetta di gestire una collezione di libri.
Ogni libro ha un ID, un titolo, un autore, un anno di pubblicazione, e un campo booleano 
"disponibile" (inizialmente True).

Struttura dati interna
{
    "libro1": {
        "titolo": "Il nome della rosa",
        "autore": "Umberto Eco",
        "anno": 1980,
        "disponibile": True
    }
}

Metodi richiesti:

* add_book(self, book_id: str, titolo: str, autore: str, anno: int) -> dict | str
Aggiunge un nuovo libro alla collezione.
Se l’ID esiste già, solleva un ValueError.

* update_book(self, book_id: str, nuovo_titolo: str, nuovo_autore: str, nuovo_anno: int) -> dict | str
Aggiorna i dati del libro.
Se l’ID non esiste, solleva un ValueError.

* remove_book(self, book_id: str) -> dict | str
Rimuove il libro dalla collezione.
Se l’ID non esiste, solleva un ValueError.

* mark_unavailable(self, book_id: str) -> dict | str
Imposta disponibile a False per il libro specificato.
Se l’ID non esiste, solleva un ValueError.

* list_books(self) -> list[str]
Restituisce una lista degli ID di tutti i libri presenti.

* get_book(self, book_id: str) -> dict | str
Restituisce i dettagli di un libro dato il suo ID.
Se il libro non esiste, restituisce "Libro non trovato".
'''