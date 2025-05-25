from Custom_types import *
from Tipi_Dati_Voli_Aerei import *

class Volo:
    _codice: CodiceVolo # <<immutabile>>
    _durata_minuti: Durata

    def __init__(self, codice: CodiceVolo, durata_minuti: Durata):
        self._codice = codice

        self.setDurataMinuti(durata_minuti)
    
    def setDurataMinuti(self, durata_minuti: Durata) -> None:
        self._durata_minuti = durata_minuti
    
    def getDurataMinuti(self) -> Durata:
        return self._durata_minuti
    
    def getCodiceVolo(self) -> CodiceVolo:
        return self._codice
    
class Aeroporto:
    _codice: CodiceAeroporto # <<immutabile>>
    _nome: str # noto alla nascita

    def __init__(self, codice: CodiceAeroporto, nome: str):
        self._codice = codice

        self.setNome(nome)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome
    
    def getNome(self) -> str:
        return self._nome
    
    def getCodiceAeroporto(self) -> CodiceAeroporto:
        return self._codice

class Città:
    _nome: str 
    _abitanti: Abitanti

    def __init__(self, nome: str, abitanti: Abitanti):
        self.setNome(nome)
        self.setAbitanti(abitanti)
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def setAbitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti
    
    def getNome(self) -> str:
        return self._nome
    
    def getAbitanti(self) -> Abitanti:
        return self._abitanti

class CompagniaAerea:
    _nome: str
    _anno_fondazione: Data1900 # <<immutabile>>

    def __init__(self, nome: str, anno_fondazione: Data1900):
        self._anno_fondazione = anno_fondazione

        self.setNome(nome)
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome
    
    def getNome(self) -> str:
        return self._nome
    
    def getAnnoFondazione(self) -> Data1900:
        return self._anno_fondazione

class Nazione:
    _nome = str

    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido")
        self._nome = nome

    def getNome(self) -> str:
        return self._nome        
    
        

        


        


        