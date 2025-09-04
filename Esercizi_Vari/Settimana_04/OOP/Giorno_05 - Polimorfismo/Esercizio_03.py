'''
Esercizio 3 - Dipendenti (versione chiara)

Tema: Polimorfismo + gestione attributi
Obiettivo: Calcolo dello stipendio con logiche diverse per ciascun tipo di dipendente.

Traccia:

1. Crea una classe astratta Dipendente con:

    * Attributo nome (stringa)
    * Metodo astratto calcola_stipendio()

2. Crea le sottoclassi:

    * DipendenteFisso:

        * Attributo stipendio_base
        * calcola_stipendio() restituisce sempre stipendio_base

    * DipendenteOrario:

        * Attributi paga_oraria e ore_lavorate
        * calcola_stipendio() restituisce paga_oraria * ore_lavorate

    * DipendenteCommissione:

        * Attributi stipendio_base, vendite_totali, percentuale
        * calcola_stipendio() restituisce stipendio_base + vendite_totali * percentuale / 100

3. Crea una lista mista di dipendenti di tutti e tre i tipi e stampa per ognuno:

    * Nome del dipendente
    * Tipo di dipendente
    * Stipendio calcolato tramite calcola_stipendio()
'''
from abc import ABC, abstractmethod

class Dipendente(ABC):
    def __init__(self, nome: str):
        self.nome = nome
    
    def get_nome(self) -> str:
        return self.nome
    
    @abstractmethod
    def calcola_stipendio(self):
        pass

class DipendenteFisso(Dipendente):
    def __init__(self, nome, stipendio_base: int|float):
        super().__init__(nome)
        self.set_stipendio_base(stipendio_base)
    
    def get_stipendio_base(self) -> int|float:
        return self.__stipendio_base
    
    def set_stipendio_base(self, stipendio_base: int|float):
        if not isinstance(stipendio_base, (int, float)) or stipendio_base <= 0:
            raise ValueError("Stipendio base non valido.")
        self.__stipendio_base = stipendio_base
    
    def calcola_stipendio(self):
        return self.__stipendio_base

class DipendenteOrario(Dipendente):
    def __init__(self, nome, paga_oraria: int|float, ore_lavorate: int):
        super().__init__(nome)
        self.set_paga_oraria(paga_oraria)
        self.set_ore_lavorate(ore_lavorate)
    
    def get_paga_oraria(self):
        return self.__paga_oraria
    
    def get_ore_lavorate(self):
        return self.__ore_lavorate
    
    def set_paga_oraria(self, paga_oraria):
        if not isinstance(paga_oraria, (int, float)) or paga_oraria <= 0:
            raise ValueError("Paga oraria non valida.")
        self.__paga_oraria = paga_oraria
    
    def set_ore_lavorate(self, ore_lavorate):
        if not isinstance(ore_lavorate, int) or ore_lavorate < 0:
            raise ValueError("Ore lavorate non valide.")
        self.__ore_lavorate = ore_lavorate
    
    def calcola_stipendio(self):
        return self.__paga_oraria * self.__ore_lavorate

class DipendenteCommissione(Dipendente):
    def __init__(self, nome, stipendio_base: int|float, vendite_totali: int|float, percentuale: float):
        super().__init__(nome)
        self.set_stipendio_base(stipendio_base)
        self.set_vendite_totali(vendite_totali)
        self.set_percentuale(percentuale)
    
    def get_stipendio_base(self) -> int|float:
        return self.__stipendio_base
    
    def get_vendite_totali(self) -> int|float:
        return self.__vendite_totali
    
    def get_percentuale(self) -> int|float:
        return self.__percentuale
    
    def set_stipendio_base(self, stipendio_base):
        if not isinstance(stipendio_base, (int, float)) or stipendio_base <= 0:
            raise ValueError("Stipendio Base non valido.")
        self.__stipendio_base = stipendio_base
    
    def set_vendite_totali(self, vendite_totali):
        if not isinstance(vendite_totali, (int, float)) or vendite_totali < 0:
            raise ValueError("Vendite totali non valide.")
        self.__vendite_totali = vendite_totali
    
    def set_percentuale(self, percentuale: int|float):
        if not isinstance(percentuale, (int, float)) or percentuale <= 0:
            raise ValueError("Percentuale non valida.")
        self.__percentuale = percentuale
    
    def calcola_stipendio(self):
        return self.__stipendio_base + self.__vendite_totali * (self.__percentuale / 100)

dipendente1 = DipendenteFisso("Luca", 2200.00)
dipendente2 = DipendenteOrario("Maria", 15.50, 160)
dipendente3 = DipendenteCommissione("Giovanni", 1200.00, 8000.00, 5)

dipendenti = [dipendente1, dipendente2, dipendente3]
for dipendente in dipendenti:
    print(f"Nome: {dipendente.get_nome()}\nTipo di dipendente: {dipendente.__class__.__name__}\nStipendio: {dipendente.calcola_stipendio():.2f}\n")