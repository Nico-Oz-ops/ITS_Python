# Esercizio 03
'''
1. Crea due istanze realistiche di Animali.
2. Stampa il nome di ciascun oggetto.
3. Cambia la quantità di zampe di un oggetto utilizzando la notazione a punto.
4. Aggiungi un metodo setZampe() per impostare le zampe di un oggetto e ripeti il compito 3, 
   ma questa volta usando il metodo.
5. Aggiungi un metodo getZampe() per restituire il numero di zampe.
6. Aggiungi un metodo chiamato stampaInfo che stampi tutti gli attributi dell'Animale.
'''

class Animal:

    def __init__(self, name:str, legs:int):
        self.name = name
        self.legs = legs
    
    def setLegs(self, legs:int):
        self.legs = legs
    
    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(f"Nome: {self.name}, Zampe: {self.legs}")

# creazione di due istanze realistiche
cane = Animal("Cane", 4)
uccello = Animal("Aquila", 2)

# stampa il nome di ciascun oggetto
print(cane.name)
print(uccello.name)
print("-" * 50)

# cambiare la quantità di zampe degli oggetti utilizzando la notazione a punto (dot notation)
cane.legs = 5
print(f"Il {cane.name} adesso ha {cane.legs} zampe")
uccello.legs = 1
print(f"L'{uccello.name} adesso ha {uccello.legs} zampa")
print("-" * 50)

# cambia il numnero di zampe usando il metodo setLegs()
cane.setLegs(6)
print(f"Il {cane.name} adesso ha {cane.getLegs()} zampe")
uccello.setLegs(3)
print(f"L'{uccello.name} adesso ha {uccello.getLegs()} zampe")
print("-" * 50)

# usar il metodo getLegs() per ottenere il numero di zampe

print(f"Il {cane.name} ha {cane.getLegs()} zampe")
print(f"L'{uccello.name} ha {uccello.getLegs()}")
print("-" * 50)

# usare metodo printInfo() per stampare tutti gli attributi dell'Animale

cane.printInfo()
uccello.printInfo()

