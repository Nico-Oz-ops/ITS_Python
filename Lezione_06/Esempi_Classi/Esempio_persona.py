class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe Persona).
    Le informazioni saranno:
    - nome
    - cognome
    - età

    Come li rappresento in Python?

    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)

    '''

    # costruttore, serve a inizializzare la classe
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
