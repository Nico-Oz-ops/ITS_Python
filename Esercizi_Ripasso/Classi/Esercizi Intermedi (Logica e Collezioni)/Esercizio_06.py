# Esercizio 6
'''
Classe base: Giocatore
Crea una classe Giocatore con:
attributi: nickname, nome, cognome, indirizzo, rank
un metodo stampa_info() che stampa tutte le informazioni del giocatore in modo leggibile.
un metodo aggiorna_rank(nuovo_rank) per aggiornare il rank del giocatore
un metodo confronta_rank(altro_giocatore) per confrontare due giocatori in base ai loro rank
'''

class Giocatore:

    def __init__(self, nickname:str, nome:str, cognome:str, indirizzo:str, rank:int):
        self.nickname = nickname
        self.nome = nome
        self.cognome = cognome
        self.indirizzo = indirizzo
        self.rank = rank
    
    def stampa_info(self):

        print(f"\nNickname: {self.nickname}\nNome: {self.nome}\nCognome: {self.cognome}\nIndirizzo: {self.indirizzo}\nRank: {self.rank}")
    
    def aggiorna_rank(self, nuovo_rank:int):

        if nuovo_rank > self.rank:
            nuovo_rank = self.rank
            print(f"Il rank di {self.nickname} è stato aggiornato a {self.rank}")
    
    def confronta_rank(self, altro_giocatore:str):

        if altro_giocatore.rank > self.rank:
            print(f"{altro_giocatore.nickname} ha un rank più alto di {self.nickname}")
        
        elif altro_giocatore.rank < self.rank:
            print(f"{altro_giocatore.nickname} ha un rank minore di {self.nickname}")
        
        else:
            print(f"I giocatori {altro_giocatore.nickname} e {self.nickname} hanno lo stesso rank")


# Creazione di due giocatori
giocatore_1 = Giocatore("yoyo195", "Miguel", "Contreras", "Via Las Petunias 195", 195)
giocatore_2 = Giocatore("littleozric", "Nico", "Rojas", "Via Los Alamos 15", 150)

# Stampa info
giocatore_1.stampa_info()
print("-" * 50)
giocatore_2.stampa_info()

# Aggiornamento del rank
print("-" * 50)
giocatore_1.aggiorna_rank(210)

# Confronto tra i giocatori
print("-" * 50)
giocatore_1.confronta_rank(giocatore_2)

        