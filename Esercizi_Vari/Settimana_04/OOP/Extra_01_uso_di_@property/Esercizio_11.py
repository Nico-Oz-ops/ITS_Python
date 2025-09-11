'''
Esercizio 11 - Conto Bancario

Tema: Gestione di dati sensibili con proprietà.
Obiettivo: Creare una classe che rappresenti un conto bancario con controllo sugli accessi e sulle operazioni.

Traccia:

1. Crea una classe ContoBancario con gli attributi:

    * titolare (stringa, non vuota)
    * saldo (float o int, inizialmente ≥ 0)

2. Usa @property per gestire saldo, impedendo valori negativi.

3. Implementa i metodi:

    * deposita(importo) → aumenta il saldo se l’importo è positivo.
    * preleva(importo) → diminuisce il saldo se l’importo è valido e non superiore al saldo disponibile.

4. Aggiungi il metodo __str__ che mostra il nome del titolare e il saldo corrente.

Suggerimento: nel setter di saldo, assicurati che non possa mai andare sotto zero.
'''
class ContoBancario:
    def __init__(self, titolare: str, saldo: int|float):
        self.titolare = titolare # property pubblica
        self.saldo = saldo # property pubblica
    
    @property
    def titolare(self):
        return self._titolare # legge l'attributo interno
    
    @titolare.setter
    def titolare(self, titolare: str):
        if not isinstance(titolare, str) or titolare.strip() == "":
            raise ValueError("Titolare non valido")
        self._titolare = titolare # assegna all'attributo interno
    
    @property
    def saldo(self):
        return self._saldo # legge l'attributo interno
    
    @saldo.setter
    def saldo(self, saldo: int|float):
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("Saldo non valido")
        self._saldo = saldo # assegna all'attributo interno
    
    
    def deposita(self, importo: int|float):
        if not isinstance(importo, (int, float)) or importo < 0:
            raise ValueError("Importo non valido")
        self._saldo += importo
    
    
    def preleva(self, importo: int|float):
        if not isinstance(importo, (int, float)) or importo < 0 or importo > self.saldo:
            raise ValueError("Importo non valido")
        self._saldo -= importo
    
    def __str__(self):
        return f"Nome titolare: {self.titolare}\nSaldo corrente: {self.saldo}"

# deposita e preleva sono definiti come metodi (non come @property), quindi si può passare un 
# argomento (cb.deposita(50)), che è l’uso più naturale.

cb = ContoBancario("Nico", 0)
print(cb)

cb.deposita(50)
print(cb)

cb.deposita(1000)
cb.preleva(125)
print(cb)
