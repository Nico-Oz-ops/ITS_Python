# Esercizio 4
'''
1. Scrivi una nuova classe chiamata Cibo, che dovrebbe 
   avere come attributi nome, prezzo e descrizione.
2. Crea almeno tre cibi diversi che conosci e ti piacciono.
3. Crea una nuova classe chiamata Menu, che dovrebbe avere una lista (di Cibi) come attributo. 
   Il metodo __init__ dovrebbe prendere una lista di Cibi come parametri opzionali (predefiniti come lista vuota []).
4. Crea i metodi aggiungiCibo() e rimuoviCibo() per il Menu.
5. Crea alcune nuove istanze di Cibo. Aggiungi ognuna al Menu usando i rispettivi metodi.
6. Aggiungi un metodo stampaPrezzi() che elenchi tutti gli articoli nel Menu con i loro prezzi.
7. Aggiungi un metodo del Menu chiamato getPrezzoMedio() che restituisca il prezzo medio dei Cibi nel Menu.
'''
# classe Cibo con gli attributi: nome, prezzo, descrizione
class Cibo:
    def __init__(self, nome:str, prezzo:float, descrizione:str):
        self.nome = nome
        self.prezzo = prezzo
        self.descrizione = descrizione

# creare 3 cibi che mi piacciono
pinsa = Cibo("Pinsa alla 'nduja", 6.50, "Pinsa con pomodoro, mozzarella, 'nduja")
pasta = Cibo("Carbonara", 9.50, "Spaghetti con guanciale, tuorli, pecorino romano, pepe")
hamburger = Cibo("Hamburger", 10.00, "Panino con carne di manzo, pomodor e formaggio")

class Menu:
    def __init__(self):
        self.cibi:list = []
    
    def aggiungiCibo(self, cibo:str):
        self.cibi.append(cibo)
    
    def rimuoviCibo(self, cibo:str):
        if cibo in self.cibi:
            self.cibi.remove(cibo)
    
    def stampaPrezzi(self):
        for cibo in self.cibi:
            print(f"\nNome: {cibo.nome}\nPrezzo: {cibo.prezzo}\nDescrizione: {cibo.descrizione}")

    def getPrezzoMedio(self):
        if len(self.cibi) == 0:
            return 0
        total = sum(cibo.prezzo for cibo in self.cibi)
        return total / len(self.cibi)

# creare una istanza del menu
menu = Menu()

# aggiungo alcuni cibi al menu
menu.aggiungiCibo(pinsa)
menu.aggiungiCibo(pasta)
menu.aggiungiCibo(hamburger)

# creare alcune nuove istanze di Cibo e aggiungo ognuna al Menu
menu.aggiungiCibo(Cibo("Lasagna", 11.50, "Lasagna con ragù, besciamella e formaggio"))
menu.aggiungiCibo(Cibo("Insalata", 6.25, "Insalata mista con vinagrette"))

# calcolo e stampo il prezzo medio
prezzo_medio = menu.getPrezzoMedio()
print(f"Il prezzo medio è {prezzo_medio: .2f}")
print("-" * 40)

# stampo prezzi di tutti i cibi
menu.stampaPrezzi()

        
    

        