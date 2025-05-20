# Esercizio 7
'''
Crea una superclasse Esito e due sottoclassi EsitoRinuncia e EsitoPunteggio. 
La superclasse rappresenta un esito generico della partita, mentre le sottoclassi 
rappresentano casi più specifici di esito: uno per la rinuncia di un giocatore e l'altro per il punteggio finale.

Superclasse Esito:

Attributi:
data: la data della partita (tipo stringa).
luogo: il luogo in cui si è svolta la partita (tipo stringa).

Metodo:
descrizione(): un metodo che restituisce una descrizione generica dell'esito della partita, 
che sarà poi sovrascritto nelle sottoclassi.


Sottoclasse EsitoRinuncia:

Attributi:
rinunciatario: il nickname del giocatore che ha rinunciato (tipo stringa).

Metodo:
descrizione(): un metodo che restituisce una descrizione specifica per il caso di rinuncia, 
indicando quale giocatore ha rinunciato alla partita.


Sottoclasse EsitoPunteggio:

Attributi:
punteggio_bianco: il punteggio del giocatore bianco (tipo float).
punteggio_nero: il punteggio del giocatore nero (tipo float).

Metodo:
descrizione(): un metodo che restituisce una descrizione specifica per il caso di punteggio finale, 
indicando i punteggi ottenuti dai due giocatori.

Esempio di utilizzo:
Crea un'istanza della classe EsitoRinuncia per rappresentare una partita in cui un giocatore ha rinunciato.

Crea un'istanza della classe EsitoPunteggio per rappresentare una partita con un punteggio finale.
'''

class Esito:

    def __init__(self, data:str, luogo:str):
        self.data = data
        self.luogo = luogo
    
    def descrizione(self):
        print(f"Esito della partita del {self.data} a {self.luogo}.")

class EsitoRinuncia(Esito):

    def __init__(self, data, luogo, rinunciatario:str):
        super().__init__(data, luogo)
        self.rinunciatario = rinunciatario

    def descrizione(self):
        return f"La partita del {self.data} a {self.luogo} è stata interrotta perché '{self.rinunciatario}' ha rinunciato."

class EsitoPunteggio(Esito):

    def __init__(self, data, luogo, punteggio_bianco:float, punteggio_nero:float):
        super().__init__(data, luogo)
        self.punteggio_bianco = punteggio_bianco
        self.punteggio_nero = punteggio_nero
    
    def descrizione(self):
        return f"Il punteggio finale della partita del {self.data} a {self.luogo} è:\nGiocatore Bianco: {self.punteggio_bianco}\nGiocatore Nero: {self.punteggio_nero}"

# Esito della partita per rinuncia
esito_rinuncia = EsitoRinuncia("2025-04-28", "Roma", "yoyo195")
print(esito_rinuncia.descrizione())
print("-" * 50)

# Esito della partita con punteggio
esito_punteggio = EsitoPunteggio("2025-04-28", "Roma", 50.5, 48.0)
print(esito_punteggio.descrizione())


    

        