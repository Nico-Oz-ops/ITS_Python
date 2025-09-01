'''
12. Classe Studente con iscrizioni multiple

Tema: __init__, __str__, __len__, __eq__

Obiettivo: Gestire corsi a cui è iscritto

Traccia:
Crea una classe Studente con nome e lista di corsi.

    * __str__ → "Studente: …, Corsi: …"
    * __len__ → numero di corsi
    * __eq__ → due studenti uguali se hanno gli stessi corsi
'''
class Corso:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"
    
    def __eq__(self, other): 
    # due corsi con lo stesso nome vengono considerati uguali, anche se sono oggetti diversi in memoria.
        if not isinstance(other, Corso):
            return NotImplemented
        return self.nome == other.nome
    
    def __lt__(self, other):
    # permette di ordinare i corsi alfabeticamente.
        if not isinstance(other, Corso):
            return NotImplemented
        return self.nome < other.nome
    
class Studente:
    def __init__(self, nome: str, corsi: list[Corso] = None):
        self.nome = nome
        self.corsi = corsi if corsi is not None else []
    
    def aggiungiCorso(self, corso: Corso):
        if not isinstance(corso, Corso):
            raise ValueError ("Errore, corso non valido")
        self.corsi.append(corso)
    
    def removeCorso(self, corso: Corso):
        if corso not in self.corsi:
            raise ValueError ("Errore, questo corso non fa parte della lista dei corsi")
        self.corsi.remove(corso)
    
    def __len__(self):
        return len(self.corsi)
    
    def __eq__(self, other):
    # confronta sia il nome sia la lista di corsi.
        if not isinstance(other, Studente):
            return NotImplemented
        return (self.nome, self.corsi) == (other.nome, other.corsi) 

    def __lt__(self, other):
    # ordina studenti per nome e corsi.
        return (self.nome, self.corsi) < (other.nome, other.corsi)

    def __str__(self):
        corso_str = ", ".join(str(corso) for corso in self.corsi)
        return f"Nome: {self.nome} - Corsi: [{corso_str}]"



corso1 = Corso("Python 6")
corso2 = Corso("Intelligenza Artificiale 1")
corso3 = Corso("Progettazione 2")
corso4 = Corso("React")

studente1 = Studente("Luis", [])
studente2 = Studente("Federico", [])
studente3 = Studente("Camillo", [])
studente4 = Studente("Federico", [])
print(studente1)
print(studente2)
print(studente3)
print(studente4)

print("-" * 50)

studente1.aggiungiCorso(corso1)
studente1.aggiungiCorso(corso3)
studente2.aggiungiCorso(corso2)
studente3.aggiungiCorso(corso1)
studente3.aggiungiCorso(corso4)
studente4.aggiungiCorso(corso2)
print(studente1)
print(studente2)
print(studente3)
print(studente4)
print(studente4 == studente2)
print(studente1 == studente3)


