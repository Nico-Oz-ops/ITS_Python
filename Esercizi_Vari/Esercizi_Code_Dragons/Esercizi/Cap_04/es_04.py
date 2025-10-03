'''
usa `curry_add(n)` per restituire una funzione che sommi `n` al valore ricevuto.
'''

def curry_add(n):
    return lambda x: x + n