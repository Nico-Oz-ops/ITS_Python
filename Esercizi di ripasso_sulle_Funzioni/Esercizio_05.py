# Esercizio 5
'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.
'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    prodotti_scontati = {}

    for prodotto, valore in prodotti.items():
        if prodotti[prodotto] > 20:
            prodotti_scontati[prodotto] = valore - (valore * 0.1)
    
    return prodotti_scontati

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0}))
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
print(filtra_e_mappa({}))