'''
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

'''

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed: bool = False
    
    def borrow(self) -> None:
        if self.is_borrowed:
            raise ValueError("Libro non disponibile")
        self.is_borrowed = True

    
    def return_book(self) -> None:
        if not self.is_borrowed:
            raise ValueError("Il libro risultava già disponibile")
        self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)

        else:
            print("Il libro non è disponibile per il prestito")
    
    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()

        else:
            print("Il libro non resulta presente tra i libri in prestito dall'utente")

class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            print("Il libro esiste già")
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)

        else:
            print("Il membro esiste già")
    
    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)
        
        else:
            print("Membro o libro in prestito non trovato")
    
    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        
        else:
            print("Membro o libro in prestito non trovato")
    
    def get_borrowed_books(self, member_id: str) -> list[Book]:
        if member_id in self.members:
            member = self.members[member_id]

            return [book.title for book in member.borrowed_books]
        
        else:
            return "Membro non trovato"


 	

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

library.borrow_book("M001", "B001")
try:
    library.borrow_book("M002", "B001")
except ValueError as e:
    print(e)


'''
class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed: bool = False
    
    def borrow(self) -> None:
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True
    
    def return_book(self) -> None:
        if not self.is_borrowed:
            raise ValueError("Book is already available")
        self.is_borrowed = False


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            raise ValueError("Book already borrowed by this member")
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            raise ValueError("Book is already borrowed")
    
    def return_book(self, book: Book) -> None:
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")
        self.borrowed_books.remove(book)
        book.return_book()


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            raise ValueError("Book already exists")
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
        else:
            raise ValueError("Member already exists")
    
    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        
        member = self.members[member_id]
        book = self.books[book_id]
        member.borrow_book(book)
    
    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        
        member = self.members[member_id]
        book = self.books[book_id]
        member.return_book(book)
    
    def get_borrowed_books(self, member_id: str) -> list[str]:
        if member_id not in self.members:
            raise ValueError("Member not found")
        member = self.members[member_id]
        return [book.title for book in member.borrowed_books]
'''