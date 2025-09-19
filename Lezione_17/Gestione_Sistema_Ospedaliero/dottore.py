from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization: str, parcel: float):
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            self.specialization = None
            print("La specializzazione non è una stringa!")
        
        if isinstance(parcel, float):
            self.parcel = parcel
        
        else:
            self.parcel = None
            print("La parcella inserita non è un float")
    
    @property
    def specialization(self):
        return self.__specialization
    
    @specialization.setter
    def specialization(self, specialization: str):
        if not isinstance(specialization, str) or specialization.strip() == "":
            print("La specializzazione non è una stringa!")
            self.__specialization = None
        else:
            self.__specialization = specialization
    
    @property
    def parcel(self):
        return self.__parcel
    
    @parcel.setter
    def parcel(self, parcel: float):
        if isinstance(parcel, (int,float)):
            self.__parcel = float(parcel)
        else:
            self.__parcel = None
            print("La parcella inserita non è un float")
        
    def isAValidDoctor(self):
        if self.eta is not None and self.eta > 30:
            return f"Doctor {self.first_name} {self.last_name} is valid!"
        else:
            return f"Doctor {self.first_name} {self.last_name} is not valid!"
    
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specialization}")




