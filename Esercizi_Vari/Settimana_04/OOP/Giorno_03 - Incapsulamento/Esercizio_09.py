'''
Esercizio 9 - Palestra: Abbonamento

Tema: Incapsulamento e metodi di validazione

Crea una classe Abbonamento con:

    * __nome_cliente (stringa)
    * __durata_mesi (int >0)
    * __lezioni_rimanenti (int ≥0)

Metodi:

    * Getter/setter con validazione
    * usa_lezione() → decrementa __lezioni_rimanenti se >0, altrimenti errore
    * __str__()
'''
class Abbonamento:
    def __init__(self, nome_cliente: str, durata_mesi: int, lezioni_rimanenti: int):
        self.set_nome_cliente(nome_cliente)
        self.set_durata_mesi(durata_mesi)
        self.set_lezioni_rimanenti(lezioni_rimanenti)
    
    def get_nome_cliente(self) -> str:
        return self.__nome_cliente
    
    def get_durata_mesi(self) -> int:
        return self.__durata_mesi
    
    def get_lezioni_rimanenti(self) -> int:
        return self.__lezioni_rimanenti
    
    def set_nome_cliente(self, nome_cliente: str):
        if not isinstance(nome_cliente, str) or nome_cliente.strip() == "":
            raise ValueError("Errore, nome di cliente non valido.")
        self.__nome_cliente = nome_cliente
    
    def set_durata_mesi(self, durata_mesi: int):
        if not isinstance(durata_mesi, int) or durata_mesi <= 0:
            raise ValueError("Errore, valore inserito non valido.")
        self.__durata_mesi = durata_mesi
    
    def set_lezioni_rimanenti(self, lezioni_rimanenti: int):
        if not isinstance(lezioni_rimanenti, int) or lezioni_rimanenti < 0:
            raise ValueError("Errore, valore inserito non valido.")
        self.__lezioni_rimanenti = lezioni_rimanenti
    
    def usa_lezione(self, lezione: int):
        if not isinstance(lezione, int) or lezione > self.__lezioni_rimanenti:
            raise ValueError("Errore, valore non valido.")
        self.__lezioni_rimanenti -= lezione
    
    def __str__(self):
        return f"Nome cliente: {self.__nome_cliente}\nDurata: {self.__durata_mesi} mesi\nLezioni rimanenti: {self.__lezioni_rimanenti}"

abbonamento1 = Abbonamento("Nico", 12, 30)
print(abbonamento1)   

print("-" * 50)

abbonamento1.usa_lezione(20)
print(abbonamento1)

print("-" * 50)

abbonamento1.usa_lezione(8)
print(abbonamento1)

print("-" * 50)

abbonamento1.usa_lezione(5) # scatta l'errore, perché il valore inserito (5) è maggiore al numero di lezioni disponibili
print(abbonamento1)