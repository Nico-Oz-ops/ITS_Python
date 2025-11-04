'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:

Test	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}
'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    risultato = dict1.copy()

    for chiave, valore in dict2.items():
        if chiave in risultato:
            risultato[chiave] += valore
        else:
            risultato[chiave] = valore
    
    return risultato

print(merge_dictionaries({'x': 5}, {'x': -5}))