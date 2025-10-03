'''
pronuncia `range_sum(n)` per restituire la somma dei 
numeri da `1` a `n` inclusi; se `n` è minore o uguale a `0`, torna `0`
'''

def range_sum(n: int) -> int:
    if n <= 0:
        return 0
    else:
        return sum(range(1, n + 1))