'''
Tema: Attributi modificabili
Obiettivo: Vedere come gli attributi possono cambiare dopo la creazione.

Nome: Contatore

Traccia:
Crea una classe Contatore con un attributo valore inizializzato 
a 0 e un metodo incrementa() che aumenta valore di 1.

Testa l’oggetto chiamando incrementa() più volte.
'''

class Contatore:

    def __init__(self):
        self.valore = 0
    
    def incrementa(self):
        self.valore += 1
        return self.valore

cont = Contatore()
print(cont.incrementa())
print(cont.incrementa())
print(cont.incrementa())
