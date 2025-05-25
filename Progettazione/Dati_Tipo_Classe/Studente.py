
from Custom_Types import *


class Studente:
    _mat: int # <<imm>> noto alla nascita
    _nome: str # noto alla nascita
    _genere: str # noto alla nascita
    _telefono: set[Telefono] # noto alla nascita [1..*]
    _email: set[Email] # non noto alla nascita [0..*]

    def __init__(self, mat: int, nome: str, genere: str, telefono: Telefono):
        self._email = set()
        self._telefono = set()
        self._mat = mat
        self.set_nome(nome)
        self.set_genere(genere)
        self.add_telefono(telefono)
        
    
    def matricola(self) -> int:
        return self._mat
    
    def nome(self) -> str:
        return self._nome
    
    def genere(self) -> str:
        return self._genere
    
    def telefoni(self) -> frozenset[Telefono]:
        return frozenset(self._telefono)
    
    def emails(self) -> frozenset[Email]:
        return frozenset(self._email)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_genere(self, genere: str) -> None:
        self._genere = genere
    
    def add_telefono(self, telefono: Telefono) -> None:
        self._telefono.add(telefono)
    
    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefono) >= 2:
            self._telefono.remove(telefono)
        else:
            raise RuntimeError("Lo studente deve avere almeno un numero di telefono")

    def add_email(self, email: Email) -> None:
        self._email.add(email)
    
    def remove_email(self, email: Email) -> None:
        if len(self._email) >= 1:
            self._email.remove(email)
