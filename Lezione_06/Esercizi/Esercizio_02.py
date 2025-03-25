# Esercizio 02
'''
1. Scrivi una classe chiamata Studente con gli attributi nome (str) e 
corsoDiStudio (str).
2. Crea tre istanze. Una per te stesso, una per il tuo vicino di sinistra 
e una per il tuo vicino di destra.
3. Aggiungi un metodo stampaInfo che stampi il nome e il 
corsoDiStudio di uno Studente. Prova il tuo metodo sugli oggetti!
4. Modifica il codice e aggiungi età e genere agli attributi. 
Modifica anche i metodi di stampa di conseguenza.
'''
# Base
class Student:
    def __init__(self, name:str, studyProgram:str):
        self.name = name
        self.studyProgram = studyProgram
    
    def printInfo(self):
        print(f"Nome: {self.name}, Corso di Studio: {self.studyProgram}")

me = Student("Nicolàs", "Musica")
chiara = Student("Chiara", "Data Analyst")
lisa = Student("Lisa", "Ingegneria Informatica")

me.printInfo()
chiara.printInfo()
lisa.printInfo()

print("-" * 80)

# Aggiungere altri 2 attributi: età e genere
class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Nome: {self.name}, Corso di Studio: {self.studyProgram}, Età: {self.age}, Genere: {self.gender}")

me = Student("Nicolàs", "Musica", 36, "Maschile")
chiara = Student("Chiara", "Data Analyst", 25, "Femminile")
lisa = Student("Lisa", "Ingegneria Informatica", 27, "Femminile")

me.printInfo()
chiara.printInfo()
lisa.printInfo()