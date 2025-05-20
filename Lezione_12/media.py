class Media:

    '''
    Attributi della classe Media
    self.title: str
    self.year: int
    '''

    # inizializzare un oggetto classe media
    def __init__(self, title:str, year:int) -> None:
        self.setTitle(title)
        self.setYear(year)
    
    # metodi setter
    def setTitle(self, title:str):
        if title:
            self.title = title
        else:
            print("Errore")
    
    def setYear(self, year:int):
        if year > 1000:
            self.year = year
        
        else:
            print("Errore")
    
    # metodi getter
    def getTitle(self) -> str:
        return self.title
    
    def getYear(self) -> int:
        return self.year
    
    def __str__(self) -> str:
        return f"\nTitolo: {self.getTitle()}\nAnno: {self.getYear()}"
        