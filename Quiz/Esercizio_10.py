# Esercizio 10

'''
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.
'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict1_copia = dict1.copy() # creo una copia del primo dizionario per evitare modificare il dizionario originale

    for key, value in dict2.items(): # itero sul secondo dizionario
        if key in dict1_copia: # se la chiave è presente in risultato (copia del dizionario 1), sommo i valori
            dict1_copia[key] += value
        
        else:
            dict1_copia[key] = value
    
    return dict1_copia

print(merge_dictionaries({'x': 5}, {'x': -5}))


# opzione 2
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    for key, value in dict2.items(): # itero sul secondo dizionario
        if key in dict1: # se la chiave è presente in dict1, sommo i valori
            dict1[key] += value
        
        else:
            dict1[key] = value
    
    return dict1

print(merge_dictionaries({'x': 5}, {'x': -5}))
