'''
Evita di ripetere i passi già tracciati invocando `fib_memo(n)`, 
che calcola l'ennesimo numero della sequenza con memoria per non rifare i calcoli. 
'''

def fib_memo(n: int) -> int:
    memo = {0: 0, 1: 1}

    if n == 0 or n == 1:
        return memo[n]
    
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return memo[n]
    
print(fib_memo(10))
