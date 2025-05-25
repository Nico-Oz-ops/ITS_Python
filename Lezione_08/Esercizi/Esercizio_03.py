# Esercizio 03

'''
Esercizio 3: Sistema di gestione della biblioteca 
Crea una classe Book contenente i seguenti attributi: titolo, autore, ISBN. 
La classe Book deve contenere i seguenti metodi:

*   __str__ , metodo per restituire una rappresentazione stringa del libro.

*   from_string , un metodo di classe per creare un'istanza di Book da una stringa 
nel formato "titolo, autore, isbn". Significa che è necessario utilizzare il riferimento 
di classe cls per creare un nuovo oggetto della classe Book utilizzando una stringa.

Esempio: 
book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)
In questo caso, divina_commedia dovrebbe essere un'istanza della classe Book con:

*   titolo = "La Divina Commedia"

*   autore = "D. Alighieri"

*   isbn = "999000666"

Crea una classe membro con i seguenti attributi: nome, member_id, borrowed_books. 
La classe membro deve contenere i seguenti metodi:

*   borrow_book, per aggiungere un libro all'elenco borrowed_books.

*   return_book, per rimuovere un libro dall'elenco borrowed_books.

*   __str__, metodo per restituire una rappresentazione stringa del membro.

*   from_string, un metodo di classe per creare un'istanza di Member da una 
    stringa nel formato "name, member_id". Significa che è necessario utilizzare 
    il riferimento di classe cls per creare un nuovo oggetto della classe Member utilizzando una stringa.

Crea una classe Libreria  con i seguenti attributi: libri, membri, totale_libri 
(ovvero, un attributo di classe per tenere traccia del numero totale di  istanze di Libro). 
La classe Libreria deve contenere i seguenti metodi:

*   add_book , per aggiungere un libro alla biblioteca e incrementare total_books.

*   remove_book , per rimuovere un libro dalla biblioteca e decrementare total_books.

*   register_member , per aggiungere un membro alla libreria.

*   lend_book , per prestare un libro a un membro. Dovrebbe verificare se il libro è 
    disponibile e se il membro è registrato.

*   __str__, metodo per restituire una rappresentazione stringa della biblioteca con 
    l'elenco dei libri e dei membri.

*   library_statistics , un metodo di classe per stampare il numero totale di libri.

Infine , scrivi un semplice programma driver. Dopo aver creato una libreria, dovresti 
iniziare creando istanze di Book e Member . Ove appropriato, usa  metodi di classe (come from_string) 
per istanziare oggetti da stringhe, migliorando la chiarezza e la modularità.

Una volta creati gli oggetti, simula alcune operazioni di base della libreria:

*   Registrare nuovi membri alla biblioteca. Questo potrebbe comportare l'aggiunta di 
    oggetti Membro a una collezione gestita dalla biblioteca.

*   Aggiungi libri alla collezione della biblioteca.

*   Prestare libri ai soci. Ciò significa contrassegnare un libro come preso in prestito e associarlo a un socio specifico.

Ad ogni passaggio significativo,  stampa lo stato della libreria per monitorare come cambia:

*   prima di prestare qualsiasi libro,
*   dopo che i libri sono stati prestati.
'''

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = isbn
    
    def __str__(self):
        return f"\n- Title: {self._title}\n- Author: {self._author}\n- ISBN: {self._isbn}"
    
    # def __repr__(self):
    #     return f"Title={self._title}; Author={self._author}; ISBN={self._isbn}"
    
    @classmethod
    def from_string(cls, str_repr: str):
        words: list[str] = str_repr.split(",")
        return cls(words[0], words[1], words[2])

class Member:
    def __init__(self, nome:str, member_id: str):
        self._nome = nome
        self._member_id = member_id
        self._borrowed_books = []
    
    def borrow_book(self, book: Book):
        self._borrowed_books.append(book)
    
    def return_book(self, book: Book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
    
    def __str__(self):
        _borrowed_books_str = "\n\n".join(str(book) for book in self._borrowed_books) or "Nessun libro in prestito"
        return f"Nome del Membro: {self._nome}\nId del Membro: {self._member_id}\nLibri in prestito: {_borrowed_books_str}\n{'-' * 50}"

    @classmethod
    def from_string(cls, member_str: str):
        words: list[str] = member_str.split(", ")
        return cls(words[0], words[1])

class Libreria:

    _total_books = 0

    def __init__(self):
        self._books = []
        self._members = []

    def add_book(self, book:Book):
        self._books.append(book)
        Libreria._total_books += 1
    
    def remove_book(self, book:Book):
        if book in self.books:
            self._books.remove(book)
            Libreria._total_books -= 1
    
    def register_member(self, member:Member):
        if member not in self._members:
            self._members.append(member)
    
    def lend_book(self, book:Book, member:Member):
        if book in self._books and member in self._members:
            member.borrow_book(book)
            self._books.remove(book)
            Libreria._total_books -= 1

        else:
            print("Libro non disponibile o membro non registrato")
    
    def __str__(self):
        _book_str = "\n\n".join(str(book) for book in self._books) or "Nessun libro disponibile"
        _member_str = "\n\n".join(str(member) for member in self._members) or "Nessun membro registrato"
        return f"Libri: {_book_str}\nMembri: {_member_str}"
    
    @classmethod
    def library_statistics(cls):
        return  f"Numero totale di libri: {cls._total_books}"

    
if __name__ == "__main__":
    # 1. creazione della libreria
    biblioteca = Libreria()

    # 2. ceazione di libri usando from_string()
    libro1 = Book.from_string("1984, George Orwell, 123456")
    libro2 = Book.from_string("Il Gattopardo, Tomasi di Lampedusa, 789012")
    libro3 = Book.from_string("La coscienza di Zeno, Italo Svevo, 345678")

    # 3. creaz<ione di membri usando from_string()
    membro1 = Member.from_string("Marcello Rossi, 001")
    membro2 = Member.from_string("Nico Nicolino, 002")

    # 4. registrazione dei membri alla biblioteca
    biblioteca.register_member(membro1)
    biblioteca.register_member(membro2)

    # 5. aggiungere libri alla collezione della biblioteca
    biblioteca.add_book(libro1)
    biblioteca.add_book(libro2)
    biblioteca.add_book(libro3)

    # 6. stato della libreria prima dei prestiti
    print("Stato della libreria PRIMA dei prestiti") 
    print(biblioteca)
    print(biblioteca.library_statistics())

    # 7. prestito di alcuni libri
    biblioteca.lend_book(libro1, membro2)
    biblioteca.lend_book(libro2, membro1)

    # 8. stato della libreria dopo i prestiti
    print("Stato della libreria DOPO i prestiti")
    print(biblioteca)
    print(biblioteca.library_statistics())




