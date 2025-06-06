# Esercizio 01

'''Liste, Tuple e Dizionari
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.'''

def lista_a_dizionario(lista: list[tuple]) -> dict:
    dizionario = {}

    for chiave, valore in lista:
        if chiave in dizionario:
            dizionario[chiave] += valore
        else:
            dizionario[chiave] = valore
    return dizionario

def classificazione_numeri(lista: list[int]) -> dict:
    dizionario = {'positivi': [], 'negativi': []}

    for numero in lista:
        if numero >= 0:
            dizionario['positivi'].append(numero)
        else:
            dizionario['negativi'].append(numero)
    return dizionario

def prodotti_sotto_50(dizionario: dict) -> dict:
    dict = {}

    for prodotto, prezzo in dizionario.items():
        if prezzo < 50:
            dict[prodotto] = round(prezzo * 1.1, 2)
    
    return dict

print(lista_a_dizionario([(5,9), (5, 4), (7, 8)]))
print(classificazione_numeri([-2, 5, 7, 9, 78, 79, -52, -63, -159]))
print(prodotti_sotto_50({"a": 51, "b": 49, "c":75, "d": 53, "e": 25}))
