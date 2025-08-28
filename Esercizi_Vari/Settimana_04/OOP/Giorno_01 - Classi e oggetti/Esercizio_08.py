'''
Tema: Aggiornamento stato interno
Obiettivo: Simulare un piccolo oggetto “interattivo”

Nome: Conto Bancario

Traccia:
Crea una classe ContoBancario con attributo saldo inizializzato a 0.
Aggiungi metodi versa(importo) e preleva(importo) per modificare il saldo.
Crea un conto, versa 100, preleva 30, e stampa il saldo finale.
'''

class ContoBancario:

    def __init__(self, saldo: int):
        self.saldo = saldo
    
    def versa(self, importo: int):
        self.saldo += importo
        
    def preleva(self, importo: int):
        if self.saldo >= importo:
            self.saldo -= importo

        else:
            return "Saldo insufficiente"
    
    def mostra_saldo(self):
        return self.saldo


conto = ContoBancario(0)
conto.versa(100)
print(conto.mostra_saldo())
conto.preleva(30)
print(conto.mostra_saldo())
