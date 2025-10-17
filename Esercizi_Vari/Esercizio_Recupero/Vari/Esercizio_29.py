'''
Esercizio - Top Spending Customers

Tema: Ordinamento e selezione di dati aggregati

Obiettivo: Individuare i clienti che hanno speso di più

Nome dell’esercizio: Top Spending Customers

Traccia:
Scrivi una funzione chiamata top_spending_customers che riceve una lista di dizionari contenenti "cliente" e "totale".
La funzione deve restituire una lista di tuple ordinate in ordine decrescente per totale speso, 
dove ogni tupla è nella forma (cliente, totale_speso).

Esempio di input:

[
    {"cliente": "Anna", "totale": 50},
    {"cliente": "Marco", "totale": 30},
    {"cliente": "Luca", "totale": 75}
]

Esempio di output:

[("Luca", 75), ("Anna", 50), ("Marco", 30)]
'''
# Alternativa 1 - uso di lambda
def top_spending_customers(clienti: list[dict[str, float]]) -> list[tuple[str, float]]:
    risultato = []

    for cliente in clienti:
            nome_cliente = cliente["cliente"]
            totale_cliente = cliente["totale"]
    
            risultato.append((nome_cliente, totale_cliente))
        
    risultato.sort(key=lambda x: x[1], reverse=True)

    return risultato

clienti = [
    {"cliente": "Anna", "totale": 50},
    {"cliente": "Marco", "totale": 30},
    {"cliente": "Luca", "totale": 75}
]

print(top_spending_customers(clienti))


# Alternativa 2 - bubble sort
def top_spending_customers(clienti: list[dict[str, float]]) -> list[tuple[str, float]]:
    risultato_2 = []

    for cliente in clienti:
        nome_cliente = cliente["cliente"]
        totale_cliente = cliente["totale"]

        risultato_2.append((nome_cliente, totale_cliente))
    
    n = len(risultato_2)

    for i in range(n):
        for j in range(0, n - i - 1):
            if risultato_2[j][1] < risultato_2[j + 1][1]:
                risultato_2[j], risultato_2[j + 1] = risultato_2[j + 1], risultato_2[j]
    return risultato_2

clienti = [
    {"cliente": "Anna", "totale": 50},
    {"cliente": "Marco", "totale": 30},
    {"cliente": "Luca", "totale": 75}
]

print(top_spending_customers(clienti))
        


    
