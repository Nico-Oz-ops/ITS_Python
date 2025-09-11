'''
Esercizio 10 - Sistema di notifiche (avanzato)

Tema: Polimorfismo avanzato + astrazione
Obiettivo: Creare un sistema estensibile di notifiche che possa funzionare con diversi canali.

Traccia:

1. Definisci una classe astratta Notifica con un metodo astratto invia(messaggio).

    * messaggio è una stringa che rappresenta il contenuto da inviare.

2. Crea tre sottoclassi che ereditano da Notifica:

    * Email → quando viene chiamato invia(messaggio), stampa: "Invio email: <messaggio>".
    * SMS → quando viene chiamato invia(messaggio), stampa: "Invio SMS: <messaggio>".
    * Push → quando viene chiamato invia(messaggio), stampa: "Invio notifica push: <messaggio>".

3. Scrivi una funzione invia_notifiche(lista_notifiche, messaggio) che:

    * riceve una lista di oggetti di tipo Notifica.
    * invia lo stesso messaggio a tutti i canali usando un unico ciclo for.

4. Crea una lista di notifiche mista (Email, SMS, Push) e testa la funzione invia_notifiche() con un messaggio di esempio.
'''

from abc import ABC, abstractmethod

class Notifica(ABC):

    def __init__(self):
        self.messaggio = "" # attributo condiviso con tutte le sottoclassi

    @abstractmethod
    def invia(self, messaggio: str):
        pass

class Email(Notifica):
    def __init__(self):
        super().__init__()
    
    def invia(self, messaggio: str):
        self.messaggio = messaggio

        return f"Invio email: {self.messaggio}"
    
class SMS(Notifica):
    def invia(self, messaggio):
        self.messaggio = messaggio

        return f"Invio SMS: {self.messaggio}"
    
class Push(Notifica):
    def invia(self, messaggio):
        self.messaggio = messaggio

        return f"Invio notifica push: {self.messaggio}"
    

messaggio = "Attenzione: il sistema sarà in manutenzione dalle 22:00 alle 23:00."
notifiche = [Email(), SMS(), Push()]

def invia_notifiche(notifiche: list[Notifica], messaggio: str):
    for notifica in notifiche:
        print(notifica.invia(messaggio))

invia_notifiche(notifiche, messaggio)

# Versione più minimalista
class Notifica(ABC):
    @abstractmethod
    def invia(self, messaggio: str):
        pass

class Email(Notifica):
    def invia(self, messaggio):
        return f"Invio email: {messaggio}"

class SMS(Notifica):
    def invia(self, messaggio):
        return f"Invio SMS: {messaggio}"

class Push(Notifica):
    def invia(self, messaggio):
        return f"Invio notifica push: {messaggio}"

def invia_notifiche(lista_notifiche: list[Notifica], messaggio: str):
    for notifica in lista_notifiche:
        print(notifica.invia(messaggio))

notifiche = [Email(), SMS(), Push()]
messaggio = "Attenzione: il sistema sarà in manutenzione dalle 00:00 fino alle 05:00."

invia_notifiche(notifiche, messaggio)

