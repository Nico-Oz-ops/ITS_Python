'''
Esercizio 2 - Pagamenti

Tema: Polimorfismo pratico
Obiettivo: Definire un’interfaccia comune con comportamenti diversi.

Traccia:
    *Crea una classe MetodoPagamento con il metodo paga(importo).
    *Crea sottoclassi CartaDiCredito, PayPal, Bonifico.
    *Ogni sottoclasse stampa un messaggio diverso per confermare il pagamento.
    *Simula un checkout con una lista di metodi e fai pagare un importo.
'''
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):

    @abstractmethod
    def paga(self, importo: int|float):
        pass

class CartaDiCredito(MetodoPagamento):
    def paga(self, importo: int|float):
        return f"Pagamento '{importo}' effettuato con carta di credito"

class PayPal(MetodoPagamento):
    def paga(self, importo: int|float):
        return f"Pagamento '{importo}' realizzato tramite PayPal"

class Bonifico(MetodoPagamento):
    def paga(self, importo: int|float):
        return f"Il pagamento '{importo}' è stato effettuato tramite bonifico bancario"

metodi_pagamento = [CartaDiCredito(), PayPal(), Bonifico()]
importo = 575.50

for metodo in metodi_pagamento:
    print(metodo.paga(importo))
