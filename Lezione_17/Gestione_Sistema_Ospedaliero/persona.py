'''
Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. 
Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, 
ed un attributo privato di tipo int per l'età.

- La classe Persona deve avere i seguenti metodi:

*init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; 
in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio 
di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, 
assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, 
allora assegnare None all'età.

* setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio 
di errore, ad esempio "Il nome inserito non è una stringa!".

* setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di 
errore, ad esempio "Il cognome inserito non è una stringa!".

* setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene 
modificato se e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad 
esempio "L'età deve essere un numero intero!".

* getName(): consente di ritornare il nome di una persona.

* getLastname(): consente di ritornare il cognome di una persona.

* getAge(): consente di ritornare l'età di una persona.

* greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
'''

class Persona:
    def __init__(self, first_name: str|None, last_name: str|None):

        if isinstance(first_name, str):
            self.first_name = first_name
        else:
            self.first_name = None
            print("Il nome inserito non è una stringa!")

        if isinstance(last_name, str):
            self.last_name = last_name
        else:
            self.last_name = None
            print("Il cognome inserito non è una stringa!")
        
        if self.first_name is not None and self.last_name is not None:
            self.eta = 0
        else:
            self.eta = None
    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name: str):
        if not isinstance(first_name, str) or first_name.strip() == "":
            print("Il nome inserito non è una stringa!")
            self.__first_name = None
        else:
            self.__first_name = first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        if not isinstance(last_name, str) or last_name.strip() == "":
            print("Il nome inserito non è una stringa!")
            self.__last_name = None
        else:
            self.__last_name = last_name
    
    @property
    def eta(self):
        return self.__eta 
    
    @eta.setter
    def eta(self, eta: int):
        if eta is None:
            self.__eta = None
        elif not isinstance(eta, int) or eta < 0:
            raise ValueError("L'età deve essere un numero intero!")
        else:
            self.__eta = eta
    
    def greet(self):
        if self.first_name and self.last_name and self.eta is not None:
            print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.eta} anni")


# p1 = Persona("Mario", "Rossi")
# p1.eta = 25
# p1.greet()
# Ciao, sono Mario Rossi! Ho 25 anni

# p2 = Persona(123, "Rossi")
# print(p2.greet())
# # Il nome inserito non è una stringa!
# # Ciao, non ho dati completi.

# p3 = Persona("Anna", "")
# print(p3.greet())
# # Il cognome inserito non è una stringa!
# # Ciao, non ho dati completi.