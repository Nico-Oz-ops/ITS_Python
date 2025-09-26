'''
Evoca `get_or_default(d, k, default)`: restituisci `d[k]` se esiste, 
altrimenti `default`, senza modificare `d`
'''

def get_or_default(d: dict, k, default=None):
    if k in d:
        return d[k]
    return default

