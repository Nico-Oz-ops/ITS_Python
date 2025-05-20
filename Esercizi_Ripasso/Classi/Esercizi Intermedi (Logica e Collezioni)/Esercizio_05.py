# Esercizio 5
'''
Classe Corso
Attributi: nome_corso, studenti (lista)

Metodi:

iscrivi(nome_studente)

rimuovi(nome_studente)

lista_studenti() → stampa tutti gli iscritti
'''

class Corso:

    def __init__(self, nome_corso:str, studenti:list[str]):
        self.nome_corso = nome_corso
        self.studenti = studenti
    
    def iscrivi(self, nome_studente:str):
        if nome_studente not in self.studenti:
            self.studenti.append(nome_studente)
            print(f"{nome_studente} è stato iscritto al corso di '{self.nome_corso}'")
        
        else:
            print(f"{nome_studente} è già iscritto al corso di '{self.nome_corso}'")
    
    def rimuovi(self, nome_studente:str):
        if nome_studente in self.studenti:
            self.studenti.remove(nome_studente)
            print(f"{nome_studente} è stato rimosso dal corso di '{self.nome_corso}'")
        
        else:
            print(f"{nome_studente} non è iscritto al corso di '{self.nome_corso}'")
    
    def lista_studenti(self):
        print("\nLa lista degli studenti iscritti al corso sono:\n")

        for i, studente in enumerate(self.studenti, 1):
            print(f"{i} - {studente}")

corso_mat = Corso("Matematica", ["Luis", "Juan", "Roberto", "Luca", "Nicolò"])
corso_mat.lista_studenti()

corso_mat.iscrivi("Mattia")
corso_mat.lista_studenti()

corso_mat.rimuovi("Juan")
corso_mat.lista_studenti()