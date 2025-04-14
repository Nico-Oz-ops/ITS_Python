# Esercizio 06
'''Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.'''

def rimuove_duplicati(lista:list) -> list:
    
    lista_senza_duplicati = []

    for elemento in lista:
        if elemento not in lista_senza_duplicati:
            lista_senza_duplicati.append(elemento)

    return lista_senza_duplicati

print(rimuove_duplicati([1, 2, 3, 1, 2, 4]))
print(rimuove_duplicati([4, 5, 'a', 4, 6]))