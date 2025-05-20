class Alieno:

    '''
    Di un alieno ci interessa sapere la galassia di provenienza
    Attributo: self.galaxy (tipo stringa)
    '''

    # inizializzare un oggetto della classe Alieno

    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str) -> None:
        
        if not isinstance(galaxy, str) or galaxy.strip() == "":
         raise ValueError("Errore! La galassia di provenienza non può essere una stringa vuota")
        
        else:
            self.galaxy = galaxy
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("kjsfdsf56$%&%vdbk")
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}"