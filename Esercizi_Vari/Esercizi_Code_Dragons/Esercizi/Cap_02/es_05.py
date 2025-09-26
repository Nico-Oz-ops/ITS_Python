'''
Cammina con `deep_get(d, path, default)` seguendo chiavi e indici in `path` 
tra dizionari e liste `d`; restituisci il passo ma, se manca, 
restituisci `default`. 
'''


def deep_get(d: dict | list, path: list, default=None):
    for chiave in path: # itero su ogni elemento della lista path
        if isinstance(d, dict) and chiave in d: # se l'oggetto corrente (d) è un dizionario e contiene la chiave... 
            d = d[chiave] # aggiorno d con il valore corrispondente a quella chiave
        elif isinstance(d, list) and isinstance(chiave, int) and 0 <= chiave < len(d): # invece se l'oggetto è una lista è la chiave è un indice intero valido
            d = d[chiave] # allora aggiorno d con l'elemento della lista in quella posizione
        else:
            return default
    return d # il ciclo ritorna l'ultimo valore raggiunto 
