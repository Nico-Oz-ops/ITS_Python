from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, idCode: str):
        super().__init__(first_name, last_name)
        self.idCode = idCode
    
    @property
    def idCode(self):
        return self.__idCode 
    
    @idCode.setter
    def idCode(self, idCode: str):
        if not isinstance(idCode, str) or idCode.strip() == "":
            raise ValueError("Id Code non valido")
        self.__idCode = idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\nID: {self.idCode}")

paz = Paziente("Nico", "Rojas", "15987rt")
paz.patientInfo