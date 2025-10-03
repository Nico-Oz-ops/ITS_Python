'''
Lascialo risuonare con `apply_twice(fn, x)`, applicando 
`fn` a `x` due volte di seguito e restituendo il risultato finale.
'''

def apply_twice(fn, x):
    return fn(fn(x))

