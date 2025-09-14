'''
Progetto 3 - Sistema bancario (con classe astratta)
Tema: OOP - Mini-progetto bancario con classi astratte, ereditarietà e polimorfismo.

Obiettivo: Creare un sistema bancario con classi astratte, gestione del saldo e polimorfismo.

Traccia:

1. Crea una classe astratta ContoBase con:

    * attributi: intestatario, saldo
    * metodi astratti: preleva(importo) e __str__()
    * metodi concreti: deposita(importo)

2. Crea due sottoclassi concrete:

    * ContoCorrente → implementa preleva() e __str__()
    * ContoRisparmio → implementa preleva() e __str__(), aggiunge attributo interesse e metodo applica_interesse()

3. Crea una classe Banca con:

    * attributi: nome_banca, conti
    * metodi: aggiungi_conto(conto) e mostra_conti()

4. Dimostra il polimorfismo:

    * crea almeno un ContoCorrente e un ContoRisparmio
    * deposita e preleva somme diverse
    * applica l’interesse sul conto risparmio
    * stampa tutti i conti usando __str__() → comportamenti diversi ma stessa interfaccia ContoBase
'''

from abc import ABC, abstractmethod

class ContoBase(ABC):
    def __init__(self, intestatario: str, saldo: float):
        self.intestatario = intestatario
        self.saldo = saldo
    
    @property
    def intestatario(self):
        return self._intestatario
    
    @intestatario.setter
    def intestatario(self, intestatario: str):
        if not isinstance(intestatario, str) or intestatario.strip() == "":
            raise ValueError("Intestatario non valido.")
        self._intestatario = intestatario
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo: int|float):
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("Saldo non valido")
        self._saldo = float(saldo)
    
    @abstractmethod
    def preleva(self, importo: int|float):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def deposita(self, importo: int|float):
        if not isinstance(importo, (int, float)) or importo <= 0:
            raise ValueError("Importo di deposito non valido")
        self.saldo += importo
    

class ContoCorrente(ContoBase):
    def __init__(self, intestatario, saldo):
        super().__init__(intestatario, saldo)
    
    def preleva(self, importo: int|float):
        if not isinstance(importo, (int, float)) or importo <= 0 or importo > self.saldo:
            raise ValueError("Importo di prelievo non valido")
        self.saldo -= importo
    
    def __str__(self):
        return f"**Conto Corrente**\nIntestatario: {self.intestatario}\nSaldo attuale: {self.saldo:.2f}"

class ContoRisparmio(ContoBase):
    def __init__(self, intestatario, saldo, interesse: float):
        super().__init__(intestatario, saldo)
        self.interesse = interesse
    
    @property
    def interesse(self):
        return self._interesse
    
    @interesse.setter
    def interesse(self, interesse: float):
        if not isinstance(interesse, (int, float)) or interesse < 0:
            raise ValueError("Interesse non valido")
        self._interesse = float(interesse)
    
    def preleva(self, importo: int|float):
        if not isinstance(importo, (int, float)) or importo <= 0 or importo > self.saldo:
            raise ValueError("Importo di prelievo non valido")
        self.saldo -= importo

    def applica_interesse(self):
        self.saldo += self.saldo * self.interesse
    
    def __str__(self):
        return f"**Conto Risparmio**\nIntestatario: {self.intestatario}\nSaldo attuale: {self.saldo:.2f}\nInteresse: {self.interesse * 100:.2f}%"

class Banca:
    def __init__(self, nome_banca: str, conti: list[ContoBase] = None):
        self.nome_banca = nome_banca
        self.conti = conti if conti is not None else []
    
    @property
    def nome_banca(self):
        return self._nome_banca
    
    @nome_banca.setter
    def nome_banca(self, nome_banca: str):
        if not isinstance(nome_banca, str) or nome_banca.strip() == "":
            raise ValueError("Nome della Banca non valido")
        self._nome_banca = nome_banca
    
    @property
    def conti(self):
        return self._conti
    
    @conti.setter
    def conti(self, conti: list[ContoBase]):
        for conto in conti:
            if not isinstance(conto, ContoBase):
                raise ValueError("Conto non valido")
        self._conti = conti
    
    def aggiungi_conto(self, conto: ContoBase):
        if not isinstance(conto, ContoBase):
            raise ValueError("Conto non valido")
        self.conti.append(conto)
    
    def mostra_conti(self):
        for conto in self.conti:
            print(conto)


conto_corrente = ContoCorrente("Mattia", 0)
conto_risparmio = ContoRisparmio("Miguel", 0, 0.02)

conto_corrente.deposita(2000)
conto_risparmio.deposita(5000)

conto_corrente.preleva(250)
conto_risparmio.preleva(125)

conto_risparmio.applica_interesse()

print(conto_corrente)
print("-" * 30)
print(conto_risparmio)


