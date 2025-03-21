class Persona:

    # costruttore
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0
    
    # funzione che mostri in output i dati relativi ad una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age} anni")
    
    # funzione che ci consenta di impostare il valore dell'attributo self.name
    def setName(self, name:str) -> None:
        self.name = name
    
    # funzione che ci consentan di impostare il valore di self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname
    
    # funzione che ci consenta di impostare un valore di self.age
    def setAge(self, age:int) -> None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age = age
    

    # funzione che mi consente di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name
    
    # funzione che mi consente di ritornare il valore di self.lastname
    def getLastname(self) -> str:
        return self.lastname

    # funzione che mi consente di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age
