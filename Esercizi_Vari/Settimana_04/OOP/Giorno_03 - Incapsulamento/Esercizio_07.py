'''
Esercizio 7 - Gioco: Mostro

Tema: Controllo valori e metodi speciali

Crea una classe Mostro con:

    * __nome (stringa)
    * __potere (int ≥ 0)

Metodi:

    * Getter/setter con validazione
    * attacca() → stampa “Mostro <nome> attacca con potere <potere>”
    * __str__()
'''
class Mostro:
    def __init__(self, nome: str, potere: int):
        self.set_nome(nome)
        self.set_potere(potere)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_potere(self) -> int:
        return self.__potere
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore, nome non valido.")
        self.__nome = nome
    
    def set_potere(self, potere: int):
        if not isinstance(potere, int) or potere < 0:
            raise ValueError("Errore, valore di potere non valido.")
        self.__potere = potere
    
    def attacca(self):
        print(f"Mostro '{self.__nome}' attacca con potere {self.__potere}")
    
    def __str__(self):
        return f"Caratteristiche del mostro:\nNome: {self.__nome}\nPotere: {self.__potere}"

mostro1 = Mostro("Hochimingo", 265000)
print(mostro1)
mostro1.attacca()

        