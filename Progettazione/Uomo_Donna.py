from Persona import Persona

class PosizioneMilitare:

    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Il nome della posizione militare non è valido")
        self.nome = nome
    
    def getNome(self):
        return self.nome

class Uomo(Persona):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, posizione_militare: PosizioneMilitare):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)

        self.setPosizioneMilitare(posizione_militare)
    
    def setPosizioneMilitare(self, posizione_militare):
        if not isinstance(posizione_militare, PosizioneMilitare):
            raise ValueError("Errore. Deve essere un'istanza di PosizioneMilitare.")
        
        self.posizione_militare = posizione_militare
    
    def getPoszioneMilitare(self):
        return self.posizione_militare

    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getDataNascita(self):
        return self.data_nascita
    
    def getCodiceFiscale(self):
        return self.codice_fiscale

class Donna(Persona):

    def __init__(self, nome, cognome, data_nascita, codice_fiscale, maternità: int):
        super().__init__(nome, cognome, data_nascita, codice_fiscale)
        self.maternità = maternità

    def setMaternità(self, maternità):
        if not isinstance(maternità, int) or maternità < 0:
            raise ValueError("Errore. Il numero di maternità deve essere un intero positivo")
        
        self.maternità = maternità

    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getDataNascita(self):
        return self.data_nascita
    
    def getCodiceFiscale(self):
        return self.codice_fiscale

    def getMaternità(self):
        return self.maternità