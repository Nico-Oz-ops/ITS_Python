from typing import Any
from abc import ABC, abstractmethod
import re
import datetime

# data_str = "31/03/2025"
# data = datetime.datetime.strptime(data_str, "%d/%m/%Y")

# print(data_str)

class CodiceFiscale:

    def __new__(cls, codice_fiscale: str):

        if not re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", codice_fiscale):
            raise ValueError(f"Errore. Il codice fiscale inserito '{codice_fiscale}' non è valido.")
       
        instance = super().__new__(cls)
        instance.codice_fiscale = codice_fiscale

        return instance
    
    def __str__(self):
        return self.codice_fiscale
    
    def __eq__(self, other):
        if isinstance(other, CodiceFiscale):
            return self.codice_fiscale == other.codice_fiscale
        return NotImplemented
    
    def __hash__(self):
        return hash(self.codice_fiscale)

class DataNascita:

    def __new__(cls, data_nascita: str):

        if not re.fullmatch(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$", data_nascita):
            raise ValueError(f"Error. La data di nascita inserita '{data_nascita}' non è in un formato valido.")
           
        # Per verificare la validità della data inserita, parsing
        try:
            parsed = datetime.datetime.strptime(data_nascita, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"Errore. La data '{data_nascita}' non esiste nel calendario")
        
        oggi = datetime.date.today()
        max_passato = oggi.replace(year=oggi.year - 130) # limite massimo: 130 anni fa

        if parsed > oggi:
            raise ValueError(f"Errore. La data '{data_nascita}' è nel futuro")
        if parsed < max_passato:
            raise ValueError(f"Errore. La data '{data_nascita}' è troppo vecchia.")

        instance = super().__new__(cls)
        instance.data_nascita = parsed

        return instance
    
    def __str__(self):
        return self.data_nascita.strftime("%d/%m/%Y")
    
    def __eq__(self, other):
        if isinstance(other, DataNascita):
            return self.data_nascita == other.data_nascita    
        return NotImplemented
    
    def __hash__(self):
        return hash(self.data_nascita)
    
class Persona(ABC):

    def __init__(self, nome: str, cognome: str, data_nascita: DataNascita, codice_fiscale: CodiceFiscale):

        self.setNome(nome)
        self.setCognome(cognome)
        self.setDataNascita(data_nascita)
        self.setCodiceFiscale(codice_fiscale)

    def setNome(self, nome):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError(f"Il nome inserito non è valido.")
        else: 
            self.nome = nome

    def setCognome(self, cognome):
        if not isinstance(cognome, str) or cognome.strip() == "":
            raise ValueError(f"Il cognome inserito non è valido.")
        else: 
            self.cognome = cognome

    def setDataNascita(self, data_nascita):
        self.data_nascita = data_nascita

    def setCodiceFiscale(self, codice_fiscale):
        self.codice_fiscale = codice_fiscale
    
    @abstractmethod
    def getNome(self):
        pass

    @abstractmethod
    def getCognome(self):
        pass
    
    @abstractmethod
    def getDataNascita(self):
        pass
    
    @abstractmethod
    def getCodiceFiscale(self):
        pass
    
    def __str__(self):
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nData di Nascita: {self.data_nascita}\nCodice Fiscale: {self.codice_fiscale}"


# creazione di un oggetto DataNascita e CodiceFiscale
# data_nascita = DataNascita("29/12/1900")
# codice_fiscale = CodiceFiscale("HNZBPD28H04H101X")

# # creazione dell'oggetto Persona
# p = Persona("Nico", "Ro", data_nascita, codice_fiscale)
# print(p)
