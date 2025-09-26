'''
1. GESTIONALE PAGAMENTO
Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza 
l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro 
da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, 
ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 
50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 
0,01 euro sono necessarie per pagare l'importo in contanti.

Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il 
numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le 
informazioni della carta di credito oltre all'importo del pagamento.

Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito 
con valori differenti e si invochi dettagliPagamento() per ognuno di essi.
'''

class Pagamento:
    def __init__(self):
        self.__importo = 0.0
    
    def get_importo(self) -> float:
        return self.__importo
    
    def set_importo(self, importo: float):
        if not isinstance(importo, (int, float)) or importo < 0:
            raise ValueError("L'importo deve essere un numero positivo")
        self.__importo = float(importo)
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.__importo:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        super().dettagliPagamento()
        print("**Pagamento in contanti**")

    def inPezziDa(self):
        importo = self.get_importo()
        pezzi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        conteggio = {}

        for pezzo in pezzi:
            if importo >= pezzo:
                conteggio[pezzo] = importo // pezzo # numero di pezzi di questo taglio
                print(f"{conteggio[pezzo]} pezzi da €{pezzo:.2f}")
                importo = round(importo - conteggio[pezzo] * pezzo, 2) # aggiorn l'importo rimanente da pagare
            else:
                conteggio[pezzo] = 0
        
        return [(chiave, valore) for chiave, valore in conteggio.items() if valore > 0]

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome_titolare: str, data_scadenza: str, numero_carta: str):
        super().__init__()
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta
    
    def dettagliPagamento(self):
        super().dettagliPagamento()
        print("**Pagamento con carta di credito**")
        print(f"Titolare: {self.nome_titolare}\n"\
              f"Data di scadenza: {self.data_scadenza}\n"\
              f"Numero carta: {self.numero_carta}")
    
# Test
if __name__ == "__main__":
    contanti1 = PagamentoContanti()
    contanti1.set_importo(1234.56)
    contanti1.dettagliPagamento()
    contanti1.inPezziDa()
    print()

    contanti2 = PagamentoContanti()
    contanti2.set_importo(78.90)
    contanti2.dettagliPagamento()
    contanti2.inPezziDa()
    print()

    carta1 = PagamentoCartaDiCredito("Mario Rossi", "12/25", "1234 5678 9012 3456")
    carta1.set_importo(250.75)
    carta1.dettagliPagamento()
    print()

    carta2 = PagamentoCartaDiCredito("Luigi Bianchi", "11/24", "6543 2109 8765 4321")
    carta2.set_importo(99.99)
    carta2.dettagliPagamento()