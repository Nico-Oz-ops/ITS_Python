'''
Scrivi un programma in Python che gestisca le informazioni principali di una scuola.
Crea le seguenti classi:
 
Persona
- Attributi: nome, cognome, eta
- Metodo: presentazione() → restituisce una stringa con nome completo ed età.
 
Studente (eredita da Persona)
- Attributi aggiuntivi: matricola, voti (lista di numeri)
Metodi:
- aggiungi_voto(voto)
- media_voti() → restituisce la media dei voti
- presentazione() → sovrascrive quello di Persona aggiungendo la matricola
 
Docente (eredita da Persona)
- Attributi aggiuntivi: materia
- Metodo: presentazione() → sovrascrive quello di Persona includendo la materia
 
ClasseScolastica
- Attributi: nome_classe, docente, studenti (lista di oggetti Studente)
Metodi:
- aggiungi_studente(studente)
- rimuovi_studente(matricola)
- media_classe() → restituisce la media complessiva di tutti gli studenti
'''

class Persona:
    def __init__(self, nome: str, cognome: str, eta: int):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def presentazione(self) -> str:
        return f"Mi chiamo {self.nome} {self.cognome} e ho {self.eta} anni."

class Studente(Persona):
    def __init__(self, nome, cognome, eta, matricola: str):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola
        self.voti: list[int] = []
    
    def aggiungi_voto(self, voto: int):
        if not isinstance(voto, int):
            raise ValueError("Errore, voto non valido")
        if voto not in self.voti:
            self.voti.append(voto)
    
    def media_voti(self):
        if not self.voti:
            return 0

        somma = 0
        for voto in self.voti:
            if not isinstance(voto, int):
                raise ValueError("Errore: voto non valido")
            somma += voto
        
        media = somma / len(self.voti)

        return media
    
    def presentazione(self):
        return f"Mi chiamo {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è: {self.matricola}"

class Docente(Persona):
    def __init__(self, nome, cognome, eta, materia: str):
        super().__init__(nome, cognome, eta)
        self.materia = materia
    
    def presentazione(self):
        return f"Mi chiamo {self.nome} {self.cognome}, ho {self.eta} anni e insegno {self.materia}"


class ClasseScolastica:
    def __init__(self, nome_classe: str, docente: Docente):
        self.nome_classe = nome_classe
        self.docente = docente
        self.studenti: list[Studente] = []

    def aggiungi_studente(self, studente: Studente):
        if studente not in self.studenti:
            self.studenti.append(studente)
    
    def rimuove_studente(self, matricola: str):
        for studente in self.studenti:
            if studente.matricola == matricola:
                self.studenti.remove(studente)
        
        print(f"Nessun studente con matricola '{matricola}' è stato trovato")
    
    def media_classe(self):
        if not self.studenti:
            return 0
        
        somma_totale = 0
        conteggio_voti = 0

        for studente in self.studenti:
            somma_totale += sum(studente.voti)
            conteggio_voti += len(studente.voti)

        if conteggio_voti == 0:
            return 0
        
        return somma_totale / conteggio_voti