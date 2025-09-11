'''
Esercizio 15 - Giocatore di Basket

Tema: Classe con più proprietà collegate e calcoli dinamici.
Obiettivo: Implementare una piccola classe “Giocatore” con statistiche e bonus che influenzano altri valori.

Traccia:

1. Crea una classe Giocatore con attributi: nome (str), punti (list[int]), bonus (int).

2. Validare: punti devono essere numeri interi ≥ 0; bonus ≥ 0.

3. Proprietà media_punti → media dei punti + bonus.

4. Proprietà top_scorer → True se media_punti >= 20, altrimenti False.

5. Metodo aggiungi_punti(punti: int) → aggiunge un punteggio alla lista, controllando la validità.

6. Metodo aggiungi_bonus(punti: int) → incrementa il bonus.

7. __str__ → restituisce nome, media_punti, top_scorer e bonus.

* Suggerimento: Usa _punti e _bonus come attributi privati e proprietà per validare i valori.
'''

class Giocatore:
    def __init__(self, nome: str, bonus: int, punti: list[int] = None):
        self.nome = nome
        self.bonus = bonus
        self.punti = punti if punti is not None else []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido")
        self._nome = nome
    
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, bonus: int):
        if not isinstance(bonus, int) or bonus < 0:
            raise ValueError("Bonus non valido")
        self._bonus = bonus
    
    @property
    def punti(self):
        return self._punti
    
    @punti.setter
    def punti(self, punti: list[int]):
        for punto in punti:
            if not isinstance(punto, int) or punto < 0:
                raise ValueError("Punti non validi")
        self._punti = punti
    
    @property
    def media_punti(self):
        if self.punti == []:
            raise ValueError("Lista vuota, non si può calcolare la media")
        return (sum(self.punti) / len(self.punti)) + self.bonus
    
    @property
    def top_scorer(self):
        return self.media_punti >= 20
    
    def aggiungi_punti(self, punti: int):
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Punti non validi")
        self.punti.append(punti)

    def aggiungi_bonus(self, punti: int):
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Punti non validi")
        self.bonus += punti
    
    def __str__(self):
        return f"Nome: {self.nome}\nMedia Punti: {self.media_punti}\nTop_scorer: {self.top_scorer}\nBonus: {self.bonus}"

giocatore1 = Giocatore("Nico", 0, [])

giocatore1.aggiungi_punti(15)
giocatore1.aggiungi_punti(15)
print(giocatore1)

print("-" * 20)

giocatore1.aggiungi_bonus(6)
print(giocatore1)