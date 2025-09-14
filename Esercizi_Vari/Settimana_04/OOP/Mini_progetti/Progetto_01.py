'''
Tema: OOP - Integrazione di classi, ereditarietà e polimorfismo.

Obiettivo: Creare un piccolo sistema per gestire studenti e corsi, usando classi, 
incapsulamento, ereditarietà e polimorfismo.

Nome dell’esercizio: gestione_studenti_corsi

Traccia:

1. Crea una classe Studente con:

    * attributi: nome, cognome, voti (lista di interi).
    * un metodo aggiungi_voto(voto) per aggiungere un voto.
    * una property media che calcola la media dei voti.

2. Crea due sottoclassi di Studente:

    * StudenteLaurea → la media si calcola normalmente.
    * StudenteMaster → la media è ponderata: ogni voto vale doppio.

3. Crea una classe Corso con:

    * attributi: nome_corso, studenti (lista di studenti iscritti).
    * un metodo aggiungi_studente(studente) per iscrivere uno studente.
    * un metodo mostra_studenti() che stampa nome, cognome e media di ciascuno.

4. Dimostra il polimorfismo:

    * iscrivi almeno un StudenteLaurea e un StudenteMaster allo stesso corso.
    * mostra come media restituisce valori diversi a seconda della sottoclasse.
'''

class Studente:
    def __init__(self, nome: str, cognome: str, voti: list[int] = None):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti if voti is not None else []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido")
        self._nome = nome
    
    @property
    def cognome(self):
        return self._cognome
    
    @cognome.setter
    def cognome(self, cognome: str):
        if not isinstance(cognome, str) or cognome.strip() == "":
            raise ValueError("Cognome non valido")
        self._cognome = cognome
    
    @property
    def voti(self):
        return self._voti
    
    @voti.setter
    def voti(self, voti: list[int]):
        for voto in voti:
            if not isinstance(voto, int) or voto < 0 or voto > 30:
                raise ValueError("Voto non valido")
        self._voti = voti
    
    def aggiungi_voto(self, voto: int):
        if not isinstance(voto, int) or voto < 0 or voto > 30:
            raise ValueError("Voto non valido")
        self.voti.append(voto)
    
    @property 
    def media(self):
        if self.voti == []:
            raise ValueError("Lista di voti vuota, non si può calcolare la media")
        return sum(self.voti) / len(self.voti)
    
    def __str__(self):
        return f"Nome: {self.nome} - Cognome: {self.cognome} - Media: {self.media:.2f}"

class StudenteLaurea(Studente):
    pass

class StudenteMaster(Studente):
    @property
    def media(self):
        if self.voti == []:
            raise ValueError("Lista vuota, non si può calcolare la media")
        
        somma_voti_ponderati = 0
        somma_pesi = 0
        for voto in self.voti:
            if not isinstance(voto, int) or voto < 0 or voto > 30:
                raise ValueError("Voto non valido")
            
            somma_voti_ponderati += voto * 2 # ogni voto vale doppio (voto * n)
            somma_pesi += 2 # ogni voto ha peso 2 (somma_pesi += n)
        
        media_ponderata = somma_voti_ponderati / somma_pesi # (calcolo per la media ponderata)
        return media_ponderata
    
    # Osservazione: avrei potuto calcolare la media così -> sum(voto * 2 for voto in self.voti)/len(self.voti),
    # ma in questa maniera la media supera il voto massimo 30.

class Corso:
    def __init__(self, nome_corso: str, studenti: list[Studente] = None):
        self.nome_corso = nome_corso
        self.studenti = studenti if studenti is not None else []
    
    @property
    def nome_corso(self):
        return self._nome_corso
    
    @nome_corso.setter
    def nome_corso(self, nome_corso: str):
        if not isinstance(nome_corso, str) or nome_corso.strip() == "":
            raise ValueError("Nome del corso non valido")
        self._nome_corso = nome_corso
    
    @property
    def studenti(self):
        return self._studenti
    
    @studenti.setter
    def studenti(self, studenti: list[Studente]):
        for studente in studenti:
            if not isinstance(studente, Studente):
                raise ValueError("Studente non valido")
        self._studenti = studenti
    
    def aggiungi_studente(self, studente: Studente):
        if not isinstance(studente, Studente):
            raise ValueError("Studente non valido")
        self.studenti.append(studente)
    
    def mostra_studenti(self):
        # creo una lista di stringhe, una per ogni studente usando __str__
        studenti_str = "\n".join(str(studente) for studente in self.studenti)
        return f"Corso: {self.nome_corso}\n" + studenti_str


# Creo studenti
studentelaurea1 = StudenteLaurea("Nico", "Rojas")
studentemaster1 = StudenteMaster("Benja", "Valen")

# Aggiungo voti
studentelaurea1.aggiungi_voto(28)
studentelaurea1.aggiungi_voto(27)

studentemaster1.aggiungi_voto(29)
studentemaster1.aggiungi_voto(30)

# Creo corso
informatica = Corso("Informatica")
informatica.aggiungi_studente(studentelaurea1)
informatica.aggiungi_studente(studentemaster1)

# Mostro studenti
print(informatica.mostra_studenti())
            

        