'''
15. Classe Prodotto con rappresentazione leggibile e tecnica

Tema: __init__, __str__, __repr__, __eq__

Obiettivo: Combina tutti i metodi speciali principali

Traccia:
Crea una classe Prodotto con nome, prezzo e categoria.

    *__str__ → "Prodotto: …, Prezzo: …, Categoria: …"
    *__repr__ → "Prodotto('nome', prezzo, 'categoria')"
    *__eq__ → due prodotti uguali se nome e categoria coincidono
'''

class Prodotto:
    def __init__(self, nome: str, prezzo: float, categoria: str):
        self.nome = nome
        self.prezzo = prezzo
        self.categoria = categoria
    
    def __str__(self):
        return f"Prodotto: {self.nome}, Prezzo: {self.prezzo}, Categoria: {self.categoria}"
    
    def __repr__(self):
        return f"Prodotto('{self.nome}', {self.prezzo}, '{self.categoria}')"
    
    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.nome, self.categoria) == (other.nome, other.categoria)
    
    def __hash__(self): # bisogna utilizzarlo sia per un set o come chiave di un dict
        return hash((self.nome, self.categoria))

prodotto1 = Prodotto("Laptop", 1200.50, "Elettronica")
prodotto2 = Prodotto("Laptop", 1300.00, "Elettronica")
prodotto3 = Prodotto("T-shirt", 19.99, "Abbigliamento")
prodotto4 = Prodotto("Caffè", 4.50, "Alimentari")

print(prodotto1)
print(prodotto2)
print(prodotto3)
print(prodotto4)
print(f"Prodotto 1 e Prodotto 2, sono uguali?", prodotto1 == prodotto2)
print(f"Prodotto 1 e Prodotto 3, sono uguali?", prodotto1 == prodotto3)
print(f"Prodotto 3 e Prodotto 4, sono uguali?", prodotto3 == prodotto4)

# Test extra - suggerito da Chat

# Lista di prodotti con alcuni duplicati (stesso nome e categoria)
prodotti = [
    Prodotto("Laptop", 1200.50, "Elettronica"),
    Prodotto("Laptop", 1500.00, "Elettronica"),  # duplicato logico
    Prodotto("T-shirt", 19.99, "Abbigliamento"),
    Prodotto("T-shirt", 25.00, "Abbigliamento"), # duplicato logico
    Prodotto("Caffè", 4.50, "Alimentari"),
]

print("\nLista prodotti:")
for p in prodotti:
    print(p)

# Confronti diretti
print("\nConfronti diretti:")
print("Laptop1 == Laptop2 ?", prodotti[0] == prodotti[1])
print("T-shirt1 == T-shirt2 ?", prodotti[2] == prodotti[3])
print("Laptop == Caffè ?", prodotti[0] == prodotti[4])

# Uso di set per vedere i duplicati logici
print("\nProdotti unici (per nome e categoria):")
print(set(prodotti))  # usa __eq__ e __repr__

'''
In Python gli oggetti personalizzati diventano automaticamente non hashable se hanno l’uguaglianza ridefinita.

Se voglio che i miei Prodotto funzionino bene dentro set o come chiavi di un dict, 
basta aggiungere il metodo __hash__.
In questo caso, visto che due prodotti sono uguali se hanno stesso nome e categoria, 
l’hash deve basarsi su queste due proprietà.

Altrimenti, se non si aggiunge il metodo __hash__ ci sarà un errore di tipo 
"TypeError: unhashable type: 'Prodotto'"
'''
