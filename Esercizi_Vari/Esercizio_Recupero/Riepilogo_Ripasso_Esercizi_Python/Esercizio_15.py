'''
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un 
nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%.

For example:

Test
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
{'Zaino': 45.0, 'Quaderno': 19.8}

print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
{}
'''
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    risultato = {}

    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            risultato[prodotto] = round(prezzo * 0.9, 2)
        
    return risultato

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))




