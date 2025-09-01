'''
13. Classe Ordine con prodotti e quantità

Tema: __init__, __str__, __len__

Obiettivo: Gestire ordini complessi

Traccia:
Crea una classe Ordine con lista di tuple (Prodotto, quantità).

    * __str__ → "Ordine: prodotto1 x2, prodotto2 x1, …"
    * __len__ → numero totale di prodotti (somma delle quantità)
'''
class Prodotto:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return self.nome == other.nome

    def __str__(self):
        return f"{self.nome}"

class Ordine:
    def __init__(self, prodotti: list[tuple[Prodotto, int]] = None):
        self.prodotti = prodotti if prodotti is not None else []
    
    def aggiungiProdotto(self, prodotto: Prodotto, quantita: int = 1):
        if not isinstance(prodotto, Prodotto):
            raise ValueError("Errore, prodotto non valido")
        self.prodotti.append((prodotto, quantita))
    
    def rimuoveProdotto(self, prodotto: Prodotto, quantita: int): # rimuove per quantità esatta, semplice ma rigido
        if (prodotto, quantita) not in self.prodotti:
            raise ValueError("Errore, prodotto non si trova nella lista di prodotti")
        self.prodotti.remove((prodotto, quantita))
    
    def __len__(self):
        return sum(quantita for _, quantita in self.prodotti)
    
    def __str__(self):
        prodotto_str = ", ".join(f"{str(prodotto)} x{quantita}" for prodotto, quantita in self.prodotti)
        return f"Ordine: [{prodotto_str}]"

pizza = Prodotto("pizza")
pasta = Prodotto("pasta")

ordine1 = Ordine([])
print(ordine1)

ordine1.aggiungiProdotto(pizza, 2)
ordine1.aggiungiProdotto(pasta, 3)
print(ordine1)
print(len(ordine1))


# Opzione Chat

class Prodotto:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return self.nome == other.nome

    def __str__(self):
        return self.nome

class Ordine:
    def __init__(self, prodotti: list[tuple[Prodotto, int]] = None):
        self.prodotti = prodotti if prodotti is not None else []
    
    def aggiungiProdotto(self, prodotto: Prodotto, quantita: int = 1):
        if not isinstance(prodotto, Prodotto):
            raise ValueError("Errore, prodotto non valido")
        self.prodotti.append((prodotto, quantita))
    
    def rimuoveProdotto(self, prodotto: Prodotto, quantita: int = 1):
        # Gestire decremento quantità (più realistico, tipo un carrello e-commerce).
        # Scorro la lista dei prodotti (che contiene tuple (Prodotto, quantità))
        for i, (p, q) in enumerate(self.prodotti):
            # Se trovo il prodotto da rimuovere (confronto usando __eq__)
            if p == prodotto:
                # Caso 1: nell'ordine c'è più quantità di quella che vogliamo rimuovere
                if q > quantita:
                     # Aggiorno la tupla con quantità ridotta
                    self.prodotti[i] = (p, q - quantita)
                # Caso 2: la quantità da rimuovere è esattamente quella presente    
                elif q == quantita:
                     # Allora elimino completamente la tupla dalla lista
                    self.prodotti.pop(i)
                # Caso 3: l'utente chiede di rimuovere più pezzi di quanti ce ne sono    
                else:
                    raise ValueError("Quantità da rimuovere maggiore di quella presente")
                return
        # Se usciamo dal ciclo senza aver trovato il prodotto
        raise ValueError("Prodotto non trovato nell'ordine")
    
    def __len__(self):
        return sum(quantita for _, quantita in self.prodotti)
    
    def __str__(self):
        prodotto_str = ", ".join(f"{p} x{q}" for p, q in self.prodotti)
        return f"Ordine: [{prodotto_str}]"

# Test
pizza = Prodotto("pizza")
pasta = Prodotto("pasta")

ordine1 = Ordine()
print(ordine1)  # Ordine: []

ordine1.aggiungiProdotto(pizza, 2)
ordine1.aggiungiProdotto(pasta, 3)
print(ordine1)  # Ordine: [pizza x2, pasta x3]

ordine1.rimuoveProdotto(pizza, 1)
print(ordine1)  # Ordine: [pizza x1, pasta x3]

    
    
        
