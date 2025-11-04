'''
Esercizio: Sistema di Gestione di una Biblioteca Digitale

Implementa tre classi interagenti per gestire il prestito e la restituzione di libri digitali.

1. Classe BookLoan
Rappresenta un prestito di un libro digitale.

A. Attributi:
    * loan_id: str
    * book_title: str
    * due_date: str (es. "2025-11-10")
    * is_loaned: bool

B. Metodi:
* borrow() -> None
Se is_loaned è False, lo imposta a True; altrimenti stampa:
"Il libro '{self.book_title}' è già in prestito."

* return_book() -> None
Se is_loaned è True, lo imposta a False; altrimenti stampa:
"Il libro '{self.book_title}' non risulta in prestito."


2. Classe Member

A. Attributi:
    * member_id: str
    * name: str
    * active_loans: list[BookLoan]

B. Metodi:
* borrow_book(loan: BookLoan) -> None
Se il libro non è in prestito, lo aggiunge a active_loans e chiama loan.borrow().
Altrimenti stampa:
"Il libro '{loan.book_title}' non è disponibile per il prestito."

* return_book(loan: BookLoan) -> None
Se il libro è in active_loans, lo rimuove e chiama loan.return_book().
Altrimenti stampa:
"Il libro '{loan.book_title}' non risulta tra i prestiti attivi del membro."


3. Classe DigitalLibrary

A. Attributi:
    * loans: dict[str, BookLoan]
    * members: dict[str, Member]

B. Metodi:
* add_loan(loan_id: str, book_title: str, due_date: str) -> None
Se loan_id esiste già, stampa:
"Il prestito con ID '{loan_id}' esiste già."
Altrimenti crea e aggiunge un nuovo BookLoan.

* register_member(member_id: str, name: str) -> None
Se member_id esiste già, stampa:
"Il membro con ID '{member_id}' è già registrato."
Altrimenti crea e aggiunge un nuovo Member.

* borrow_book(member_id: str, loan_id: str) -> None
Se entrambi esistono, invoca member.borrow_book(loan).
Altrimenti stampa:
"Membro o prestito non trovato."

* return_book(member_id: str, loan_id: str) -> None
Se entrambi esistono, invoca member.return_book(loan).
Altrimenti stampa:
"Membro o prestito non trovato."

* list_available_books() -> list[str]
Restituisce una lista di loan_id non ancora in prestito.

* list_member_loans(member_id: str) -> list[str] | str
Se il membro esiste, restituisce una lista di loan_id attivi.
Altrimenti restituisce:
"Errore: membro non trovato."
'''

class BookLoan:
    def __init__(self, loan_id: str, book_title: str, due_date: str) -> None:
        self.loan_id = loan_id
        self.book_title = book_title
        self.due_date = due_date
        self.is_loaned: bool = False
    
    def borrow(self) -> None:
        if not self.is_loaned:
            self.is_loaned = True
        else:
            print(f"Il libro '{self.book_title}' è già in prestito.")
    
    def return_book(self) -> None:
        if self.is_loaned:
            self.is_loaned = False
        else:
            print(f"Il libro '{self.book_title}' non risulta in prestito.")

class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.active_loans: list[BookLoan] = []

    def borrow_book(self, loan: BookLoan) -> None:
        if not loan.is_loaned:
            loan.borrow()
            self.active_loans.append(loan)
        else:
            print(f"Il libro '{loan.book_title}' non è disponibile per il prestito.")
    
    def return_book(self, loan: BookLoan) -> None:
        if loan in self.active_loans:
            self.active_loans.remove(loan)
            loan.return_book()     
        else:
            print(f"Il libro '{loan.book_title}' non risulta tra i prestiti attivi del membro.")   
    

class DigitalLibrary:
    def __init__(self):
        self.loans: dict[str, BookLoan] = {}
        self.members: dict[str, Member] = {}
    
    def add_loan(self, loan_id: str, book_title: str, due_date: str) -> None:
        if loan_id in self.loans:
            print(f"Il prestito con ID {loan_id} esiste già.")
        else:
            self.loans[loan_id] = BookLoan(loan_id, book_title, due_date)
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id in self.members:
            print(f"Il membro con ID {member_id} è già registrato.")
        else:
            self.members[member_id] = Member(member_id, name)
    
    def borrow_book(self, member_id: str, loan_id: str) -> None:
        if member_id in self.members and loan_id in self.loans:

            member = self.members[member_id]
            loan = self.loans[loan_id]

            member.borrow_book(loan)
        
        else:
            print("Membro o prestito non trovato.")
    
    def return_book(self, member_id: str, loan_id: str) -> None:
        if member_id in self.members and loan_id in self.loans:

            member = self.members[member_id]
            loan = self.loans[loan_id]

            member.return_book(loan)

        else:
            print("Membro o prestito non trovato.")

    def list_available_books(self) -> list[str]:
        return [loan_id for loan_id, loan in self.loans.items() if not loan.is_loaned]
    
    def list_member_loans(self, member_id: str) -> list[str]|str:
        if member_id in self.members:
            member = self.members[member_id]

            return [loan.loan_id for loan in member.active_loans]
        
        else:
            return "Errore, membro non trovato."
