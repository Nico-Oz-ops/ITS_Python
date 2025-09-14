'''
Progetto 2 - Libreria con libri e utenti (con classe astratta)

Tema: OOP - Libreria con classi astratte, ereditarietà e polimorfismo.

Obiettivo: Creare un sistema per gestire libri e utenti di una libreria, usando classi astratte, 
ereditarietà, polimorfismo e incapsulamento.

Traccia:

1. Classe astratta LibroBase

Attributi comuni:

    * titolo: str
    * autore: str
    * disponibile: bool (True se disponibile, False se in prestito)

Metodi:

    * __str__() → metodo astratto (da implementare nelle sottoclassi)
    * prestito() → imposta disponibile = False se il libro è libero
    * restituisci() → imposta disponibile = True

2. Sottoclassi concrete

LibroCartaceo:

    * Attributo aggiuntivo: numero_pagine: int
    * Implementa __str__() (mostra titolo, autore, numero di pagine, stato)

Ebook:

    * Attributo aggiuntivo: dimensione_mb: float
    * Implementa __str__() (mostra titolo, autore, dimensione in MB, stato)

3. Classe Utente

Attributi:

    * nome: str
    * cognome: str
    * libri_presi: list[LibroBase] (lista dei libri presi in prestito)

Metodi

    * prendi_in_prestito(libro) → se il libro è disponibile, lo aggiunge a libri_presi e imposta 
      disponibile = False
    * restituisci_libro(libro) → rimuove il libro da libri_presi e imposta disponibile = True
    * __str__() → mostra nome, cognome e lista dei libri presi

4. Dimostrazione del polimorfismo

    * Crea un LibroCartaceo e un Ebook
    * Stampa le loro informazioni con __str__()
    * Fai prendere in prestito i libri a un utente e mostra come cambia lo stato
    * Dimostra che entrambi i tipi di libro condividono metodi comuni (prestito, restituisci) 
      ma hanno rappresentazioni diverse tramite __str__()
'''

from abc import ABC, abstractmethod

class LibroBase(ABC):

    def __init__(self, titolo: str, autore: str, disponibile: bool = True):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = disponibile

    @property
    def titolo(self):
        return self._titolo
    
    @titolo.setter
    def titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido")
        self._titolo = titolo
    
    @property 
    def autore(self):
        return self._autore
    
    @autore.setter
    def autore(self, autore: str):
        if not isinstance(autore, str) or autore.strip() == "":
            raise ValueError("Autore non valido")
        self._autore = autore

    @property
    def disponibile(self):
        return self._disponibile
    
    @disponibile.setter
    def disponibile(self, disponibile: bool):
        if not isinstance(disponibile, bool):
            raise ValueError("'Disponibile' deve essere booleano")
        self._disponibile = disponibile
    
    def prestito(self):
        if self.disponibile == True: # oppure "if self.disponibile:"
            self.disponibile = False
            return True
        return False
    
    def restituisci(self):
        self.disponibile = True
    
    @abstractmethod
    def __str__(self):
        pass
    
class LibroCartaceo(LibroBase):
    def __init__(self, titolo, autore, numero_pagine: int, disponibile = True):
        super().__init__(titolo, autore, disponibile)
        self.numero_pagine = numero_pagine
    
    @property
    def numero_pagine(self):
        return self._numero_pagine
    
    @numero_pagine.setter
    def numero_pagine(self, numero_pagine: int):
        if not isinstance(numero_pagine, int) or numero_pagine <= 0:
            raise ValueError("Numero di pagine non validi")
        self._numero_pagine = numero_pagine
    
    def __str__(self):
        stato_libro = "Disponibile" if self.disponibile else "Non Disponibile"
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nNumero di pagine: {self.numero_pagine}\nStato: {stato_libro}"
    
class Ebook(LibroBase):
    def __init__(self, titolo, autore, dimensione_mb: float, disponibile = True):
        super().__init__(titolo, autore, disponibile)
        self.dimensione_mb = dimensione_mb
    
    @property
    def dimensione_mb(self):
        return self._dimensione_mb
    
    @dimensione_mb.setter
    def dimensione_mb(self, dimensione_mb: float):
        if not isinstance(dimensione_mb, (int, float)) or dimensione_mb <= 0:
            raise ValueError("Dimensione non valida")
        self._dimensione_mb = float(dimensione_mb)
    
    def __str__(self):
        stato_ebook = "Disponibile" if self.disponibile else "Non Disponibile"
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nDimensione: {self.dimensione_mb}MB\nStato: {stato_ebook}"
    
class Utente:
    def __init__(self, nome: str, cognome: str, libri_presi: list[LibroBase] = None):
        self.nome = nome
        self.cognome = cognome
        self.libri_presi = libri_presi if libri_presi is not None else []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido")
        self._nome = nome
    
    @property
    def cognome(self):
        return self._cognome
    
    @cognome.setter
    def cognome(self, cognome: str):
        if not isinstance(cognome, str) or cognome.strip() == "":
            raise ValueError("Cognome non valido")
        self._cognome = cognome
    
    @property
    def libri_presi(self):
        return self._libri_presi
    
    @libri_presi.setter
    def libri_presi(self, libri_presi: list[LibroBase]):
        for libro in libri_presi:
            if not isinstance(libro, LibroBase):
                raise ValueError("Libro non valido")
        self._libri_presi = libri_presi
    
    def prendi_in_prestito(self, libro: LibroBase):
        if not isinstance(libro, LibroBase):
            raise ValueError("Libro non valido")
        if libro.prestito(): # provo a prendere il libro (se è disponibile)
            self.libri_presi.append(libro)
    
    def restituisce_libro(self, libro: LibroBase):
        if not isinstance(libro, LibroBase):
            raise ValueError("Libro non valido")
        if libro in self.libri_presi:
            self.libri_presi.remove(libro)
            libro.restituisci() # aggiorno lo stato del libro
    
    def __str__(self):
        if self.libri_presi == []:
            lista_libri_presi_str = "Al momento non ci sono libri presi"
        else:
            lista_libri_presi_str = "\n".join([str(libro) for libro in self.libri_presi])
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nLibri presi: {lista_libri_presi_str}"

# def __str__(self):
    #lista_libri_presi_str = "Al momento non ci sono libri presi" if not self.libri_presi \
                            #else "\n".join([str(libro) for libro in self.libri_presi])

# Libro Cartaceo
libro1 = LibroCartaceo(
    titolo="Il nome della rosa",
    autore="Umberto Eco",
    numero_pagine=512,
    disponibile=True)
print(libro1)

print("-" * 50)

# Ebook
libro2 = Ebook(
    titolo="1984",
    autore="George Orwell",
    dimensione_mb=1.8,
    disponibile=True)
print(libro2)

print("-" * 50)

utente1 = Utente("Nico", "Vals", [])
print(utente1)

print("-" * 50)

utente2 = Utente("Xavi", "Callega", [])
utente2.prendi_in_prestito(libro1)
print(utente2)

print("-" * 50)

utente1.prendi_in_prestito(libro2)
utente2.restituisce_libro(libro1)
print(utente1)

print("-" * 50)

print(utente2)

