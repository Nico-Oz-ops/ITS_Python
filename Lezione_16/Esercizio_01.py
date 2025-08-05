# Esercizio 01
'''
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
e una classe derivata Film che rappresenti specificamente un film e ne specifichi il titolo. 
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.
 
Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, 
dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
 
Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, 
ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, 
"Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, 
il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%
Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
'''
class Media:

    def __init__(self) -> None:
        self.title = ""
        self.reviews: list[int] = []
    
    def get_title(self) -> str:
        return self.title
    
    def set_title(self, title: str) -> None:
        self.title = title
    
    def aggiungiValutazione(self, voto: int) -> None:

        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            raise ValueError("Errore, voto non valido. Inserire un voto compreso tra 1 e 5")
    
    def getMedia(self) -> float:
        if not self.reviews:
            return 0.0
        
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self) -> str:
        voto_medio = self.getMedia()

        if voto_medio < 1.5:
            return "Terribile"
        
        elif voto_medio < 2.5:
            return "Brutto"
        
        elif voto_medio < 3.5:
            return "Normale"
        
        elif voto_medio < 4.5:
            return "Bello"
        
        else:
            return "Grandioso"
    
    def ratePercentage(self, voto: int) -> float:

        if not (1 <= voto <= 5):
            raise ValueError("Errore, il voto deve essere compreso tra 1 e 5")
        
        totale = len(self.reviews)
        if totale == 0:
            return 0.0
        
        conteggio = self.reviews.count(voto)
        percentuale = (conteggio / totale) * 100

        return round(percentuale, 2)
    
    def recensione(self) -> str:
        print(f"Titolo del film: {self.get_title()}")
        print(f"Voto medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.ratePercentage(1):.2f}%")
        print(f"Brutto: {self.ratePercentage(2):.2f}%")
        print(f"Normale: {self.ratePercentage(3):.2f}%")
        print(f"Bello: {self.ratePercentage(4):.2f}%")
        print(f"Grandioso: {self.ratePercentage(5):.2f}%")

class Film(Media):
    pass


if __name__ == "__main__":

    # Primo film
    film1 = Film()
    film1.set_title("The Shawshank Redemption")
    valutazioni1 = [5, 5, 4, 4, 3, 5, 5, 4, 5, 3]
    for voto in valutazioni1:
        film1.aggiungiValutazione(voto)

    # Secondo film
    film2 = Film()
    film2.set_title("Inception")
    valutazioni2 = [4, 3, 4, 4, 5, 5, 4, 2, 3, 4]
    for voto in valutazioni2:
        film2.aggiungiValutazione(voto)

    # Stampa recensioni
    film1.recensione()
    print()
    film2.recensione()
