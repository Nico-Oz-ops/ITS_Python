'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa 
ogni elemento alla sua frequenza nella lista.
For example:

Test

print(frequency_dict(['mela', 'banana', 'mela']))
{'mela': 2, 'banana': 1}
'''
def frequency_dict(elements: list) -> dict:
    risultato = {}

    for elemento in elements:
        if elemento in risultato:
            risultato[elemento] += 1
        else:
            risultato[elemento] = 1
    
    return risultato

print(frequency_dict(['mela', 'banana', 'mela']))
