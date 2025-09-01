'''
9. Classe Carrello con prodotti

Tema: __init__, __str__, __len__

Obiettivo: Gestire articoli multipli

Traccia:
Crea una classe Prodotto con nome e prezzo, poi una classe Carrello che contiene una lista di prodotti.

    * __str__ → "Carrello: prodotto1, prodotto2, …"
    * __len__ → numero di prodotti totali nel carrello
'''

class Prodotto:
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome
        self.prezzo = prezzo
    
    def __str__(self):
        return f"{self.nome} - {self.prezzo: .2f}"
    
    # def __repr__(self):
    #     return f"Prodotto('{self.nome}', {self.prezzo})"

class Carrello:
    def __init__(self, prodotti: list[Prodotto] = None):
        self.prodotti = prodotti if prodotti is not None else []
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        if not isinstance(prodotto, Prodotto):
            raise ValueError("Errore, prodotto non valido")
        self.prodotti.append(prodotto)
    
    def totale_prodotti(self):
        return sum(prodotto.prezzo for prodotto in self.prodotti)

    def __len__(self):
        return len(self.prodotti)
    
    def __str__(self):
        # Per forzare l’uso di __str__ di ogni prodotto, devo costruire manualmente la stringa della lista, 
        # in questa maniera evito implementare __repr__ sulla class Prodotto, ad esempio con un join:
        prodotto_str = ", ".join(str(prodotto) for prodotto in self.prodotti)
        return f"Carrello: [{prodotto_str}]\nProdotti totali: {len(self.prodotti)}\nPrezzo totale: {self.totale_prodotti():.2f}"
    
prodotto1 = Prodotto("Riso, 1kg", 1.655)
prodotto2 = Prodotto("Pasta integrale, 500gr", 0.99)
prodotto3 = Prodotto("Yogurt Greco, 500gr", 2.65)
prodotto4 = Prodotto("Petto di pollo, 1kg", 8.49)
prodotto5 = Prodotto("Banane, 1kg", 0.99)

carrello = Carrello([])
print(carrello)
print(len(carrello))

carrello.aggiungi_prodotto(prodotto1)
print(carrello)

carrello.aggiungi_prodotto(prodotto4)
carrello.aggiungi_prodotto(prodotto5)
print(carrello)

