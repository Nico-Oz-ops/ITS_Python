'''
Esercizio 8 - Biblioteca: Rivista

Tema: Incapsulamento e metodi di aggiornamento

Crea una classe Rivista con:

    * __titolo (stringa)
    * __numero (int >0)
    * __numero_copie (int ≥0)

Metodi:

    * Getter/setter con validazioni
    * aggiungi_copie(n) / rimuovi_copie(n)
    * __str__()
'''
class Rivista:
    def __init__(self, titolo: str, numero: int, numero_copie: int):
        self.set_titolo(titolo)
        self.set_numero(numero)
        self.set_numero_copie(numero_copie)
    
    def get_titolo(self) -> str:
        return self.__titolo
    
    def get_numero(self) -> int:
        return self.__numero
    
    def get_numero_copie(self) -> int:
        return self.__numero_copie
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Errore, titolo non valido.")
        self.__titolo = titolo
    
    def set_numero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Errore, valore di numero non valido.")
        self.__numero = numero
    
    def set_numero_copie(self, numero_copie: int):
        if not isinstance(numero_copie, int) or numero_copie < 0:
            raise ValueError("Errore, valore di numero di copie non valido.")
        self.__numero_copie = numero_copie
    
    def aggiungi_copie(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Errore, valore non valido.")
        self.__numero_copie += n
    
    def rimuovi_copie(self, n: int):
        if not isinstance(n, int) or n > self.__numero_copie:
            raise ValueError("Errore, valore non valido.")
        self.__numero_copie -= n
    
    def __str__(self):
        return f"Titolo: {self.__titolo}, Numero: {self.__numero}, Num. Copie: {self.__numero_copie}"

rivistaDB = Rivista("Don Balòn", 125, 1450)
print(rivistaDB)

print("-" * 50)

rivistaDB.aggiungi_copie(500)
print(rivistaDB)

print("-" * 50)

rivistaDB.rimuovi_copie(1225)
print(rivistaDB)


# Opzione suggerita da Chat - metodo rimuovi() "user friendly"
class Rivista:
    def __init__(self, titolo: str, numero: int, numero_copie: int):
        self.set_titolo(titolo)
        self.set_numero(numero)
        self.set_numero_copie(numero_copie)
    
    def get_titolo(self) -> str:
        return self.__titolo
    
    def get_numero(self) -> int:
        return self.__numero
    
    def get_numero_copie(self) -> int:
        return self.__numero_copie
    
    def set_titolo(self, titolo: str):
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Titolo non valido")
        self.__titolo = titolo
    
    def set_numero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Numero non valido")
        self.__numero = numero
    
    def set_numero_copie(self, numero_copie: int):
        if not isinstance(numero_copie, int) or numero_copie < 0:
            raise ValueError("Numero di copie non valido")
        self.__numero_copie = numero_copie
    
    # User-friendly: aggiunge solo valori positivi
    def aggiungi_copie(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Numero di copie da aggiungere non valido")
        self.__numero_copie += n
    
    # User-friendly: non va mai sotto zero
    def rimuovi_copie(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Numero di copie da rimuovere non valido")
        self.__numero_copie = max(self.__numero_copie - n, 0)
    
    def __str__(self):
        return f"Titolo: {self.__titolo}, Numero: {self.__numero}, Num. Copie: {self.__numero_copie}"


# --- Test ---
rivistaDB = Rivista("Don Balòn", 125, 1450)
print(rivistaDB)
print("-" * 50)

rivistaDB.aggiungi_copie(500)
print(rivistaDB)
print("-" * 50)

# Anche se proviamo a rimuovere più copie di quante ce ne siano, non va in negativo
rivistaDB.rimuovi_copie(2000)
print(rivistaDB)

    