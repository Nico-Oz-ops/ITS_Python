# Esercizio 6
'''
Classe Partita
Crea una classe Partita con:
attributi: data, luogo, regole, komi, giocatore_bianco, giocatore_nero
metodo stampa_riepilogo() che stampa i dati della partita e i nickname dei due giocatori
'''

class Partita:

    def __init__(self, data:str, luogo:str, regole:str, komi:float, giocatore_bianco:str, giocatore_nero:str):
        self.data = data
        self.luogo = luogo
        self.regole = regole
        self.komi = komi
        self.giocatore_bianco = giocatore_bianco
        self.giocatore_nero = giocatore_nero

    def stampa_riepilogo(self):
        print(f"\nData: {self.data}")
        print(f"Luogo: {self.luogo}")
        print(f"Regole: {self.regole}")
        print(f"Komi: {self.komi}")
        print(f"Giocatore Bianco: {self.giocatore_bianco}")
        print(f"Giocatore Nero: {self.giocatore_nero}")        

partita_1 = Partita("2025-04-28", "Roma", "Regole ufficiali", 6.5, "yoyo195", "littleozric")
partita_1.stampa_riepilogo()