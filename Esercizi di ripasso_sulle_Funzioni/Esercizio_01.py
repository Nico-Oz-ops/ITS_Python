# Esercizio 1
'''
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. 
Se ci sono valori duplicati, scarta i duplicati.
'''
# versione dict comprehension
# def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
#     inversione_dict = {valore: chiave for chiave, valore in dizionario.items()}

#     return inversione_dict

# print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))


# versione ciclo for
def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:
    inversione_dict = {}

    for chiave, valore in dizionario.items():
        if valore not in inversione_dict:
            inversione_dict[valore] = chiave

    return inversione_dict

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))
print(inverti_mappa({'a': 1, 'b': 1, 'c': 2}))
print(inverti_mappa({'a': 2, 'b': 1, 'c': 2}))
print(inverti_mappa({}))
