'''
1. Classe Corso
Rappresenta un corso (materia o insegnamento) offerto dalla scuola.
 
Attributi
    * nome: stringa
    * docente: stringa (o oggetto Docente, se vuoi estendere dopo)
    * studenti_iscritti: lista di oggetti Studente
    * attivo: booleano (True se il corso è attivo)
 
Metodi:
* __init__
* attiva() → imposta attivo = True
* disattiva() → imposta attivo = False
* aggiungi_studente(studente: Studente) → aggiunge uno studente alla lista
* rimuovi_studente(studente: Studente) → rimuove lo studente
* __str__() → restituisce una stringa tipo: "Corso di Matematica tenuto da Rossi (3 studenti, Attivo)"
 
 
2. Classe Studente
Rappresenta uno studente iscritto alla scuola.
 
Attributi
    * nome: stringa
    * id_studente: stringa
    * corsi_iscritti: lista di oggetti Corso
    
Metodi
* __init__
* iscriviti_corso(corso: Corso) → aggiunge il corso alla lista e iscrive lo studente nel corso
* abbandona_corso(corso: Corso) → rimuove il corso dalla lista e dallo stesso corso
* __str__() → restituisce "Nome (ID: S001) - Corsi: [Matematica, Inglese]"
 
 
3.Classe Scuola
Rappresenta l’intero sistema della scuola digitale.
 
Attributi
    * nome: stringa
    * studenti: dizionario di oggetti Studente, chiave: id_studente
    * corsi: dizionario di oggetti Corso, chiave: nome
 
Metodi
* __init__
* aggiungi_studente(studente: Studente)
* aggiungi_corso(corso: Corso)
* iscrivi_studente_a_corso(id_studente: str, nome_corso: str)
* rimuovi_studente_da_corso(id_studente: str, nome_corso: str)
* lista_corsi_attivi() → restituisce tutti i corsi con attivo == True
* __str__() → stampa un riepilogo con numero studenti e corsi
'''
from __future__ import annotations

class Corso:
    def __init__(self, nome: str, docente: str):
        self.nome = nome
        self.docente = docente
        self.studenti_iscritti: list[Studente] = []
        self.attivo: bool = False
    
    def attiva(self):
        if not self.attivo:
            self.attivo = True
        else:
            print(f"Il corso {self.nome} è già attivo")
    
    def disattiva(self):
        if self.attivo:
            self.attivo = False
        
        else:
            print(f"Il corso {self.nome} non è attivo")
    
    def aggiungi_studente(self, studente: Studente):
        if studente not in self.studenti_iscritti:
            self.studenti_iscritti.append(studente)
        else:
            print(f"Lo studente {studente.nome} è già iscritto")
    
    def rimuovi_studente(self, studente: Studente):
        if studente in self.studenti_iscritti:
            self.studenti_iscritti.remove(studente)
        else:
            print(f"Lo studente {studente.nome} non fa parte degli studenti iscritti al corso")
    
    def __str__(self):
        stato_corso = "Attivo" if self.attivo else "Non attivo"
        return f"Corso di  {self.nome} tenuto da {self.docente} ({len(self.studenti_iscritti)}, {stato_corso})"

class Studente:
    def __init__(self, nome: str, id_studente: str):
        self.nome = nome
        self.id_studente = id_studente
        self.corsi_iscritti: list[Corso] = []
    
    def iscriviti_corso(self, corso: Corso):
        if corso not in self.corsi_iscritti:
            self.corsi_iscritti.append(corso)
            corso.aggiungi_studente(self)
    
    def abbandona_corso(self, corso: Corso):
        if corso in self.corsi_iscritti:
            self.corsi_iscritti.remove(corso)
            corso.rimuovi_studente(self)
    
    def __str__(self):
        corsi = ", ".join(corso.nome for corso in self.corsi_iscritti)
        return f"{self.nome} (ID: {self.id_studente}) - Corsi: [{corsi}]"

class Scuola:
    def __init__(self, nome: str):
        self.nome = nome
        self.studenti: dict[str, Studente] = {}
        self.corsi: dict[str, Corso] = {}
    
    def aggiungi_studente(self, studente: Studente):
        if studente not in self.studenti:
            self.studenti[studente.id_studente] = studente
    
    def aggiungi_corso(self, corso: Corso):
        if corso not in self.corsi:
            self.corsi[corso.nome] = corso
    
    def iscrivi_studente_a_corso(self, id_studente: str, nome_corso: str):
        if id_studente not in self.studenti:
            print(f"Lo studente con ID {id_studente} non esiste")
            return
        
        if nome_corso not in self.corsi:
            print(f"Il corso '{nome_corso}' non esiste")
            return
        
        studente = self.studenti[id_studente]
        corso = self.corsi[nome_corso]

        return studente.iscriviti_corso(corso)

    def rimuovi_studente_da_corso(self, id_studente: str, nome_corso: str):
        if id_studente not in self.studenti:
            print(f"Lo studente con ID {id_studente} non esiste")
            return
        
        if nome_corso not in self.corsi:
            print(f"Il corso '{nome_corso}' non esiste")
            return
        
        studente = self.studenti[id_studente]
        corso = self.corsi[nome_corso]

        return studente.abbandona_corso(corso)
    
    def lista_corsi_attivi(self):
        corsi_attivi = [corso for corso in self.corsi.values() if corso.attivo]
        return corsi_attivi
    
    def __str__(self):
        num_studenti = len(self.studenti)
        num_corsi = len(self.corsi)
        num_corsi_attivi = len([corso for corso in self.corsi.values() if corso.attivo])

        return (f"\nNumero di studenti: {num_studenti}\n"
                f"Numero di corsi: {num_corsi}\n"
                f"Numero di corsi attivi: {num_corsi_attivi}")
    
