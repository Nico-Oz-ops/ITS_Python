'''
15. Catalogo Prodotti Unici

Tema: __eq__, __hash__, uso con set e dict.

Obiettivo: Gestire un catalogo di prodotti unici, evitando duplicati logici.

Traccia:
Crea una classe Catalogo che permette di:

    * Aggiungere un prodotto (aggiungi_prodotto).
    * Vedere tutti i prodotti unici (mostra_prodotti).
    * Controllare se un prodotto esiste già nel catalogo (__contains__).
    * Dare la lunghezza del catalogo (__len__).

I prodotti duplicati (stesso nome e categoria) non devono essere 
aggiunti due volte, anche se hanno prezzo diverso.
'''
class Prodotto:
    def __init__(self, nome: str, prezzo: float, categoria: str):
        self.nome = nome
        self.prezzo = prezzo
        self.categoria = categoria
    
    def __str__(self):
        return f"Prodotto: '{self.nome}', Prezzo: {self.prezzo}, Categoria: '{self.categoria}'"
    
    # def __repr__(self):
    #     return f"Prodotto('{self.nome}', {self.prezzo}, '{self.categoria}')"
    
    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.nome, self.categoria) == (other.nome, other.categoria)
    
    def __hash__(self):
        return hash((self.nome, self.categoria))

class Catalogo:
    def __init__(self):
        self.prodotti = set() # # un set per evitare duplicati logici (grazie a __eq__ e __hash__ in Prodotto)
    
    def aggiungereProdotto(self, prodotto: Prodotto):
        if not isinstance(prodotto, Prodotto):
            raise ValueError("Errore, prodotto non valido")
        self.prodotti.add(prodotto)
    
    def rimuovereProdotto(self, prodotto: Prodotto):
        if prodotto not in self.prodotti:
            raise ValueError("Errore, prodotto non trovato")
        self.prodotti.remove(prodotto)
    
    def mostraProdotti(self):
        for prodotto in self.prodotti:
            print(prodotto)
        
    def __contains__(self, prodotto: Prodotto):
        return prodotto in self.prodotti # # permette di fare: prodotto in catalogo
    
    def __len__(self):
        return len(self.prodotti)
    
    # def __str__(self): # non è necessario usare questo metodo perché ho già il metodo "mostraProdotti"
    #     prodotto_str = "\n".join(str(prodotto) for prodotto in self.prodotti)
    #     return f"{prodotto_str}"


p1 = Prodotto("Laptop", 1200.50, "Elettronica")
p2 = Prodotto("Laptop", 1300.00, "Elettronica")  # duplicato logico
p3 = Prodotto("Caffè", 4.50, "Alimentari")

catalogo = Catalogo()
catalogo.aggiungereProdotto(p1)
catalogo.aggiungereProdotto(p2) # non viene aggiunto
catalogo.aggiungereProdotto(p3)

print("Contenuto del catalogo:")
catalogo.mostraProdotti()

print("-" * 30)

print("Verifica presenza di prodotto:")
print(p2 in catalogo)
print(Prodotto("T-shirt", 19.99, "Abbigliamento") in catalogo)
print("-" * 30)

print("Lunghezza del catalogo:")
print(len(catalogo))
print("-" * 30)

p4 = Prodotto("T-shirt", 19.99, "Abbigliamento")
catalogo.aggiungereProdotto(p4)
catalogo.mostraProdotti()