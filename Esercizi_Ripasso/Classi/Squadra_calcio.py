class Giocatore:

    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.ruolo = ""

    def __str__(self):
        return f"\nInformazione del giocatore: \nNome: {self.nome}\nCognome: {self.cognome}\nRuolo: {self.ruolo}"
    
    def setNome(self, nome):

        if not nome.isalpha():
            raise ValueError("Errore, il nome deve essere composto solo da lettere")
        
        self.nome = nome
    
    def setCognome(self, cognome):

        if not cognome.isalpha():
            raise ValueError("Errore: il cognome deve essere composto solo da lettere")
        
        self.cognome = cognome
    
    def setRuolo(self, ruolo):

        if not ruolo.isalpha():
            raise ValueError("Errore: il ruolo deve essere composto solo da lettere")
        
        self.ruolo = ruolo
    
    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getRuolo(self):
        return self.ruolo


class Squadra:

    def __init__(self):
        self.nome_squadra = ""
        self.giocatori:list[Giocatore] = []
    
    def setNomeSquadra(self, nome_squadra:str):
        self.nome_squadra = nome_squadra
    
    def getNomeSquadra(self) -> str:
        return self.nome_squadra
    
    def aggiungiGiocatore(self, giocatore:Giocatore):
        self.giocatori.append(giocatore)
    
    def mostraSquadra(self):
        print(f"\nSquadra: {self.nome_squadra}")
        for giocatore in self.giocatori:
            print(giocatore)
    
    def contaGiocatori(self):
        return f"\nTotale giocatori: {len(self.giocatori)}"
    
# Info del giocatore 1 
calciatore_1 = Giocatore()
calciatore_1.setNome("Mario")
calciatore_1.setCognome("Rossi")
calciatore_1.setRuolo("Attacante")
# print(calciatore_1)
# print("-" * 50)

# Info della squadra
squadra = Squadra()
squadra.setNomeSquadra("Los Marcianos")
squadra.aggiungiGiocatore(calciatore_1)
squadra.mostraSquadra()
print(squadra.contaGiocatori())

# Info del giocatore 2
calciatore_2 = Giocatore()
calciatore_2.setNome("Pichulero")
calciatore_2.setCognome("Rojo")
calciatore_2.setRuolo("Attacante")

# Info della squadra aggiornata
squadra.aggiungiGiocatore(calciatore_2)
squadra.mostraSquadra()
print(squadra.contaGiocatori())

        

        
        
        