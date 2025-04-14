# Esercizio ripasso

class Persona:

    def __init__(self, nome="", cognome="", eta=0):
        self.setNome(nome)
        self.setCognome(cognome)
        self.setEta(eta)
    
    def setNome(self,nome:str) -> None:

        if not nome.isalpha():
            raise ValueError("Errore: il nome deve contenere solo lettere")
    
        self.nome = nome
    
    def setCognome(self, cognome:str) -> None:

        if not cognome.isalpha():
            raise ValueError("Errore: il cognome deve contenere solo lettere")
        
        self.cognome = cognome
    
    def setEta(self, eta:int) -> None:

        if eta < 0:
            raise ValueError("Errore: l'età non può essere negativa")

        elif eta > 130:
            raise ValueError("Errore: l'età non può superare i 130 anni")

        self.eta = eta
    
    def getNome(self) -> str:
        return self.nome
    
    def getCognome(self) -> str:
        return self.cognome
    
    def getEta(self) -> int:
        return self.eta
    
    def __str__(self):
        return f"Nome: {self.getNome()}\nCognome: {self.getCognome()}\nEtà: {self.getEta()}"
    
    def __call__(self):
        if self.eta < 18:
            return f"Hai {self.eta} anni, sei minorenne"
        
        elif 18 <= self.eta < 30:
            return f"Hai {self.eta} anni, sei magiorenne" 
        
        elif 30 <= self.eta < 65:
            return f"Hai {self.eta} anni, sei un adulto"
        
        else:
            return f"Hai {self.eta} sei un anziano"
        

if __name__ == "__main__":
    try:

        persona1 = Persona("Nico", "Rojas", 37)
        print("Informazioni della persona:")
        print(persona1)
        print(persona1()) # chiamata al __call__
    
    except ValueError as e:
        print(f"Errore: {e}")

    