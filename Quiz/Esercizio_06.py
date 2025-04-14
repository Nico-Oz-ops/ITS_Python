# Esercizio 6
'''
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
'''

def remove_duplicates(lista:list) -> list:
    lista_senza_duplicati = []

    for elemento in lista:
        if elemento not in lista_senza_duplicati:
            lista_senza_duplicati.append(elemento)

    return lista_senza_duplicati

print(remove_duplicates([4, 5, 'a', 4, 6,'a', 4]))
        
    

