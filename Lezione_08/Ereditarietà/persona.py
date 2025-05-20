class Persona:
    '''All'interno del costruttore, vengono chiamati 
    i metodi setName, setLastname e setAge 
    per impostare i valori degli attributi. 
    Questi metodi si occupano di eseguire eventuali 
    validazioni sui dati prima di assegnarli.'''
    def __init__(self, name:str, lastname:str, age:int):
        self.setName(name)
        self.setLastName(lastname)
        self.setAge(age)

    def __str__(self):
        '''Metodo __str__: restituisce una rappresentazione 
        in formato stringa dell'oggetto, utile per la stampa.
        '''
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def __call__(self):
        '''Il metodo __call__ è un metodo speciale che permette di "chiamare" un oggetto 
        come se fosse una funzione. In altre parole, puoi eseguire un'istanza della 
        classe Persona come se fosse una funzione.
        In questo caso, il metodo controlla l'età della persona e stampa 
        un messaggio che varia a seconda dell'età
        '''
        if self.age < 18:
            print(f"{self.name} {self.lastname} è minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} è maggiorenne")
        elif 30 <= self.age < 80:
            print(f"{self.name} {self.lastname} è una persona adulta")
        else:
            print(f"{self.name} {self.lastname} è una persona anziana")
    
    def setName(self, name:str) -> None:
        '''Questo metodo imposta il nome della persona. 
        Controlla che il nome non sia una stringa vuota. 
        Se il nome è valido (non vuoto), viene assegnato all'attributo name; 
        altrimenti, viene stampato un messaggio di errore.
        '''
        if name:
            self.name = name
        else:
            print("Errore! Il nome non può essere una stringa vuota.")
    
    def setLastName(self, lastname:str) -> None:
        '''Imposta il cognome della persona. Anch'esso controlla 
        che il cognome non sia una stringa vuota.
        '''
        if lastname:
            self.lastname = lastname
        else:
            print("Errore! Il cognome non può essere una stringa vuota.")
    
    def setAge(self, age:int) -> None:
        '''Questo metodo imposta l'età della persona. Effettua un controllo che l'età 
        sia compresa tra 0 e 130. Se l'età non è valida (ad esempio, se è inferiore a 0 o superiore a 130), 
        l'età viene impostata su 0. Se l'età è valida, viene assegnata all'attributo age.
        '''
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
    
    # I metodi setName, setLastName, setAge, impostano i valori per nome, cognome ed età, con validazione.
    
    def getName(self) -> str:
        '''Restituisce il nome della persona. 
        È un semplice getter per l'attributo name.
        '''
        return self.name
    
    def getLastName(self) -> str:
        '''Restituisce il cognome della persona. 
        È un getter per l'attributo lastname.
        '''
        return self.lastname
    
    def getAge(self) -> int:
        '''Restituisce l'età della persona. 
        È un getter per l'attributo age.
        '''
        return self.age
        
        