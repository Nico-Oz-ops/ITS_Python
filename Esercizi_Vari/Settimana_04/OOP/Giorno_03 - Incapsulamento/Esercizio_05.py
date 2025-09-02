'''
Esercizio 5 - Gestione di un inventario di prodotti

Tema: Attributi privati, getter/setter, metodi di controllo
Obiettivo: Creare una classe ProdottoInventario con gestione sicura di quantità e prezzo

Traccia:
Crea una classe ProdottoInventario con attributi privati:

    * __nome (stringa)
    * __prezzo (float > 0)
    * __quantita (int ≥ 0)

Implementa:

    * get_nome(), get_prezzo(), get_quantita()
    * set_nome(nome), set_prezzo(prezzo), set_quantita(quantita) (controlli validità)
    * aggiungi_quantita(n) → aggiunge n unità (n>0)
    * rimuovi_quantita(n) → rimuove n unità se disponibili, altrimenti ValueError
    * __str__() → stampa tutte le informazioni del prodotto

Suggerimento:

    * Tutti gli attributi devono essere privati (__nome, __prezzo, __quantita)
    * Tutti i controlli di validità devono essere fatti nei setter e nei metodi di modifica della quantità
'''
class ProdottoInventario:
    def __init__(self, nome: str, prezzo: float, quantita: int):
        self.set_nome(nome)
        self.set_prezzo(prezzo)
        self.set_quantita(quantita)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_prezzo(self) -> float:
        return self.__prezzo
    
    def get_quantita(self) -> int:
        return self.__quantita
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore, nome non valido")
        self.__nome = nome
    
    def set_prezzo(self, prezzo: float):
        if not isinstance(prezzo, (int, float)) or prezzo < 0:
            raise ValueError("Errore, prezzo non valido")
        self.__prezzo = prezzo
    
    def set_quantita(self, quantita: int):
        if not isinstance(quantita, int) or quantita < 0:
            raise ValueError("Errore, quantità non valida")
        self.__quantita = quantita
    
    def aggiungi_quantita(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Errore, valore non valido")
        
        self.__quantita += n
    
    def rimuovi_quantita(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Errore, valore non valido")
        
        if n > self.__quantita:
            raise ValueError("Valore non valido")
        
        self.__quantita -= n
    
    def __str__(self):
        return f"Nome Prodotto: {self.__nome}, Prezzo: {self.__prezzo}, Quantità: {self.__quantita}"

prodotto1 = ProdottoInventario("Laptop", 1200.50, 10)
print(prodotto1)
prodotto2 = ProdottoInventario("Caffè", 4.50, 50)
print(prodotto2)

prodotto1.aggiungi_quantita(5)
print(prodotto1)
prodotto2.rimuovi_quantita(15)
print(prodotto2)
