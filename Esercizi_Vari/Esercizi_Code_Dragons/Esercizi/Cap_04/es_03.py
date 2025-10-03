'''
Costruisci `compose(f, g)`, restituendo una funzione che, chiamata con `x`, 
calcola `g(x)` e poi `f` del risultato. 
'''

def compose(f, g):
    return lambda x: f(g(x))