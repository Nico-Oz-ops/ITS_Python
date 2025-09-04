'''
Esercizio 10 - Biblioteca

Crea una classe Pubblicazione con attributi titolo e anno.

Crea sottoclassi:

    * Libro (autore, pagine)
    * Rivista (numero, mese)

Override di __str__() per mostrare le info specifiche.
Poi crea una lista di pubblicazioni e stampale tutte.
'''

class Pubblicazione:
    def __init__(self, titolo: str, anno: int):
        self.set_titolo(titolo)
        self.set_anno(anno)
    
    def get_titolo(self) -> str:
        return self.titolo 
    
    def get_anno(self) -> int:
        return self.anno 
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido.")
        self.titolo = titolo.title()
    
    def set_anno(self, anno: int):
        if not isinstance(anno, int) or anno < 1900:
            raise ValueError("Anno non valido")
        self.anno = anno 
    
    def __str__(self) -> str:
        return f"Titolo: {self.titolo}\nAnno: {self.anno}"

class Libro(Pubblicazione):
    def __init__(self, titolo, anno, autore: str, pagine: int):
        super().__init__(titolo, anno)
        self.set_autore(autore)
        self.set_pagine(pagine)
    
    def get_autore(self) -> str:
        return self.autore 
    
    def get_pagine(self) -> int:
        return self.pagine 

    def set_autore(self, autore: str):
        if not isinstance(autore, str) or autore.strip() == "":
            raise ValueError("Autore non valido.")
        self.autore = autore.title()
    
    def set_pagine(self, pagine: int):
        if not isinstance(pagine, int) or pagine <= 0:
            raise ValueError("Numero di pagine non valide.")
        self.pagine = pagine
    
    def __str__(self):
        return super().__str__() + f"\nAutore: {self.autore}\nNumero di pagine: {self.pagine}"

class Rivista(Pubblicazione):
    def __init__(self, titolo, anno, numero: int, mese: str):
        super().__init__(titolo, anno)
        self.set_numero(numero)
        self.set_mese(mese)
    
    def get_numero(self) -> int:
        return self.numero 
    
    def get_mese(self) -> str:
        return self.mese 
    
    def set_numero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Numero di rivista non valido.")
        self.numero = numero
    
    def set_mese(self, mese: str):
        if not isinstance(mese, str) or mese.strip() == "" or mese.capitalize() not in \
            ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]:
            raise ValueError("Mese non valido")
        self.mese = mese.capitalize()
    
    def __str__(self):
        return super().__str__() + f"\nNumero: {self.numero}\nMese: {self.mese}"

pubblicazioni = [Libro("Il nome della rosa", 1980, "Umberto Eco", 512), 
                 Libro("1984", 1949, "George Orwell", 328),
                 Rivista("national Geographic", 2023, 205, "marzo"), 
                 Rivista("Time", 2021, 48, "Dicembre")]

for pubblicazione in pubblicazioni:
    print(pubblicazione)


# Versione proposta da Chat - uso di @property (più pythonica)
class Pubblicazione:
    def __init__(self, titolo: str, anno: int):
        self.titolo = titolo
        self.anno = anno

    @property
    def titolo(self) -> str:
        return self._titolo

    @titolo.setter
    def titolo(self, valore: str):
        if not isinstance(valore, str) or valore.strip() == "":
            raise ValueError("Titolo non valido.")
        self._titolo = valore.title()

    @property
    def anno(self) -> int:
        return self._anno

    @anno.setter
    def anno(self, valore: int):
        if not isinstance(valore, int) or valore < 1900:
            raise ValueError("Anno non valido")
        self._anno = valore

    def __str__(self) -> str:
        return f"Titolo: {self.titolo}\nAnno: {self.anno}"


class Libro(Pubblicazione):
    def __init__(self, titolo, anno, autore: str, pagine: int):
        super().__init__(titolo, anno)
        self.autore = autore
        self.pagine = pagine

    @property
    def autore(self) -> str:
        return self._autore

    @autore.setter
    def autore(self, valore: str):
        if not isinstance(valore, str) or valore.strip() == "":
            raise ValueError("Autore non valido.")
        self._autore = valore.title()

    @property
    def pagine(self) -> int:
        return self._pagine

    @pagine.setter
    def pagine(self, valore: int):
        if not isinstance(valore, int) or valore <= 0:
            raise ValueError("Numero di pagine non valide.")
        self._pagine = valore

    def __str__(self):
        return super().__str__() + f"\nAutore: {self.autore}\nNumero di pagine: {self.pagine}"


class Rivista(Pubblicazione):
    def __init__(self, titolo, anno, numero: int, mese: str):
        super().__init__(titolo, anno)
        self.numero = numero
        self.mese = mese

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valore: int):
        if not isinstance(valore, int) or valore <= 0:
            raise ValueError("Numero di rivista non valido.")
        self._numero = valore

    @property
    def mese(self) -> str:
        return self._mese

    @mese.setter
    def mese(self, valore: str):
        mesi_validi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
                       "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
        valore_corr = valore.strip().capitalize()
        if valore_corr not in mesi_validi:
            raise ValueError("Mese non valido")
        self._mese = valore_corr

    def __str__(self):
        return super().__str__() + f"\nNumero: {self.numero}\nMese: {self.mese}"


# Lista di pubblicazioni
pubblicazioni = [
    Libro("Il nome della rosa", 1980, "Umberto Eco", 512),
    Libro("1984", 1949, "George Orwell", 328),
    Rivista("national Geographic", 2023, 205, "marzo"),
    Rivista("Time", 2021, 48, "Dicembre")
]

# Stampa
for pubblicazione in pubblicazioni:
    print(pubblicazione)

        