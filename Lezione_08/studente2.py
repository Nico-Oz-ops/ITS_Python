from persona import Persona # la classe studente è una specializzazione della classe Persona

class Studente(Persona):

    def __init__(self, name:str, lastname:str, age:int, corso_di_studi:str, voto_medio:float):
        # Inizializza gli attributi della classe base (Persona)
        super().__init__(name, lastname, age) # super() chiama il costruttore della classe base
        self.corso_di_studi = corso_di_studi
        self.voto_medio = voto_medio
    
    def __str__(self):
        # si sovrascrive il metodo __str__ della classe base per aggiungere informazioni spoecifiche dello studente
        return super().__str__() + f"\nCorso di studi: {self.corso_di_studi}\nVoto medio: {self.voto_medio}"
    
    def studia(self):
        print(f"{self.getName()} {self.getLastName()} sta studiando per migliorare il suo voto")
    
    def __call__(self):
        # si sovrascrive il metodo __call__ della classe base (Persona) per aggiungere una logica specifica per gli studenti
        
        super().__call__() # chiama il metodo __call__ della classe base
        if self.voto_medio < 18:
            print(f"{self.getName()} {self.getLastName()} ha bisogno di migliorare i suoi voti")
        
        else:
            print(f"{self.getName()} {self.getLastName()} sta andando bene!")

# creo un'istanza della classe Studente
studente = Studente(name="Xavi", lastname="Rossi", age=25, corso_di_studi="Ingegneria Informatica", voto_medio=25)

# stampo l'oggetto
print(studente)

# chiamata del metodo __call__(verificare età e voti)
studente()

# chiamata del metodo studia
studente.studia()
