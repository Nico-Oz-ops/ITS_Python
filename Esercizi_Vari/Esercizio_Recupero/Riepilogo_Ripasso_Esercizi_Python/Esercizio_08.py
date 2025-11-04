'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta 
agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato 
    e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena 
    creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro 
    nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente 
    non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. 
    Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che 
    contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio 
    di errore se nessuna ricetta contiene l'ingrediente.

For example:

Test	Result
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
'''


class RecipeManager:
    def __init__(self):
        self.ricetta: dict[str, list[str]] = {}
    
    def create_recipe(self, name: str, ingredients: list[str]) -> dict|str:
        if name in self.ricetta:
            return "Errore, ricetta esiste già."
        self.ricetta[name] = ingredients

        return {name: self.ricetta[name]}
    
    def add_ingredient(self, recipe_name: str, ingredient: str) -> dict|str:
        if not recipe_name in self.ricetta:
            return "Errore, la ricetta non esiste"
        if ingredient in self.ricetta[recipe_name]:
            return "Errore, l'ingrediente esiste già"
        self.ricetta[recipe_name].append(ingredient)

        return {recipe_name: self.ricetta[recipe_name]}
    
    def remove_ingredient(self, recipe_name: str, ingredient: str) -> dict|str:
        if recipe_name not in self.ricetta:
            return "Errore, ricetta non esiste"
        if ingredient not in self.ricetta[recipe_name]:
            return "Errore, l'ingrediente non è presente"
        self.ricetta[recipe_name].remove(ingredient)

        return {recipe_name: self.ricetta[recipe_name]}
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> dict|str:
        if recipe_name not in self.ricetta:
            return "Errore, la ricetta non esiste"
        if old_ingredient not in self.ricetta[recipe_name]:
            return "Errore, l'ingrediente non è presente"
        
        index = self.ricetta[recipe_name].index(old_ingredient)
        self.ricetta[recipe_name][index] = new_ingredient

        return {recipe_name: self.ricetta[recipe_name]}
    
    def list_recipes(self) -> list[str]:
        return list(self.ricetta.keys())
    
    def list_ingredients(self, recipe_name: str) -> list[str]|str:
        if recipe_name not in self.ricetta:
            return "Errore, la ricetta non esiste"
        return self.ricetta[recipe_name]

    def search_recipe_by_ingredient(self, ingredient: str) -> dict|str:
        trovate = {name: ingredients for name, ingredients in self.ricetta.items() if ingredient in ingredients}
        
        if trovate:
            return trovate
        
        return "Errore, nessuna ricetta contiene l'ingrediente"


# Test
manager = RecipeManager()
print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
print(manager.add_ingredient("Torta di mele", "Zucchero"))
print(manager.list_recipes()) # ['Torta di mele']
print(manager.list_ingredients("Torta di mele"))
print(manager.search_recipe_by_ingredient("Uova"))