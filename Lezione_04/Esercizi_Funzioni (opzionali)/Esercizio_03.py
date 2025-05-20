# Esercizio 3
'''
Carrello degli acquisti e-commerce :

Crea una funzione che definisca un prodotto con un nome, un prezzo e una quantità.
Creare funzioni che gestiscano il carrello, consentendo all'utente di aggiungere, 
rimuovere e visualizzare i prodotti nel carrello.
Crea una funzione che calcoli il totale del carrello e applichi eventuali sconti o tasse.
Crea una funzione per stampare un riepilogo dettagliato del carrello, inclusi prodotti e totali.
Implementare un ciclo for per scorrere gli articoli nel carrello e stampare informazioni 
dettagliate su ciascun prodotto e il totale.
'''
from typing import Any

def prodotto(nome:str, prezzo:float, quantita:int) -> dict[str, Any]:
    return {
        "nome": nome,
        "prezzo": prezzo,
        "quantita": quantita,
    }

def aggiungere_prodotto(carrello:list[dict[str, Any]], prodotto: dict[str, Any]):
    carrello.append(prodotto)

def rimuovere_prodotto(carrello:list[dict[str, Any]], nome_prodotto:str) -> list[dict[str, Any]]:
    lista_aggiornata = []
    for prodotto in carrello:
        if prodotto["nome"] != nome_prodotto:
            lista_aggiornata.append(prodotto)

    return lista_aggiornata

def visualizza_carrello(carrello:list[dict[str, Any]]) -> None:
    print("I prodotti nel carrello sono: ")
    for prodotto in carrello:
        print(f"- {prodotto["name"]}: {prodotto["quantita"]}, ognuno costa {prodotto["prezzo"]}")

def totale_carrello(carrello:list[dict[str, Any]], sconto:float=0.2) -> dict[str, Any]:
        # Compute the subtotal as the sum of (price * quantity) for each product
    subtotal: float = sum(prodotto['prezzo'] * prodotto['quantita'] for prodotto in carrello)
    discount: float = sconto
    tax: float = 0.22  # VAT of 22%
    
    # Apply discount to subtotal
    discounted_total: float = subtotal * (1 - discount)
    # Apply tax to the discounted total
    total: float = discounted_total * (1 + tax)
    
    # Return all calculated amounts in a dictionary
    return {
        "subtotal": subtotal,
        "discount": discount * 100,  # As a percentage
        "tax": tax * 100,            # As a percentage
        "total": total
    }

def print_summary(carrello: list[dict[str, Any]]) -> None:
    # Print basic cart contents
    visualizza_carrello(carrello)
    print("\nDetailed Summary:")
    
    # Print each product with total price
    for prodotto in carrello:
        total_price: float = prodotto['prezzo'] * prodotto['quantita']  # type: ignore
        print(f"{prodotto['nome']} - Quantità: {prodotto['quantita']}, Unit Price: €{prodotto['price']}, Total: €{total_price}")
    
    # Calculate and print subtotal, discount, tax, and final total
    totals: dict[str, float] = calculate_total(cart)
    print("\nTotals:")
    print(f"Subtotal: €{totals['subtotal']}")
    print(f"Discount Applied: {totals['discount']}%")
    print(f"Tax: {totals['tax']}%")
    print(f"Final Total: €{round(totals['total'], 2)}")


