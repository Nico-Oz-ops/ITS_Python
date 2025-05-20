from Persona import Persona
from abc import ABC, abstractmethod

class Studente(Persona):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, matricola: int):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)
    
        self.setMatricola(matricola) # impostazione della matricola con validazione
    
    def setMatricola(self, matricola: int):
        if not isinstance(matricola, int) or matricola <= 0:
            raise ValueError("Errore. Numero di matricola non valido")
        
        self.matricola = matricola

    def getMatricola(self):
        return self.matricola  
   
    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getDataNascita(self):
        return self.data_nascita
    
    def getCodiceFiscale(self):
        return self.codice_fiscale
    
    def __eq__(self, other):
        if isinstance(other, Studente):
            return self.matricola == other.matricola
        return False
    
    def __hash__(self):
        return hash(self.matricola)

class Impiegato(Persona, ABC):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.setStipendio(stipendio) # impostazione dello stipendio con validazione
    
    @abstractmethod
    def setStipendio(self, stipendio: float):
        pass

    @abstractmethod
    def getStipendio(self):
        pass

    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getDataNascita(self):
        return self.data_nascita
    
    def getCodiceFiscale(self):
        return self.codice_fiscale

class Direttore(Impiegato):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)

    def setStipendio(self, stipendio: float):
        if not isinstance(stipendio, float) or stipendio <= 0:
            raise ValueError("Errore. Lo stipendio deve essere un valore positivo")
        
        self.stipendio = stipendio
    
    def getStipendio(self):
        return self.stipendio

class Segretario(Impiegato):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, stipendio: float):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)

    def setStipendio(self, stipendio: float):
        if not isinstance(stipendio, float) or stipendio <= 0:
            raise ValueError("Errore. Lo stipendio deve essere un valore positivo")
        
        self.stipendio = stipendio
    
    def getStipendio(self):
        return self.stipendio

class Progettista(Impiegato):
    
    def __init__(self, nome, cognome, data_nascita, codice_fiscale, stipendio, progetti=None):
        super().__init__(nome, cognome, data_nascita, codice_fiscale, stipendio)

        self.setProgetti(progetti if progetti is not None else [])
    
    def setProgetti(self, progetti):
        if not isinstance(progetti, list) or not all(isinstance(progetto, Progetto) for progetto in progetti):
            raise ValueError("Errore. Si deve fornire una lista di progetti")
        self.progetti = progetti
    
    def getProgetti(self):
        return self.progetti
    
    def haProgetti(self) -> bool:
        if len(self.progetti) == 0:
            print(f"{self.nome} non ha progetti.")
            return False
        return True

    def setStipendio(self, stipendio: float):
        if not isinstance(stipendio, float) or stipendio <= 0:
            raise ValueError("Errore. Lo stipendio deve essere un valore positivo")
        
        self.stipendio = stipendio
    
    def getStipendio(self):
        return self.stipendio

class Progetto:

    def __init__(self, nome: str):
        self.setNome(nome)
    
    def setNome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Il nome del progetto non è valido.")
        self.nome = nome
    
    def getNome(self):
        return self.nome
