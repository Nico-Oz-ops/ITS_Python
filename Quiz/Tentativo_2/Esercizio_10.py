# Esercizio 10
'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''

def merge_dictionaries(dict1:dict, dict2:dict) -> dict:
    dict1_copy = dict1.copy()

    for key, value in dict2.items():

        if key in dict1_copy:
            dict1_copy[key] += value

        else:
            dict1_copy[key] = value 
            
    return dict1_copy

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({}, {}))
print(merge_dictionaries({'a': 3}, {'b': 4}))