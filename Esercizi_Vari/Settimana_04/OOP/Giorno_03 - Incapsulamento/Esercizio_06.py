'''
Esercizio 6 - Gioco: Personaggio

Tema: Attributi privati e metodi di aggiornamento

Crea una classe Personaggio con:

    * __nome (stringa)
    * __vita (int ≥ 0)
    * __mana (int ≥ 0)

Metodi:

    * Getter e setter per tutti gli attributi
    * subisci_danno(punti) → riduce vita, non può diventare negativa
    * usa_mana(punti) → riduce mana, non può diventare negativa
    * __str__() leggibile
'''
class Personaggio:
    def __init__(self, nome: str, vita: int, mana: int):
        self.set_nome(nome)
        self.set_vita(vita)
        self.set_mana(mana)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_vita(self) -> int:
        return self.__vita
    
    def get_mana(self) -> int:
        return self.__mana
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore, nome non valido")
        self.__nome = nome
    
    def set_vita(self, vita: int):
        if not isinstance(vita, int) or vita < 0:
            raise ValueError("Errore, valore di vita non valido")
        self.__vita = vita
    
    def set_mana(self, mana: int):
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("Errore, valore di mana non valido")
        self.__mana = mana
    
    def subisci_danno(self, punti: int):
        if not isinstance(punti, int) or punti > self.__vita:
            raise ValueError("Errore, valore di punti non validi")
        self.__vita -= punti
    
    def usa_mana(self, punti: int):
        if not isinstance(punti, int) or punti > self.__mana:
            raise ValueError("Errore, valore di punti di uso di mana non validi")
        self.__mana -= punti
    
    def __str__(self):
        return f"Caratteristiche del personaggio:\nNome: {self.__nome}\nVita: {self.__vita}\nMana: {self.__mana}"

personaggio1 = Personaggio("Peech", 65500, 14500)
print(personaggio1)

print("-" * 50)

personaggio1.subisci_danno(15000)
personaggio1.usa_mana(2850)
print(personaggio1)

print("-" * 50)

personaggio1.subisci_danno(20000)
personaggio1.usa_mana(12000) # scatta l'errore
print(personaggio1)

        
# Opzione suggerita da Chat - "user-friendly" nei metodi subisci_danni() e usa_mana()

class Personaggio:
    def __init__(self, nome: str, vita: int, mana: int):
        self.set_nome(nome)
        self.set_vita(vita)
        self.set_mana(mana)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_vita(self) -> int:
        return self.__vita
    
    def get_mana(self) -> int:
        return self.__mana
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido")
        self.__nome = nome
    
    def set_vita(self, vita: int):
        if not isinstance(vita, int) or vita < 0:
            raise ValueError("Valore di vita non valido")
        self.__vita = vita
    
    def set_mana(self, mana: int):
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("Valore di mana non valido")
        self.__mana = mana
    
    # User-friendly: vita non diventa negativa
    def subisci_danno(self, punti: int):
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Danno non valido")
        self.__vita = max(self.__vita - punti, 0)
    
    # User-friendly: mana non diventa negativa
    def usa_mana(self, punti: int):
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Mana non valido")
        self.__mana = max(self.__mana - punti, 0)
    
    def __str__(self):
        return (f"Caratteristiche del personaggio:\n"
                f"Nome: {self.__nome}\nVita: {self.__vita}\nMana: {self.__mana}")

# --- Test ---
personaggio1 = Personaggio("Peech", 65500, 14500)
print(personaggio1)
print("-" * 50)

personaggio1.subisci_danno(15000)
personaggio1.usa_mana(2850)
print(personaggio1)
print("-" * 50)

# Anche se i punti superano i valori, non genera errore
personaggio1.subisci_danno(60000)
personaggio1.usa_mana(20000)
print(personaggio1)
