# Esercizio 2
'''
Crea una classe Contatore con:
Attributo: valore inizializzato a 0
Metodi:
incrementa() → aumenta valore di 1
stampa() → mostra valore
'''

class Contatore:

    def __init__(self, valore:int):
        self.valore = valore
    
    def incrementa(self):
        self.valore += 1

    def stampa(self):
        print(f"Il valore è: {self.valore}")

contatore = Contatore(0)
contatore.incrementa()
contatore.stampa()

# Variante interattiva

class Contatore:

    def __init__(self, valore:int):
        self.valore = valore
    
    def incrementa(self):
        self.valore += 1

    def stampa(self):
        print(f"Il valore è: {self.valore}")
    
    def reset(self):
        self.valore = 0

contatore = Contatore(0)

while True:
    comando = input("Cosa ti piacerebbe fare? (Scegliere i = incrementa, r = reset, s = stampa, e = esci): ").lower()

    if comando == "i":
        contatore.incrementa()
    
    elif comando == "r":
        contatore.reset()
    
    elif comando == "s":
        contatore.stampa()

    elif comando == "e":
        print("Stai uscendo dal programma")
        break

    else:
        print("Comando non riconosciuto")

