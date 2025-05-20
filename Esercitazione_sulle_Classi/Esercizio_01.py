# Esercizio 1
'''
Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di 
prestito e restituzione degli stessi. Gli utenti del sistema devono essere in 
grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali 
libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. 
Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. 
    Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, 
    lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, 
    lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
    Se non ci sono libri disponibili, restituisce un messaggio di errore.
'''

class Libro:

    def __init__(self, titolo:str, autore:str, prestato=False):
        self.titolo = titolo
        self.autore = autore
        self.prestato = prestato
    
    def __str__(self):
        stato = "Prestato" if self.prestato else "Disponibile"
        return f"'{self.titolo}' di '{self.autore}'"
    
class Biblioteca:

    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro:Libro):
        self.catalogo.append(libro)
        
        return f"Hai aggiunto {libro} al catalogo della biblioteca"
    
    def presta_libro(self, titolo:str):

        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                if not libro.prestato:
                    libro.prestato = True
                    return f"Libro '{libro.titolo}' prestato con successo"
                
                else:
                    return f"Libro '{libro.titolo}' è stato già prestato"
        
        return f"Non si è trovato nessun libro con il titolo '{titolo}'"
    
    def restituisci_libro(self, titolo:str):

        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                if libro.prestato:
                    libro.prestato = False
                    return f"Libro '{libro.titolo}' restituito con successo"
                
                else:
                    return f"Il libro '{libro.titolo}' non è stato prestato"
        
        return f"Non si è trovato nessun libro con il titolo '{titolo}'"
    
    def mostra_libri_disponibili(self):

        disponibili = [libro.titolo for libro in self.catalogo if not libro.prestato]

        if disponibili:
            return f"Libri disponibili:\n- " + "\n- ".join(disponibili)
        
        else:
            return "In questo momento non ci sono libri disponibili"
        
# creazione della biblioteca (oggetto)
mia_biblioteca = Biblioteca()

# si aggiungono alcuni libri alla biblioteca
print(mia_biblioteca.aggiungi_libro(Libro("I miei stupidi intenti", "Bernardo Zanoni")))
print(mia_biblioteca.aggiungi_libro(Libro("A brave new world", "Aldous Huxley")))
print("-" * 50)

# prestito di un libro
print(mia_biblioteca.presta_libro("i miei stupidi intenti"))
print(mia_biblioteca.presta_libro("1984"))
print("-" * 50)

# visualizzare i libri disponibili
print(mia_biblioteca.mostra_libri_disponibili())
print("-" * 50)

# restituire un libro
print(mia_biblioteca.restituisci_libro("1984"))
print(mia_biblioteca.restituisci_libro("i miei stupidi intenti"))
print("-" * 50)

# mostrare i libri disponibili
print(mia_biblioteca.mostra_libri_disponibili())




                
                



    
        


        