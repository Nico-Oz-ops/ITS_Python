'''
Esercizio 6 - Dipendenti

Crea una classe base Dipendente con attributi nome e stipendio.

Crea due sottoclassi:

    * Impiegato (aggiungi attributo bonus)
    * Manager (aggiungi attributo team_size)

Override del metodo __str__() per mostrare le informazioni complete di ciascun ruolo.
'''

class Dipendente:
    def __init__(self, nome: str, stipendio: float):
        self.set_nome(nome)
        self.set_stipendio(stipendio)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_stipendio(self) -> float:
        return self.__stipendio
    
    def set_nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido.")
        self.__nome = nome
    
    def set_stipendio(self, stipendio: float):
        if not isinstance(stipendio, (int, float)) or stipendio <= 0:
            raise ValueError("Stipendio non valido.")
        self.__stipendio = stipendio
    
    def __str__(self):
        return f"Nome dipendente: {self.__nome}\nStipendio: {self.__stipendio} euro"

class Impiegato(Dipendente):
    def __init__(self, nome: str, stipendio: float, bonus: float):
        super().__init__(nome, stipendio)
        self.set_bonus(bonus)
    
    def get_bonus(self) -> float:
        return self.__bonus
    
    def set_bonus(self, bonus: float):
        if not isinstance(bonus, (int, float)) or bonus < 0:
            raise ValueError("Bonus non valido.")
        self.__bonus = bonus
    
    def __str__(self):
        return super().__str__() + f"\nBonus: {self.__bonus}"

class Manager(Dipendente):
    def __init__(self, nome: str, stipendio: float, team_size: int):
        super().__init__(nome, stipendio)
        self.set_team_size(team_size)
    
    def get_team_size(self) -> int:
        return self.__team_size
    
    def set_team_size(self, team_size: int):
        if not isinstance(team_size, int) or team_size < 0:
            raise ValueError("Team size non valido.")
        self.__team_size = team_size
    
    def __str__(self):
        return super().__str__() + f"\nTeam size: {self.__team_size}"

impiegato = Impiegato("Pietro", 2150.00, 575.50)
manager = Manager("Giuseppe", 3000, 5)

print(impiegato)
print("-" * 40)
print(manager)
        