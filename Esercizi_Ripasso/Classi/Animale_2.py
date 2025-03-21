class Animale_2:

    def __init__(self):
        self.nome = ""
        self.razza = ""
        self.zampe = 0
        self.colore = ""

    def displayData(self) -> None:
        return f"Nome: {self.nome}\nRazza: {self.razza}\nZampe: {self.zampe}\nColore: {self.colore}"
    
    def setName(self, nome:str) -> None:
        self.nome = nome
    
    def setRace(self, razza:str) -> None:
        self.razza = razza

    def setPaws(self, zampe:int) -> None:
        self.zampe = zampe
    
    def setColor(self, colore:str) -> None:
        self.colore = colore
        
    def getName(self) -> str:
        return self.nome
    
    def getRace(self) -> str:
        return self.razza
    
    def getPaws(self) -> int:
        return self.zampe
    
    def getColor(self) -> str:
        return self.colore


