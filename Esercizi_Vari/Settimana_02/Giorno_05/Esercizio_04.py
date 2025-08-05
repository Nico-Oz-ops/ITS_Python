'''
Tema: Ricorsione su dizionario
Obiettivo: Sommare tutti i valori numerici (int o float) presenti in un dizionario.
'''

# Esercizio 04
# Titolo: "somma_valori"

'''
Traccia:
Scrivi una funzione ricorsiva che prende un dizionario e restituisce 
la somma di tutti i valori che sono numeri interi o float. Ignora gli altri valori.

Suggerimento:
Estrai una chiave, controlla il valore, somma se numerico, 
e richiama la funzione sul dizionario senza quella chiave.
'''

def somma_valori(diz: dict) -> float:

    if len(diz) == 0:
        return 0
    
    chiave = next(iter(diz)) # con next(iter()) posso prendere una chiave qualsiasi da un dizionario, solitamente la prima se l'ordine è stabuile
    # chiave = list(diz.key())[0]  ---> un'altra opzione per prendere una chiave dal dizionario
    valore = diz[chiave] # prendo il valore
    diz_resto = diz.copy() # si crea una copia del dizionario
    diz_resto.pop(chiave) # si rimuove la chiave corrente

    if isinstance(valore, (int, float)): # controllo se il valore è numerico
        return valore + somma_valori(diz_resto)
    
    else:
        return somma_valori(diz_resto)

print(somma_valori({'a': 5, 'b': 3.2, 'c': 'x', 'd': 2}))
print(somma_valori({'aji': -9, 'calabaza': 37.5, 'zeta': 'wess', 'd': 2.36}))


    # chiave = list(diz.key())[0]  ---> un'altra opzione per prendere una chiave dal dizionario

