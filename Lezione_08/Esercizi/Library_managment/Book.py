
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
        borrowed_books_str = "\n\n".join(str(book) for book in self._borrowed_books) or "Nessun libro in prestito"
        return f"Nome del Membro: {self._nome}\nId del Membro: {self._member_id}\nLibri in prestito: {borrowed_books_str}\n{'-' * 50}"

    @classmethod
    def from_string(cls, member_str: str):
        words: list[str] = member_str.split(",")
        return cls(words[0], words[1])

class Libreria:

    total_books = 0

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book:Book):
        self.books.append(book)
        Libreria.total_books += 1
    
    def remove_book(self, book:Book):
        if book in self.books:
            self.books.remove(book)
            Libreria.total_books -= 1
    
    def register_member(self, member:Member):
        if member not in self.members:
            self.members.append(member)
    
    def lend_book(self, book:Book, member:Member):
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.books.remove(book)
            Libreria.total_books -= 1

        else:
            print("Libro non disponibile o membro non registrato")
    
    def __str__(self):
        book_str = "\n".join(str(book) for book in self.books) or "Nessun libro disponibile"
        member_str = "\n".join(str(member) for member in self.members) or "Nessun membro registrato"
        return f"Libri: {book_str}\nMembri: {member_str}"
    
    @classmethod
    def library_statistics(cls):
        return  f"Numero totale di libri: {cls.total_books}"

    
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




