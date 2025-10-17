'''
Tema: Ordinamento personalizzato e trasformazione di strutture dati

Obiettivo: Ordinare una lista di dizionari e restituire i risultati come lista di tuple

Nome dell’esercizio: Ordinare prodotti per prezzo (crescente)

Traccia:
Scrivi una funzione chiamata sort_products_by_price che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta un prodotto e contiene le chiavi "nome" e "prezzo".

La funzione deve ordinare i prodotti dal meno costoso al più costoso utilizzando l’algoritmo Bubble Sort, 
senza usare funzioni integrate come sorted().

Dopo aver ordinato i dati, la funzione deve restituire una lista di tuple, dove ogni tupla è nella forma:
(nome, prezzo)

È consentito l’uso di lambda per accedere ai valori del dizionario durante il confronto.

Esempio di input:

[
    {"nome": "Mela", "prezzo": 1.2},
    {"nome": "Banana", "prezzo": 0.8},
    {"nome": "Pera", "prezzo": 1.5}
]

Esempio di output:

[
    ("Banana", 0.8),
    ("Mela", 1.2),
    ("Pera", 1.5)
]

Suggerimento:
Puoi usare una lambda per accedere al prezzo di ciascun prodotto:

chiave_prezzo = lambda prodotto: prodotto["prezzo"]
'''

# Alternativa 1 - bubble sort
def sort_products_by_price(prodotti: list[dict[str, float]]) -> list[tuple[str, float ]]:
    lista_ordinata = []

    for prodotto in prodotti:
        nome_prodotto = prodotto["nome"]
        prezzo_prodotto = prodotto["prezzo"]

        lista_ordinata.append((nome_prodotto, prezzo_prodotto))
    
    n = len(lista_ordinata)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordinata[j][1] > lista_ordinata[j + 1][1]:
                lista_ordinata[j], lista_ordinata[j + 1] = lista_ordinata[j + 1], lista_ordinata[j]
    
    return lista_ordinata

prodotti = [
    {"nome": "Mela", "prezzo": 1.2},
    {"nome": "Banana", "prezzo": 0.8},
    {"nome": "Pera", "prezzo": 1.5}
]
print(sort_products_by_price(prodotti))


# Alternativa 2 - lambda
def sort_products_by_price(prodotti: list[dict[str, float]]) -> list[tuple[str, float ]]:
    prodotti_ordinati = []

    for prodotto in prodotti:
        nome = prodotto["nome"]
        prezzo = prodotto["prezzo"]

        prodotti_ordinati.append((nome, prezzo))

        prodotti_ordinati.sort(key=lambda x: x[1])
    
    return prodotti_ordinati

prodotti = [
    {"nome": "Mela", "prezzo": 1.2},
    {"nome": "Banana", "prezzo": 0.8},
    {"nome": "Pera", "prezzo": 1.5}
]
print(sort_products_by_price(prodotti))

