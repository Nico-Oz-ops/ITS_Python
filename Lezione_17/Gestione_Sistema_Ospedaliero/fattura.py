from paziente import Paziente
from dottore import Dottore

class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore):

        if doctor.isAValidDoctor():
            self.doctor = doctor
            self.patients = patients if patients is not None else []
            self.fatture = len(self.patients)
            self.salary = 0
        
        else:
            self.doctor = None
            self.patients = None
            self.fatture = None
            self.salary = None

            print("Non è possibile creare la classe fattura poichè il dottore non è valido")
        
    def getSalary(self):
        if self.doctor is not None and self.patients is not None:
            self.salary = self.doctor.parcel * len(self.patients)
            return self.salary
        return None
    
    def getFatture(self):
        if self.patients is not None:
            self.fatture = len(self.patients)
            return self.fatture
        return None

    
    def addPatient(self, newPatient: Paziente):
        if not isinstance(newPatient, Paziente):
            raise ValueError("Nuovo paziente non valido")
        self.patients.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.last_name} è stato aggiunto il paziente {newPatient.idCode}")
    
    def removePatient(self, idCode: str):
        if self.doctor is not None:
            trovato = False

            for paziente in self.patients:
                if paziente.idCode == idCode:
                    self.patients.remove(paziente)
                    trovato = True
                    break

            if trovato:
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.doctor.last_name} è stato rimosso il paziente {idCode}")
            else:
                print(f"Paziente con ID {idCode} non trovato")

        else:
            print("Operazione non possibile: dottore non trovato")




