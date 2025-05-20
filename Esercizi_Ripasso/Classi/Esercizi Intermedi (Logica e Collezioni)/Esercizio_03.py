# Esercizio 3
'''
Classe Negozio
Classe Prodotto:

Attributi: nome, prezzo

Classe Negozio:

Attributo: lista di prodotti

Metodi:

aggiungi_prodotto(prodotto)

totale_prodotti() → quanti prodotti ci sono

valore_totale() → somma dei prezzi

mostra_prodotti()
'''

class Prodotto:

    def __init__(self, nome:str, prezzo:float):
        self.nome = nome
        self.prezzo = prezzo
    
class Negozio:

    def __init__(self, prodotti:list[Prodotto]):
        self.prodotti = prodotti
    
    def aggiungi_prodotto(self, prodotto:Prodotto):
        self.prodotti.append(prodotto)
    
    def totale_prodotti(self):
        return len(self.prodotti)
    
    def valore_totale(self):
        return sum(prodotto.prezzo for prodotto in self.prodotti)
    
    def mostra_prodotti(self):
        print("I prodotti nel negozio sono:\n")

        for i, prodotto in enumerate(self.prodotti, 1):
            print(f"{i} - {prodotto.nome} - ${prodotto.prezzo}")



prodotto_1 = Prodotto("Pane", 1.5)
prodotto_2 = Prodotto("Latte", 2.3)

negozio = Negozio([prodotto_1])
negozio.aggiungi_prodotto(prodotto_2)

negozio.mostra_prodotti()
print("\nTotale prodotti:", negozio.totale_prodotti())
print("Valore totale: €", negozio.valore_totale())      
        
