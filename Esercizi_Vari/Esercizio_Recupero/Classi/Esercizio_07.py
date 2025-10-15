'''
Esercizio: Sistema di Gestione di una Biblioteca Digitale
Implementa tre classi interagenti per gestire il prestito e la restituzione dei libri digitali.

1. Classe EBook
Rappresenta un libro digitale disponibile per il prestito.

A. Attributi:

* book_id: str
* title: str
* author: str
* is_borrowed: bool

B. Metodi:

    * borrow() -> None
    Se is_borrowed è False, lo imposta a True; altrimenti stampa:
    "Il libro '{self.title}' di {self.author} è già in prestito."

    * return_book() -> None
    Se is_borrowed è True, lo imposta a False; altrimenti stampa:
    "Il libro '{self.title}' di {self.author} non è attualmente in prestito."

2. Classe User

A. Attributi:

* user_id: str
* name: str
* borrowed_books: list[EBook]

B. Metodi:

    * borrow_book(book: EBook) -> None
    Se il libro non è già in prestito, lo aggiunge a borrowed_books e chiama book.borrow().
    Altrimenti stampa:
    "Il libro '{book.title}' non è disponibile per il prestito."

    * return_book(book: EBook) -> None
    Se il libro è in borrowed_books, lo rimuove e chiama book.return_book().
    Altrimenti stampa:
    "Il libro '{book.title}' non è stato preso in prestito da questo utente."

3. Classe DigitalLibrary

A. Attributi:

* books: dict[str, EBook]
* users: dict[str, User]

B. Metodi:

    * add_book(book_id: str, title: str, author: str) -> None
    Se book_id esiste già, stampa:
    "Il libro con ID '{book_id}' esiste già."
    Altrimenti crea e aggiunge un nuovo EBook.

    * register_user(user_id: str, name: str) -> None
    Se user_id esiste già, stampa:
    "L'utente con ID '{user_id}' è già registrato."
    Altrimenti crea e aggiunge un nuovo User.

    * borrow_book(user_id: str, book_id: str) -> None
    Se entrambi esistono, invoca user.borrow_book(book)
    Altrimenti stampa:
    "Utente o libro non trovato."

    * return_book(user_id: str, book_id: str) -> None
    Se entrambi esistono, invoca user.return_book(book)
    Altrimenti stampa:
    "Utente o libro non trovato."

    * list_available_books() -> list[str]
    Restituisce una lista di book_id non in prestito.

    * list_user_borrowed_books(user_id: str) -> list[str] | str
    Se l’utente esiste, restituisce una lista di book_id presi in prestito.
    Altrimenti restituisce:
    "Errore: utente non trovato."
'''