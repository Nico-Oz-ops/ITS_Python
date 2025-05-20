class Persona:

    def __init__(self, name:str, lastname:str, age:int):
        self.setName(name)
        self.setLastName(lastname)
        self.setAge(age)
    
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def setName(self, name:str) -> None:
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Errore! Il nome deve essere una stringa e non può essere una vuota")
        
        else:
            self.name = name

    def setLastName(self, lastname:str) -> None:
        if not isinstance(lastname, str) or lastname.strip() == "":
            raise ValueError("Errore! Il cognome non può essere una stringa vuota")
        
        else:
            self.lastname = lastname

    def setAge(self, age:int) -> None:
        if not isinstance(age, int) and (age < 0 or age > 130):
            raise ValueError("Errore! L'età deve essere un valore intero e compreso tra 0 e 129 anni")
        
        else:
            self.age = age

    def getName(self) -> str:
        return self.name
    
    def getLastName(self) -> str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age
    
    def speak(self) -> None:
        print(f"\nHello! My name is {self.getName()}!\n")
    
    