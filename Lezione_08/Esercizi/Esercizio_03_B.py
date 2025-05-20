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

    def __init__(self, titolo: str, autore: str, isbn: str):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def __str__(self):
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nISBN: {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):

        # creo una variabile "parti" per dividere la stringa "book_str" dove si trova una virgola
        parti = book_str.split(",")

        # verifico che la stringa divisa abbia 3 parti
        if len(parti) != 3:
            raise ValueError("Errore. La longitud della stringa deve contenere 3 parti: titolo, autore e ISBN")
        
        # rimuovo eventuali spazi in più
        titolo, autore, isbn = [p.strip() for p in parti]

        # si crea e si restituisce l'oggetto Book
        return cls(titolo, autore, isbn)

class Membro:

    def __init__(self, nome: str, member_id: str):
        self.nome = nome
        self.member_id = member_id
        self.borrowed_books = []

    # aggiungere un libro alla lista dei libri presi in prestito
    def borrow_book(self, book:Book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
    
    # rimuovere un libro dalla lista dei libri in prestito, se presente
    def return_book(self, book:Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print(f"Il libro {book.titolo} non si trova nella lista.")
    
    # restituire una rappresentazione testuale del membro
    def __str__(self):

        # se non c'è nessun libro in prestito allora:
        if not self.borrowed_books:
            books_str = "Nessun libro in prestito"
        
        else:
            # converto in stringa con str(book), che chiama il metodo __str__() della classe Book.
            # unisco le stringhe dei libri con due righe di spazio tra loro
            books_str = "\n\n".join(str(book) for book in self.borrowed_books)

        return f"Informazione del membro\nNome: {self.nome}\nID: {self.member_id}\n{'-' * 30}\nLibri in prestito: \n{books_str}"
                            
    
    # crea un'istanza di Member da una stringa nel formato 'name, member_id'
    @classmethod
    def from_string(cls, member_stringa: str):

        name, member_id = member_stringa.split(", ")
        return cls(name, member_id)

# Crea libri
libro1 = Book("Il nome della rosa", "Umberto Eco", "1111111111")
libro2 = Book("El Principito", "A. de Saint-Exupéry", "2222222222")
libro3 = Book("Un Mundo Feliz", "Aldous Huxley", "33333333")
libro4 = Book("I miei stupidi intenti", "Nonmiricordo", "4444444444")

# Crea membro
membro = Membro.from_string("Giulia Rossi, 12345")

# Aggiunge libri
membro.borrow_book(libro1)
membro.borrow_book(libro2)
membro.borrow_book(libro3)
membro.borrow_book(libro4)

# Rimuove un libro
membro.return_book(libro1)

# Stampa informazioni
print(membro)

