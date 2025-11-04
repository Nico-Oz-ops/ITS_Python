'''
Esercizio: Gestore di Biblioteca (LibraryManager)

Scrivi una classe chiamata LibraryManager che gestisca i libri disponibili in una biblioteca.
Ogni libro è salvato in un dizionario principale, dove la chiave è l’ID del libro e 
il valore è un sotto-dizionario con i dettagli.

Struttura dati:
self.libri = {
    "b001": {
        "titolo": "Il signore degli anelli",
        "autore": "J.R.R. Tolkien",
        "copie": 3
    },
    "b002": {
        "titolo": "1984",
        "autore": "George Orwell",
        "copie": 5
    }
}

Metodi richiesti:

* add_book(book_id: str, titolo: str, autore: str, copie: int) -> dict | str
Aggiunge un nuovo libro alla biblioteca.

    * Se l’ID esiste già, restituisce "Errore, libro già presente."
    * Altrimenti aggiunge il libro e restituisce il dizionario del libro aggiunto.


* update_copies(book_id: str, nuove_copie: int) -> dict | str
Aggiorna il numero di copie disponibili.

    * Se l’ID non esiste, restituisce "Errore, libro non trovato."
    * Se esiste, aggiorna e restituisce il dizionario aggiornato.


* update_author(book_id: str, nuovo_autore: str) -> dict | str
Modifica il nome dell’autore associato a un libro.

    * Se l’ID non esiste, restituisce "Errore, libro non trovato."
    * Se esiste, restituisce il libro aggiornato.


* remove_book(book_id: str) -> dict | str
Rimuove un libro dall’archivio e restituisce i suoi dati.

    * Se l’ID non esiste, restituisce "Errore, libro non trovato."


* get_book(book_id: str) -> dict | str
Restituisce i dettagli completi di un libro.

    * Se l’ID non esiste, restituisce "Errore, libro non trovato."


* list_books() -> list[str]
Restituisce la lista di tutti gli ID dei libri presenti nella biblioteca.


* find_by_title(titolo: str) -> dict | str
Cerca tutti i libri che corrispondono (anche parzialmente e senza distinzione 
tra maiuscole e minuscole) al titolo indicato.

    * Se trova corrispondenze, restituisce un dizionario con i risultati.
    * Se non trova nulla, restituisce "Nessun libro trovato con questo titolo."
'''